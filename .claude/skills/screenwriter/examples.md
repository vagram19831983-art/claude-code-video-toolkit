# Screenwriter Skill - Examples

Real-world examples of using the screenwriter skill to create compelling video scripts.

---

## Example 1: Product Demo Script

### Context
- **Product:** Deployment automation tool
- **Audience:** Developers
- **Duration:** 90 seconds
- **Goal:** Drive free trial signups

### Raw Input
```
Features:
- Deploy in 60 seconds
- Zero-downtime deploys
- Rollback with one click
- Works with 12 cloud providers

Metrics:
- 50,000 deployments per day
- 99.99% uptime
- Average deploy: 47 seconds
```

### Output Script

**Scene 01: Hook (5 seconds)**
```
Still waiting 30 minutes for deployments to finish?
```
*Word count: 8 | Estimated: 3 seconds*

**Scene 02: Problem (15 seconds)**
```
Every deploy means context switching. Waiting. Wondering if something broke.

Your team deserves better.
```
*Word count: 17 | Estimated: 7 seconds*

**Scene 03: Solution (12 seconds)**
```
Meet TurboDeploy - get your code live in under 60 seconds. [pause 0.5s]

Zero downtime. Zero stress.
```
*Word count: 18 | Estimated: 11 seconds*

**Scene 04: Demo (40 seconds)**
```
Watch this. [pause 1.0s]

I push to main. TurboDeploy detects the change and starts building. [pause 0.5s]

Forty-two seconds later, it's live across 12 regions. [pause 1.0s]

And if something goes wrong? One click to roll back. [pause 0.5s]

Right back to the last working version.
```
*Word count: 50 | Estimated: 38 seconds*

**Scene 05: Stats (18 seconds)**
```
Teams using TurboDeploy ship 50,000 times per day. [pause 0.5s]

Average deploy time? Forty-seven seconds. [pause 0.5s]

With 99.99% uptime.
```
*Word count: 22 | Estimated: 17 seconds*

**Scene 06: CTA (10 seconds)**
```
Start your free trial today. No credit card needed. [pause 0.5s]

Link below.
```
*Word count: 14 | Estimated: 8 seconds*

**Total:** 129 words | ~84 seconds (target: 90s) ✅

---

## Example 2: Sprint Review Script

### Context
- **Project:** Mobile app sprint
- **Audience:** Internal team
- **Duration:** 120 seconds
- **Goal:** Share progress and celebrate wins

### Raw Input
```
Sprint 47: Mobile Performance
Completed:
- Reduced app launch time from 4.2s to 1.8s
- Implemented image caching (saves 2MB per session)
- Fixed 8 crash bugs
- Added dark mode toggle

Next sprint:
- Offline mode
- Push notifications
```

### Output Script

**Scene 01: Title (3 seconds)**
```
[Visual only - "Sprint 47: Mobile Performance"]
```
*No narration*

**Scene 02: Overview (12 seconds)**
```
Sprint 47 had one goal: make the app feel instant. [pause 0.5s]

Did we hit it? Let's find out.
```
*Word count: 19 | Estimated: 11 seconds*

**Scene 03: Shipped Features (25 seconds)**
```
We shipped four major improvements. [pause 0.5s]

App launch now takes under two seconds. Image caching saves bandwidth. Dark mode is finally here. [pause 0.5s]

And we squashed eight crash bugs along the way.
```
*Word count: 38 | Estimated: 24 seconds*

**Scene 04: Demo (45 seconds)**
```
Here's the before and after. [pause 1.0s]

Old version: tap the icon, wait... wait... four seconds. [pause 1.0s]

New version: tap and you're in. One point eight seconds. [pause 1.0s]

That's a fifty-seven percent improvement. Users won't even notice the loading screen anymore.
```
*Word count: 50 | Estimated: 43 seconds*

**Scene 05: Metrics (20 seconds)**
```
The numbers back it up. [pause 0.5s]

Launch time dropped from 4.2 seconds to 1.8. [pause 0.5s]

Image caching cuts data usage by 2 megabytes per session. [pause 0.5s]

And crash rate? Down to 0.3 percent.
```
*Word count: 38 | Estimated: 21 seconds*

**Scene 06: Next Sprint (15 seconds)**
```
Sprint 48 starts Monday. [pause 0.5s]

We're tackling offline mode and push notifications. [pause 0.5s]

See you in two weeks.
```
*Word count: 20 | Estimated: 13 seconds*

**Total:** 165 words | ~112 seconds (target: 120s) ✅

---

## Example 3: Tutorial Script

### Context
- **Topic:** Setting up authentication
- **Audience:** Developers (intermediate)
- **Duration:** 180 seconds
- **Goal:** Teach implementation step-by-step

### Raw Input
```
Tutorial: Add Auth to Your App
Steps:
1. Install package
2. Configure environment variables
3. Wrap app with provider
4. Add login button
5. Protect routes

Common mistake: Forgetting to add REDIRECT_URI
```

### Output Script

**Scene 01: Hook (5 seconds)**
```
Add authentication to your app in 10 minutes. Let's go.
```
*Word count: 11 | Estimated: 5 seconds*

