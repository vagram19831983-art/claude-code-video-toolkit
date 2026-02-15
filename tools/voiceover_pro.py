#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parallel voiceover generation via ElevenLabs Internal API.

Ported from VoicePro_fixed.py for the video toolkit's per-scene workflow.

Features:
  - Text chunking (≤1500 chars) with sentence-boundary splitting
  - Parallel generation via ThreadPoolExecutor
  - API key rotation from base.txt on quota exhaustion
  - Evomi residential proxy with sticky session rotation
  - Firebase auth (refresh token → access token)
  - Retry logic: 10 task retries + 5 network retries
  - Resume: skips already-generated files on re-run
  - Silence padding (1.5s) after each chunk via ffmpeg

Usage:
    # Per-scene (main mode)
    python tools/voiceover_pro.py --scene-dir public/audio/scenes --base base.txt

    # Single file
    python tools/voiceover_pro.py --script VOICEOVER-SCRIPT.md --output out.mp3 --base base.txt

    # With concat for SadTalker
    python tools/voiceover_pro.py --scene-dir public/audio/scenes --base base.txt \\
        --concat public/audio/voiceover-concat.mp3

    # Custom settings
    python tools/voiceover_pro.py --scene-dir public/audio/scenes --base base.txt \\
        --voice-id ZthjuvLPty3kTMaNKVKb --speed 1.0 --threads 2 --no-proxy

    # JSON output
    python tools/voiceover_pro.py --scene-dir public/audio/scenes --base base.txt --json

Key format for base.txt (one per line):
    API_KEY:REFRESH_TOKEN
    API_KEY:REFRESH_TOKEN:DD.MM.YYYY