**Scene 02: Prerequisites (8 seconds)**
```
You'll need Node.js and a free account. Links in the description.
```
*Word count: 13 | Estimated: 7 seconds*

**Scene 03: Step 1 - Install (20 seconds)**
```
First, install the package. [pause 0.5s]

npm install auth-kit. [pause 1.0s]

While that runs, grab your API key from the dashboard. [pause 0.5s]

Copy it - we'll need it in a second.
```
*Word count: 32 | Estimated: 22 seconds*

**Scene 04: Step 2 - Environment Variables (25 seconds)**
```
Create a .env file in your project root. [pause 1.0s]

Add three variables: API_KEY, CLIENT_ID, and REDIRECT_URI. [pause 0.5s]

That last one trips people up. [pause 0.5s]

It's the URL where users land after logging in. Usually localhost:3000/callback during development.
```
*Word count: 50 | Estimated: 28 seconds*

**Scene 05: Step 3 - Provider Wrapper (30 seconds)**
```
Now wrap your app with the AuthProvider. [pause 1.0s]

Import it at the top. [pause 0.5s]

Then wrap your App component. Pass in your config. [pause 1.0s]

This gives every component access to authentication state. [pause 0.5s]

Who's logged in, their profile, logout methods - all available.
```
*Word count: 55 | Estimated: 32 seconds*

**Scene 06: Step 4 - Login Button (35 seconds)**
```
Let's add a login button. [pause 1.0s]

Import the useAuth hook. Call it to get the login function. [pause 1.0s]

Wire it up to a button. [pause 0.5s]

onClick equals login. [pause 1.0s]

Now when I click it... [pause 0.5s]

Redirects to the login page. I sign in. [pause 1.0s]

And I'm back in the app, authenticated.
```
*Word count: 67 | Estimated: 37 seconds*

**Scene 07: Step 5 - Protect Routes (25 seconds)**
```
Last step: protect routes that need authentication. [pause 1.0s]

Import ProtectedRoute. [pause 0.5s]

Wrap any route that requires login. [pause 1.0s]

Now if someone tries to access this page without logging in, they're redirected to the login screen automatically.
```
*Word count: 45 | Estimated: 27 seconds*

**Scene 08: Result (15 seconds)**
```
And that's it. [pause 0.5s]

Full authentication in under 50 lines of code. [pause 1.0s]

Next video: adding profile pages and user management.
```
*Word count: 25 | Estimated: 16 seconds*

**Total:** 298 words | ~174 seconds (target: 180s) ✅

---

## Example 4: Before/After Comparison

### Original Script (Generic, Too Long)

**Scene: Feature Introduction (30 seconds target)**
```
Our platform offers a comprehensive suite of innovative tools designed to optimize and streamline your development workflow, enabling you to achieve greater productivity and efficiency through the utilization of cutting-edge technology and best-in-class methodologies that have been proven to deliver exceptional results for organizations of all sizes.
```

**Issues:**
- 49 words for 30 seconds = too dense (need ~75 words/min pace)
- Passive voice ("have been proven")
- Vague claims ("innovative," "cutting-edge")
- No specific benefits
- Corporate jargon ("comprehensive suite," "utilization")

### Improved Script (Specific, Right Length)

**Scene: Feature Introduction (30 seconds)**
```
Three tools that'll change how you ship code. [pause 0.5s]

First: one-click deploys. Your code goes live in under 60 seconds. [pause 0.5s]

Second: automatic rollbacks. If something breaks, we revert instantly. [pause 0.5s]

Third: preview environments. Test every branch before merging. [pause 1.0s]

That's it. Deploy faster, break less, ship with confidence.
```

**Improvements:**
- 54 words + 2.5s pauses = 29 seconds ✅
- Active voice ("we revert," "test")
- Specific numbers ("60 seconds," "three tools")
- Clear benefits ("deploy faster, break less")
- Conversational tone

---

## Example 5: Adjusting Tone by Audience

### Same Content, Three Audiences

**Raw Input:**
```
Feature: API rate limiting now configurable per endpoint
Benefit: Prevent abuse without blocking legitimate users
Details: Set limits from 10 to 10,000 requests/hour
```

### Version A: Technical Audience (Developers)

```
We've added per-endpoint rate limiting. [pause 0.5s]

Configure limits from 10 to 10,000 requests per hour. [pause 0.5s]

Different endpoints get different thresholds. Your authentication endpoint might allow 100 requests per hour, while your search API handles 5,000. [pause 0.5s]

Granular control without the blanket restrictions.
```

**Tone:** Technical, assumes knowledge, uses proper terminology

### Version B: Business Audience (Managers)

```
You can now prevent API abuse without blocking your customers. [pause 0.5s]

Set request limits for each API endpoint based on what makes sense. [pause 0.5s]

High-traffic features get higher limits. Sensitive operations get tighter controls. [pause 0.5s]

Protect your infrastructure while keeping the user experience smooth.
```

**Tone:** Business-focused, emphasizes outcomes over implementation

### Version C: General Audience (Marketing)

```
Your API just got smarter. [pause 0.5s]

Now you can stop bad actors without slowing down real users. [pause 0.5s]

Set custom limits for every part of your API. [pause 0.5s]

The right protection, exactly where you need it.
```

**Tone:** Simple, benefit-forward, avoids jargon

---

## Example 6: Adding Emotional Arc

### Flat Script (No Arc)

```
We released three features. Image compression, lazy loading, and caching. These make the app faster. Users will notice the difference.
```

**Issue:** Informative but no emotional journey. Reads like release notes.

### With Emotional Arc

**Setup (Frustration):**
```
Slow apps lose users. Every extra second of load time costs you customers.
```

**Rising Action (Hope):**
```
So we made ours faster. [pause 0.5s] A lot faster.
```

**Climax (Excitement):**
```
Image compression cuts file sizes by 60%. Lazy loading defers off-screen content. And caching? [pause 0.5s] Your users might never see a loading spinner again.
```

**Resolution (Satisfaction):**
```
Fast apps win. [pause 0.5s] Yours just became one of them.
```

**Emotional Path:** Frustration → Hope → Excitement → Satisfaction

---

## Example 7: CTA Variations

### Weak CTAs (Generic)
```
❌ "Learn more"
❌ "Click here"
❌ "Get started"
❌ "Contact us"
❌ "Try it out"
```

### Strong CTAs (Specific + Benefit + Friction Reducer)

**For Free Trial:**
```
✅ "Start your free trial - no credit card needed"
✅ "Test it free for 30 days - cancel anytime"
✅ "Try all features free - setup takes 2 minutes"
```

**For Content Download:**
```
✅ "Download the migration guide - it's free"
✅ "Get the complete checklist - no signup required"
✅ "Grab the template - starts downloading immediately"
```

**For Demo/Call:**
```
✅ "Book a 15-minute demo - pick your time"
✅ "Talk to an engineer - available today"
✅ "See it in action - watch the 5-minute walkthrough"
```

**For Documentation:**
```
✅ "Read the full docs - examples included"
✅ "Follow the step-by-step guide - with screenshots"
✅ "Check the API reference - copy-paste ready code"
```

---

## Example 8: Pause Usage

### Without Strategic Pauses

```
We just shipped the biggest release in company history. Twelve features. Zero bugs. Two weeks of work. This changes everything.
```

**Issues:** Rushes through impressive claims, no time to absorb

### With Strategic Pauses

```
We just shipped the biggest release in company history. [pause 1.0s]

Twelve features. [pause 0.5s] Zero bugs. [pause 0.5s] Two weeks of work. [pause 1.5s]

This changes everything.
```

**Impact:**
- 1.0s after "biggest release" = let that sink in
- 0.5s between stats = rhythm, emphasis
- 1.5s before "this changes everything" = dramatic reveal
- Final statement lands with weight

---

## Key Takeaways from Examples

1. **Specificity wins** - "60 seconds" beats "fast"
2. **Front-load value** - Hook in first 5 seconds or lose viewers
3. **Benefits > Features** - "Deploy faster" > "Has deployment tool"
4. **Tone matches audience** - Technical for devs, business for managers
5. **Pauses create impact** - Strategic silence emphasizes key points
6. **Emotional arc engages** - Frustration → Hope → Satisfaction
7. **Strong CTAs convert** - Specific action + benefit + friction reducer
8. **One idea per sentence** - Complex thoughts split into digestible pieces

---

## Anti-Patterns to Avoid

### ❌ Jargon Overload
```
"Leverage our synergistic platform to optimize your value streams and actualize transformational outcomes."
```
**Problem:** Nobody talks like this. Sounds like a parody.

### ❌ Feature Dumping
```
"We have SSO, RBAC, 2FA, SAML, OAuth, LDAP, AD integration, audit logs, compliance reports, and encryption."
```
**Problem:** Laundry list. Not memorable. No context for why each matters.

### ❌ Passive Voice
```
"Your data is encrypted by our system using industry-standard protocols."
```
**Problem:** Distant, corporate. Who's doing what?

**Better:** "We encrypt your data end-to-end."

### ❌ Hedge Words
```
"This might help you become somewhat more productive, potentially saving you almost an hour per week."
```
**Problem:** Sounds uncertain. Undermines credibility.

**Better:** "Save an hour every week."

### ❌ No Pauses (Wall of Text)
```
"Our platform enables teams to collaborate more effectively by providing real-time updates shared dashboards integrated workflows and seamless communication tools that work across all devices and time zones so everyone stays aligned no matter where they're working from."
```
**Problem:** Run-on sentence. Narrator will sound frantic. Viewers tune out.

---

## Using These Examples

When writing your own scripts:

1. **Find similar example** - Match your video type (demo, review, tutorial)
2. **Note the structure** - See how scenes flow and connect
3. **Check timing** - Compare word counts to durations
4. **Adapt tone** - Adjust formality based on your audience
5. **Apply principles** - Specificity, benefits, active voice, pauses

Remember: These are templates, not rigid formulas. Adapt to your brand voice and content needs.