"""

# ─────────────────────────────  configuration  ─────────────────────────────────
DEFAULT_THREADS        = 2
DEFAULT_MIN_BYTES      = 1024
SILENCE_SEC            = 1.5
MAX_CHUNK_SIZE         = 1500

# ─ Retry settings ─
MAX_NETWORK_RETRIES    = 5
MAX_TASK_RETRIES       = 10
NETWORK_RETRY_DELAY    = 3

# ─ HTTP settings ─
MIN_ROTATE_SEC         = 31
REQUEST_TIMEOUT        = 30

# ─ Voice defaults ─
STANDARD_VOICE_ID      = "ZthjuvLPty3kTMaNKVKb"
VOICE_SIMILARITY       = 0.75
VOICE_STABILITY        = 0.39
VOICE_STYLE_EXAGGERATE = 0.0
VOICE_SPEED            = 1.0

# ─ Firebase (ElevenLabs Internal API) ─
FIREBASE_API_KEY = "AIzaSyBSsRE_1Os04-bxpd5JTLIniy3UK4OqKys"
REFRESH_URL = f"https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}"

COMMON_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/143.0.0.0 Safari/537.36",
    "Origin": "https://elevenlabs.io",
    "Referer": "https://elevenlabs.io/",
}

# ────────────────────────────  stdlib  ─────────────────────────────────────────
import argparse
import json
import os
import random
import re
import shutil
import string
import subprocess
import sys
import tempfile
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path
from queue import Empty, Queue

# ────────────────────────────  third-party  ────────────────────────────────────
import requests
from dotenv import load_dotenv

load_dotenv()


# ═══════════════════════════════════════════════════════════════════════════════
#  CLI
# ═══════════════════════════════════════════════════════════════════════════════

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Parallel voiceover generation via ElevenLabs Internal API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    # Input modes
    p.add_argument("--scene-dir", type=str,
                   help="Directory of .txt scripts (per-scene mode)")
    p.add_argument("--script", "-s", type=str,
                   help="Single script file path")
    p.add_argument("--output", "-o", type=str,
                   help="Output path for single-file mode")
    p.add_argument("--concat", type=str,
                   help="Concatenate all scene audio into one file (use with --scene-dir)")

    # Keys & proxy
    p.add_argument("--base", type=str, default="base.txt",
                   help="Path to base.txt with API keys (default: base.txt)")
    p.add_argument("--no-proxy", action="store_true",
                   help="Disable proxy (direct connection)")

    # Voice settings
    p.add_argument("--voice-id", "-v", type=str,
                   help=f"ElevenLabs voice ID (default: from env or {STANDARD_VOICE_ID})")
    p.add_argument("--speed", type=float, default=VOICE_SPEED,
                   help="Speech speed 0.70-1.2 (default: 1.0)")
    p.add_argument("--stability", type=float, default=VOICE_STABILITY,
                   help="Voice stability 0-1 (default: 0.39)")
    p.add_argument("--similarity", type=float, default=VOICE_SIMILARITY,
                   help="Similarity boost 0-1 (default: 0.75)")
    p.add_argument("--style", type=float, default=VOICE_STYLE_EXAGGERATE,
                   help="Style exaggeration 0-1 (default: 0.0)")

    # Processing
    p.add_argument("--threads", type=int, default=DEFAULT_THREADS,
                   help="Parallel threads (default: 2)")
    p.add_argument("--min-bytes", type=int, default=DEFAULT_MIN_BYTES,
                   help="Minimum MP3 file size to consider valid (default: 1024)")

    # Output format
    p.add_argument("--json", action="store_true",
                   help="JSON output for machine parsing")
    p.add_argument("--dry-run", action="store_true",
                   help="Show plan without making API calls")

    return p.parse_args()


# ═══════════════════════════════════════════════════════════════════════════════
#  PROXY (Evomi Residential Sticky)
# ═══════════════════════════════════════════════════════════════════════════════

use_proxy = True
proxy_login = os.getenv("PROXY_LOGIN", "")
proxy_password = os.getenv("PROXY_PASSWORD", "")
proxy_host = os.getenv("PROXY_HOST", "core-residential.evomi.com")
proxy_port = os.getenv("PROXY_PORT", "1000")
proxies: dict = {}

rotate_lock = threading.Lock()
last_rotate_ts = 0.0


def generate_session_id() -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


def get_proxies_dict(session: str) -> dict:
    """Evomi format: params appended to password."""
    full_password = f"{proxy_password}_country-US_session-{session}_lifetime-30"
    auth = f"{proxy_login}:{full_password}"
    return {
        "http": f"http://{auth}@{proxy_host}:{proxy_port}",
        "https": f"http://{auth}@{proxy_host}:{proxy_port}",
    }


def init_proxy() -> None:
    global proxies
    if use_proxy and proxy_login and proxy_password:
        proxies = get_proxies_dict(generate_session_id())
    else:
        proxies = {}


def rotate_proxy() -> None:
    global last_rotate_ts, proxies
    if not use_proxy or not proxy_login:
        return
    now = time.time()
    with rotate_lock:
        if now - last_rotate_ts < MIN_ROTATE_SEC:
            return
        try:
            new_session = generate_session_id()
            proxies = get_proxies_dict(new_session)
            print(f"[PROXY] IP changed. Session: {new_session}")
        except Exception as e:
            print(f"[PROXY] Rotation error: {e}")
        finally:
            last_rotate_ts = time.time()
            time.sleep(2)


# ═══════════════════════════════════════════════════════════════════════════════
#  KEY POOL MANAGEMENT (base.txt)
# ═══════════════════════════════════════════════════════════════════════════════

csv_lock = threading.Lock()
reserved_keys: set = set()
base_txt_path: str = "base.txt"


def _load_rows() -> list[dict]:
    rows: list[dict] = []
    if not os.path.exists(base_txt_path):
        return rows
    with open(base_txt_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(":")
            if len(parts) < 2:
                continue
            rows.append({
                "API": parts[0].strip(),
                "Refresh": parts[1].strip(),
                "Date": parts[2].strip() if len(parts) > 2 else "",
            })
    return rows


def _save_rows(rows: list[dict]) -> None:
    tmp = base_txt_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for row in rows:
            if row["Date"]:
                f.write(f"{row['API']}:{row['Refresh']}:{row['Date']}\n")
            else:
                f.write(f"{row['API']}:{row['Refresh']}\n")
    shutil.move(tmp, base_txt_path)


def _parse_date(date_str: str) -> datetime:
    if not date_str:
        return datetime(1970, 1, 1)
    try:
        return datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        return datetime(1970, 1, 1)


def get_free_user_credentials() -> dict | None:
    """Pick the oldest available key (unused for 31+ days)."""
    with csv_lock:
        rows = _load_rows()
        limit = datetime.now() - timedelta(days=31)
        candidates = [
            (row, _parse_date(row["Date"]))
            for row in rows
            if row["API"] not in reserved_keys
            and _parse_date(row["Date"]) <= limit
        ]
        if not candidates:
            return None
        row, _ = min(candidates, key=lambda x: x[1])
        reserved_keys.add(row["API"])
        return row


def mark_api_key_exhausted(api_key: str) -> None:
    with csv_lock:
        rows = _load_rows()
        for row in rows:
            if row["API"] == api_key:
                row["Date"] = datetime.now().strftime("%d.%m.%Y")
                break
        _save_rows(rows)
    reserved_keys.discard(api_key)


# ═══════════════════════════════════════════════════════════════════════════════
#  FIREBASE AUTH (refresh → access token)
# ═══════════════════════════════════════════════════════════════════════════════

def get_access_token(refresh_token: str, max_retries: int = 3) -> str | None:
    headers = COMMON_HEADERS.copy()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    for attempt in range(max_retries):
        try:
            resp = requests.post(
                REFRESH_URL, data=data, headers=headers,
                proxies=proxies, timeout=REQUEST_TIMEOUT,
            )
            if resp.status_code == 200:
                js = resp.json()
                return js.get("id_token") or js.get("access_token")
            elif resp.status_code == 400:
                print(f"[AUTH] Invalid refresh token: {resp.text[:120]}")
                return None
            else:
                print(f"[AUTH] Token error: {resp.status_code} {resp.text[:120]}")
                return None
        except Exception as e:
            print(f"[AUTH] Network error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                rotate_proxy()
                time.sleep(NETWORK_RETRY_DELAY)
    return None


# ═══════════════════════════════════════════════════════════════════════════════
#  ELEVENLABS HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def cleanup_voices(access_token: str) -> None:
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"
    try:
        r = requests.get(
            "https://api.us.elevenlabs.io/v1/voices",
            headers=headers, proxies=proxies, timeout=REQUEST_TIMEOUT,
        )
        r.raise_for_status()
        for v in r.json().get("voices", []):
            if v.get("category") != "premade":
                delete_voice(access_token, v["voice_id"])
    except requests.RequestException:
        pass


def delete_voice(access_token: str, voice_id: str) -> None:
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"
    try:
        requests.delete(
            f"https://api.us.elevenlabs.io/v1/voices/{voice_id}",
            headers=headers, proxies=proxies, timeout=REQUEST_TIMEOUT,
        ).raise_for_status()
        print(f"[API] Voice {voice_id} deleted.")
    except requests.RequestException:
        pass


# ═══════════════════════════════════════════════════════════════════════════════
#  AUDIO UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

def silence_mp3(path: str, duration: float = SILENCE_SEC,
                sr: int = 44100, bitrate: str = "128k") -> None:
    subprocess.run(
        ["ffmpeg", "-f", "lavfi",
         "-i", f"anullsrc=r={sr}:cl=mono",
         "-t", str(duration), "-c:a", "libmp3lame",
         "-b:a", bitrate, path, "-y"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
    )


def get_audio_params(path: str) -> tuple[str, str, str]:
    try:
        out = subprocess.check_output(
            ["ffprobe", "-v", "error", "-select_streams", "a:0",
             "-show_entries", "stream=sample_rate,channels,bit_rate",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
        ).decode().splitlines()
        vals = (out + ["44100", "1", "128000"])[:3]
        return vals[0], vals[1], vals[2]
    except Exception:
        return "44100", "1", "128000"


def get_audio_duration(file_path: str) -> float | None:
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error",
             "-show_entries", "format=duration",
             "-of", "csv=p=0", file_path],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            return float(result.stdout.strip())
    except (FileNotFoundError, ValueError):
        pass
    return None


# ═══════════════════════════════════════════════════════════════════════════════
#  BACKOFF HELPER
# ═══════════════════════════════════════════════════════════════════════════════

def _needs_backoff(detail: dict, http_status: int) -> bool:
    status = str(detail.get("status", "")).lower()
    msg = str(detail.get("message", "")).lower()
    triggers = ("subscription", "buy", "payment", "vpn", "proxy",
                "detected_unusual_activity", "unusual activity")
    return http_status in (402, 403, 429) or any(t in status + " " + msg for t in triggers)


# ═══════════════════════════════════════════════════════════════════════════════
#  TEXT-TO-SPEECH (Internal API)
# ═══════════════════════════════════════════════════════════════════════════════

def text_to_speech(
    access_token: str, text: str, out_file: str, voice_id: str,
    similarity: float = VOICE_SIMILARITY,
    stability: float = VOICE_STABILITY,
    style_exaggeration: float = VOICE_STYLE_EXAGGERATE,
    speed: float = VOICE_SPEED,
    max_network_retries: int = MAX_NETWORK_RETRIES,
):
    """
    Generate speech. Returns:
      True               — success
      "quota_exceeded"    — quota hit
      "unusual_activity"  — account flagged
      "network_error"     — all retries failed
      "error"             — other error
    """
    url = f"https://api.us.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"
    headers["Content-Type"] = "application/json"

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "similarity_boost": similarity,
            "stability": stability,
            "style_exaggeration": style_exaggeration,
        },
        "generation_config": {"speed": speed},
    }

    network_retries = 0

    while True:
        # ── request ──
        try:
            r = requests.post(
                url, json=payload, headers=headers,
                proxies=proxies, timeout=REQUEST_TIMEOUT, stream=True,
            )
        except requests.exceptions.Timeout:
            network_retries += 1
            print(f"[NET] Timeout (attempt {network_retries}/{max_network_retries})")
            if network_retries >= max_network_retries:
                return "network_error"
            rotate_proxy()
            time.sleep(NETWORK_RETRY_DELAY)
            continue
        except requests.RequestException as e:
            network_retries += 1
            print(f"[NET] Error (attempt {network_retries}/{max_network_retries}): {e}")
            if network_retries >= max_network_retries:
                return "network_error"
            rotate_proxy()
            time.sleep(NETWORK_RETRY_DELAY)
            continue

        # ── success: write stream + append silence ──
        if r.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as t:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        t.write(chunk)
                tmp = t.name

            try:
                sr, ch, br = get_audio_params(tmp)
                bitrate = f"{int(int(br) / 1000)}k"
                cl = "mono" if ch == "1" else "stereo"

                silence = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
                subprocess.run(
                    ["ffmpeg", "-f", "lavfi", "-i", f"anullsrc=r={sr}:cl={cl}",
                     "-t", str(SILENCE_SEC), "-c:a", "libmp3lame", "-b:a", bitrate,
                     silence, "-y"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
                )

                concat_file = tempfile.NamedTemporaryFile(delete=False, mode="w").name
                with open(concat_file, "w") as f:
                    f.write(f"file '{tmp}'\nfile '{silence}'\n")

                subprocess.run(
                    ["ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_file,
                     "-c", "copy", out_file, "-y"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
                )

                os.remove(tmp)
                os.remove(silence)
                os.remove(concat_file)
                return True
            except Exception as e:
                print(f"[ffmpeg] Audio processing error: {e}")
                if os.path.exists(tmp):
                    os.remove(tmp)
                return "error"

        # ── error handling ──
        try:
            detail = r.json().get("detail", {})
        except Exception:
            detail = {}

        if _needs_backoff(detail, r.status_code):
            network_retries += 1
            msg = detail.get("message", "") or f"HTTP {r.status_code}"
            print(f"[API] {r.status_code}: {msg[:120]} (attempt {network_retries}/{max_network_retries})")
            if network_retries >= max_network_retries:
                return "network_error"
            rotate_proxy()
            time.sleep(NETWORK_RETRY_DELAY)
            continue

        if detail.get("status") == "quota_exceeded":
            print("[API] Quota exceeded")
            return "quota_exceeded"

        if detail.get("status") == "detected_unusual_activity":
            print("[API] Unusual activity — account flagged")
            return "unusual_activity"

        print(f"[API] Error {r.status_code}: {detail.get('message', r.text)[:120]}")
        return "error"


# ═══════════════════════════════════════════════════════════════════════════════
#  TEXT CHUNKING
# ═══════════════════════════════════════════════════════════════════════════════

def split_text_into_chunks(text: str, max_chunk_size: int = MAX_CHUNK_SIZE) -> list[str]:
    if not text:
        return [""]
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks: list[str] = []
    current: list[str] = []
    size = 0
    for s in sentences:
        s_size = len(s) + 1
        if size + s_size > max_chunk_size and current:
            chunks.append(" ".join(current))
            current, size = [], 0
        current.append(s)
        size += s_size
    if current:
        chunks.append(" ".join(current))
    return chunks


# ═══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STRUCTURES (shared between workers)
# ═══════════════════════════════════════════════════════════════════════════════

merge_lock = threading.Lock()
completed_chunks: dict[int, int] = defaultdict(int)
processed_chunks: set[tuple[int, int]] = set()
chunk_count_by_row: list[int] = []
chunk_dir: str = ""

# Scene name mapping: row_idx → original filename stem
scene_names: list[str] = []


# ═══════════════════════════════════════════════════════════════════════════════
#  WORKER THREAD
# ═══════════════════════════════════════════════════════════════════════════════

def worker(
    tid: int, q: Queue, chunk_map: list[list[str]], out_dir: str,
    min_bytes: int, retry_cnt: dict[tuple[int, int], int],
    voice_speed: float, voice_id_override: str,
    voice_similarity: float, voice_stability: float, voice_style: float,
):
    user_creds = get_free_user_credentials()
    if not user_creds:
        print(f"[T{tid}] No available accounts — thread done.")
        return

    api_key = user_creds["API"]
    refresh_token = user_creds["Refresh"]

    print(f"[T{tid}] Authenticating key {api_key[:8]}...")
    access_token = get_access_token(refresh_token)

    if not access_token:
        print(f"[T{tid}] Failed to get access token for {api_key[:8]}")
        reserved_keys.discard(api_key)
        return

    lib_id = None
    print(f"[T{tid}] Session started.")

    while True:
        try:
            row_idx, ch_idx = q.get_nowait()
        except Empty:
            break

        scene_name = scene_names[row_idx] if row_idx < len(scene_names) else str(row_idx + 1)
        ch_no = ch_idx + 1
        local_retries = 0

        while True:
            text = chunk_map[row_idx][ch_idx]
            chunk_path = os.path.join(chunk_dir, f"{scene_name}_{ch_no}.mp3")
            final_path = os.path.join(out_dir, f"{scene_name}.mp3")

            # 1. Already exists?
            if os.path.exists(final_path) and os.path.getsize(final_path) >= min_bytes:
                q.task_done()
                break

            if os.path.exists(chunk_path) and os.path.getsize(chunk_path) >= min_bytes:
                with merge_lock:
                    if (row_idx, ch_idx) not in processed_chunks:
                        processed_chunks.add((row_idx, ch_idx))
                        completed_chunks[row_idx] += 1
                q.task_done()
                break

            total_attempts = retry_cnt[(row_idx, ch_idx)] + local_retries + 1
            print(f"[T{tid}] → {scene_name}, chunk {ch_no} — attempt {total_attempts}")

            if total_attempts > MAX_TASK_RETRIES:
                print(f"[T{tid}] ✗ {scene_name}, chunk {ch_no} — max retries ({MAX_TASK_RETRIES}), skipping")
                q.task_done()
                break

            # 2. Empty text → silence
            if not text:
                try:
                    silence_mp3(chunk_path)
                    with merge_lock:
                        processed_chunks.add((row_idx, ch_idx))
                        completed_chunks[row_idx] += 1
                except subprocess.CalledProcessError:
                    local_retries += 1
                    continue
                q.task_done()
                break

            if lib_id is None:
                cleanup_voices(access_token)
                lib_id = voice_id_override or STANDARD_VOICE_ID

            voice_id = lib_id or STANDARD_VOICE_ID

            # 3. TTS call
            result = text_to_speech(
                access_token, text, chunk_path, voice_id,
                similarity=voice_similarity,
                stability=voice_stability,
                style_exaggeration=voice_style,
                speed=voice_speed,
            )

            # 4. Quota exceeded → rotate key
            if result == "quota_exceeded":
                mark_api_key_exhausted(api_key)
                if lib_id:
                    delete_voice(access_token, lib_id)

                user_creds = get_free_user_credentials()
                if not user_creds:
                    retry_cnt[(row_idx, ch_idx)] += local_retries
                    q.put((row_idx, ch_idx))
                    q.task_done()
                    return

                api_key = user_creds["API"]
                refresh_token = user_creds["Refresh"]
                print(f"[T{tid}] Switching to key {api_key[:8]}...")

                access_token = get_access_token(refresh_token)
                if not access_token:
                    retry_cnt[(row_idx, ch_idx)] += local_retries
                    q.put((row_idx, ch_idx))
                    q.task_done()
                    return

                lib_id = None
                continue

            # 5. Unusual activity — account flagged, switch key
            if result == "unusual_activity":
                mark_api_key_exhausted(api_key)
                if lib_id:
                    delete_voice(access_token, lib_id)

                user_creds = get_free_user_credentials()
                if not user_creds:
                    retry_cnt[(row_idx, ch_idx)] += local_retries
                    q.put((row_idx, ch_idx))
                    q.task_done()
                    return

                api_key = user_creds["API"]
                refresh_token = user_creds["Refresh"]
                print(f"[T{tid}] Account flagged, switching to key {api_key[:8]}...")

                access_token = get_access_token(refresh_token)
                if not access_token:
                    retry_cnt[(row_idx, ch_idx)] += local_retries
                    q.put((row_idx, ch_idx))
                    q.task_done()
                    return

                lib_id = None
                continue

            # 6. Network error
            if result == "network_error":
                local_retries += 1
                print(f"[T{tid}] Network error for {scene_name}, chunk {ch_no} — retry #{local_retries}")
                continue

            # 7. Auth error
            if result == "auth_error":
                print(f"[T{tid}] Refreshing token...")
                access_token = get_access_token(refresh_token)
                if not access_token:
                    local_retries += 1
                continue

            # 8. Other error
            if result is not True:
                local_retries += 1
                print(f"[T{tid}] Error for {scene_name}, chunk {ch_no} — retry #{local_retries}")
                continue

            # File too small?
            if not os.path.exists(chunk_path) or os.path.getsize(chunk_path) < min_bytes:
                local_retries += 1
                print(f"[T{tid}] File too small for {scene_name}, chunk {ch_no} — retry #{local_retries}")
                continue

            # 8. Success — merge chunks if all done
            with merge_lock:
                processed_chunks.add((row_idx, ch_idx))
                completed_chunks[row_idx] += 1
                merge_needed = completed_chunks[row_idx] == chunk_count_by_row[row_idx]

            if merge_needed:
                try:
                    concat_file = tempfile.NamedTemporaryFile(delete=False, mode="w").name
                    with open(concat_file, "w") as f:
                        for i in range(chunk_count_by_row[row_idx]):
                            chunk_fn = os.path.join(chunk_dir, f"{scene_name}_{i + 1}.mp3")
                            f.write(f"file '{chunk_fn}'\n")

                    subprocess.run(
                        ["ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_file,
                         "-c", "copy", final_path, "-y"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
                    )

                    os.remove(concat_file)
                    for i in range(chunk_count_by_row[row_idx]):
                        try:
                            os.remove(os.path.join(chunk_dir, f"{scene_name}_{i + 1}.mp3"))
                        except OSError:
                            pass
                    print(f"[T{tid}]   ✓ {scene_name}.mp3 assembled.")
                except Exception as e:
                    print(f"[T{tid}] Merge error for {scene_name}: {e}")

            q.task_done()
            break

    # Thread cleanup
    if lib_id and access_token:
        delete_voice(access_token, lib_id)
    reserved_keys.discard(api_key)
    print(f"[T{tid}] Done.")


# ═══════════════════════════════════════════════════════════════════════════════
#  UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

def collect_missing(out_dir: str, min_bytes: int) -> list[int]:
    missing = []
    for i, name in enumerate(scene_names):
        path = os.path.join(out_dir, f"{name}.mp3")
        if not os.path.exists(path) or os.path.getsize(path) < min_bytes:
            missing.append(i)
    return missing


def run_pass(
    pass_no: int, missing_rows: list[int], chunk_map: list[list[str]],
    out_dir: str, threads: int, min_bytes: int,
    retry_cnt: dict[tuple[int, int], int], voice_speed: float,
    voice_id: str, voice_similarity: float, voice_stability: float,
    voice_style: float,
) -> None:
    print(f"\n── Pass {pass_no}: {len(missing_rows)} scenes to generate ──")
    tasks: Queue = Queue()
    for idx in missing_rows:
        for ch_idx in range(len(chunk_map[idx])):
            tasks.put((idx, ch_idx))

    with ThreadPoolExecutor(max_workers=threads) as pool:
        futures = [
            pool.submit(
                worker, n + 1, tasks, chunk_map, out_dir,
                min_bytes, retry_cnt, voice_speed, voice_id,
                voice_similarity, voice_stability, voice_style,
            )
            for n in range(threads)
        ]
        for f in as_completed(futures):
            f.result()


def concat_audio_files(mp3_files: list[Path], output_path: Path) -> dict:
    """Concatenate MP3 files using ffmpeg concat demuxer."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        for mp3 in mp3_files:
            escaped = str(mp3).replace("'", "'\\''")
            f.write(f"file '{escaped}'\n")
        concat_list = f.name

    try:
        result = subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
             "-i", concat_list, "-c", "copy", str(output_path)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"[ffmpeg] Concat error: {result.stderr[:200]}")
            return {"success": False, "error": result.stderr[:200]}

        duration = get_audio_duration(str(output_path))
        return {
            "success": True,
            "output": str(output_path),
            "duration_seconds": round(duration, 2) if duration else None,
            "source_files": len(mp3_files),
        }
    finally:
        Path(concat_list).unlink(missing_ok=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  SCENE LOADING (txt files → chunk_map)
# ═══════════════════════════════════════════════════════════════════════════════

def load_scenes_from_dir(scene_dir: Path) -> tuple[list[list[str]], list[str]]:
    """Load .txt files from scene directory, return (chunk_map, scene_names)."""
    txt_files = sorted(scene_dir.glob("*.txt"))
    if not txt_files:
        print(f"Error: No .txt files in {scene_dir}", file=sys.stderr)
        sys.exit(1)

    names: list[str] = []
    chunks: list[list[str]] = []

    for txt_file in txt_files:
        text = txt_file.read_text(encoding="utf-8").strip()
        names.append(txt_file.stem)
        chunks.append(split_text_into_chunks(text))

    return chunks, names


def load_single_script(script_path: str) -> tuple[list[list[str]], list[str]]:
    """Load a single script file, return (chunk_map, names)."""
    with open(script_path, encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print("Error: Empty script", file=sys.stderr)
        sys.exit(1)

    stem = Path(script_path).stem
    return [split_text_into_chunks(text)], [stem]


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    global chunk_dir, chunk_count_by_row, scene_names, use_proxy, base_txt_path

    args = parse_args()

    # Validate args
    if args.scene_dir and args.script:
        print("Error: Cannot use both --scene-dir and --script", file=sys.stderr)
        sys.exit(1)
    if not args.scene_dir and not args.script:
        print("Error: Provide --scene-dir or --script", file=sys.stderr)
        sys.exit(1)
    if args.script and not args.output:
        print("Error: --output required for single-file mode", file=sys.stderr)
        sys.exit(1)
    if args.concat and not args.scene_dir:
        print("Error: --concat requires --scene-dir", file=sys.stderr)
        sys.exit(1)

    # Config
    base_txt_path = args.base
    if not os.path.exists(base_txt_path):
        print(f"Error: base.txt not found at {base_txt_path}", file=sys.stderr)
        sys.exit(1)

    use_proxy = not args.no_proxy
    init_proxy()

    threads = max(1, args.threads)
    min_bytes = max(1, args.min_bytes)
    voice_id = args.voice_id or os.getenv("ELEVENLABS_VOICE_ID") or STANDARD_VOICE_ID

    # Load scenes
    if args.scene_dir:
        scene_path = Path(args.scene_dir)
        if not scene_path.is_dir():
            print(f"Error: Directory not found: {scene_path}", file=sys.stderr)
            sys.exit(1)
        chunk_map, scene_names = load_scenes_from_dir(scene_path)
        out_dir = str(scene_path.resolve())
    else:
        chunk_map, scene_names = load_single_script(args.script)
        out_dir = str(Path(args.output).parent.resolve())
        Path(out_dir).mkdir(parents=True, exist_ok=True)

    chunk_count_by_row = [len(c) for c in chunk_map]
    chunk_dir = os.path.join(out_dir, "_chunks")
    os.makedirs(chunk_dir, exist_ok=True)

    total_scenes = len(chunk_map)
    total_chunks = sum(chunk_count_by_row)
    total_chars = sum(len(t) for chunks in chunk_map for t in chunks)

    # Print info
    if not args.json:
        print(f"=== VoicePro Parallel TTS ===")
        print(f"Scenes: {total_scenes}, Chunks: {total_chunks}, Chars: {total_chars}")
        print(f"Threads: {threads}, Speed: {args.speed}")
        print(f"Voice: {voice_id}")
        print(f"Retry: {MAX_TASK_RETRIES} task / {MAX_NETWORK_RETRIES} network")
        if use_proxy and proxy_login:
            print(f"Proxy: {proxy_host}:{proxy_port}")
        else:
            print("Proxy: disabled")
        keys = _load_rows()
        limit = datetime.now() - timedelta(days=31)
        avail = sum(1 for r in keys if _parse_date(r["Date"]) <= limit)
        print(f"Keys: {avail}/{len(keys)} available in {base_txt_path}")

    # Dry run
    if args.dry_run:
        result = {
            "dry_run": True,
            "mode": "per_scene" if args.scene_dir else "single",
            "scenes": total_scenes,
            "chunks": total_chunks,
            "total_chars": total_chars,
            "voice_id": voice_id,
            "threads": threads,
            "scene_names": scene_names,
        }
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print("\nWould generate:")
            for i, name in enumerate(scene_names):
                n_chunks = chunk_count_by_row[i]
                chars = sum(len(t) for t in chunk_map[i])
                print(f"  {name}.mp3 ({n_chunks} chunks, {chars} chars)")
        return

    # ── Main generation loop ──
    retry_cnt: dict[tuple[int, int], int] = defaultdict(int)
    pass_no = 1

    while True:
        # Reset global state between passes
        processed_chunks.clear()
        completed_chunks.clear()

        missing = collect_missing(out_dir, min_bytes)
        if not missing:
            if not args.json:
                print(f"\n=== All {total_scenes} scenes generated. ===")
            break

        if pass_no > 5:
            if not args.json:
                print(f"\n=== Max passes reached. {len(missing)} scenes still missing. ===")
            break

        run_pass(
            pass_no, missing, chunk_map, out_dir, threads,
            min_bytes, retry_cnt, args.speed, voice_id,
            args.similarity, args.stability, args.style,
        )
        pass_no += 1

    # ── Collect results ──
    results = []
    total_duration = 0.0
    for name in scene_names:
        mp3_path = os.path.join(out_dir, f"{name}.mp3")
        if os.path.exists(mp3_path):
            duration = get_audio_duration(mp3_path)
            r = {
                "success": True,
                "scene": name,
                "output": mp3_path,
                "size_bytes": os.path.getsize(mp3_path),
            }
            if duration:
                r["duration_seconds"] = round(duration, 2)
                r["duration_frames_30fps"] = int(duration * 30)
                total_duration += duration
            results.append(r)
        else:
            results.append({"success": False, "scene": name, "output": mp3_path})

    # ── Concat if requested ──
    concat_result = None
    if args.concat:
        mp3_files = [Path(r["output"]) for r in results if r.get("success")]
        if not args.json:
            print(f"\nConcatenating {len(mp3_files)} files...")
        concat_result = concat_audio_files(mp3_files, Path(args.concat))
        if not args.json and concat_result.get("success"):
            print(f"  ✅ {args.concat} ({concat_result.get('duration_seconds')}s)")

    # ── Output ──
    final = {
        "success": all(r.get("success") for r in results),
        "mode": "per_scene" if args.scene_dir else "single",
        "voice_id": voice_id,
        "total_scenes": total_scenes,
        "total_duration_seconds": round(total_duration, 2),
        "total_duration_frames_30fps": int(total_duration * 30),
        "scenes": results,
    }
    if concat_result:
        final["concat"] = concat_result

    if args.json:
        print(json.dumps(final, indent=2))
    else:
        print(f"\nResults:")
        for r in results:
            status = "✅" if r.get("success") else "❌"
            dur = f" ({r.get('duration_seconds', '?')}s)" if r.get("success") else ""
            print(f"  {status} {r['scene']}.mp3{dur}")
        print(f"\nTotal: {total_duration:.1f}s ({int(total_duration * 30)} frames @ 30fps)")

    # Cleanup _chunks dir if empty
    try:
        if os.path.isdir(chunk_dir) and not os.listdir(chunk_dir):
            os.rmdir(chunk_dir)
    except OSError:
        pass


if __name__ == "__main__":
    main()
