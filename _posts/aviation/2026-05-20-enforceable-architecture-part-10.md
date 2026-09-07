---
title: "Enforceable Architecture Part 10: Putting It All Together — A Complete Pipeline"
date: 2026-05-20
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "The final part of the series: how ADR-as-spec, fitness functions, policy-as-code, and review boards fit together into one working system."
header:
  teaser: /assets/images/aviation/T10.png
toc: false
---

{% include blog-sidebar.html %}

This is the final part of our ten-part series on enforceable architecture. We started with a simple, painful observation: an architecture rule that lives only in a wiki diagram is operationally dead, especially once AI agents are writing a large share of your code. Today, we connect every piece into one complete picture, using our airline as the example throughout.

## The Full Journey, in One Story

Picture a Solution Architect at an airline, deciding that a new Disruption Management Service — which rebooks passengers automatically during flight cancellations — must never write directly to the Crew Rostering database, for the same legal rest-time reasons we saw back in Part 1.

**Step 1 — ADR-as-spec (Part 2):** The architect writes this decision as an ADR, including a structured rule block: `disruption-management forbids: direct-write to crew-schedule-db; must use crew-rostering-api`. The human-readable explanation and the machine-checkable rule live in the same document.

**Step 2 — Fitness function (Part 3):** A small automated check reads this rule and scans the Disruption Management codebase for any forbidden database connection. This check takes seconds to run.

**Step 3 — Policy-as-code (Part 4):** Because "never bypass the domain-owning service's API" is actually a company-wide pattern, not just a one-off rule, it becomes part of a shared policy applied across every domain, not hand-copied into dozens of separate scripts.

**Step 4 — Spec-Driven Development (Part 5):** When a team asks an AI agent to build the Disruption Management Service's rebooking logic, the task specification includes this constraint explicitly, so the agent has the rule from the very first line of code it writes, not as an afterthought.

**Step 5 — CI/CD gates (Part 7):** The fitness function runs automatically as a required pull request check. Nothing merges until it passes, whether the code was written by a person or an agent.

**Step 6 — The case study pattern (Part 8):** Months later, a well-meaning engineer, chasing a performance issue, tries a direct database shortcut. The gate catches it in minutes, with a clear error message pointing back to the original ADR.

**Step 7 — Exception handling (Part 6):** During a major storm causing hundreds of cancellations, an urgent, time-boxed exception is needed to handle extreme load. The review board approves it quickly, because the request is specific and time-limited, not a permanent bypass.

**Step 8 — Policy versioning (Part 9):** A year later, the Crew Rostering API itself is redesigned. The policy is versioned, existing services get a migration window, and nothing breaks overnight.

## The Real Shift This Series Describes

None of these eight steps is complicated on its own. The real change is treating architecture as something continuously enforced, not something documented once and hoped for. This matters for any organization, but it matters urgently for one adopting AI coding agents at scale, because agents move fast, generate large volumes of code, and — unlike a cautious human — will not stop to ask "is this actually allowed?" unless the answer is built directly into the system they operate in.

## A Final Word

As a Solution Architect who has worked inside a large airline group's Enterprise Architecture function, I have seen firsthand how easily good architectural intent gets lost between the diagram and the deployed system. The tools and practices in this series — ADR-as-spec, fitness functions, policy-as-code, exception-driven review, CI/CD gates, and policy versioning — are not exotic. They are a practical, buildable answer to a very old problem, made urgent again by a very new one: agents that read your code, but never your wiki.

Thank you for following this series from Part 1 to the end. I hope it gives you a concrete starting point for making your own architecture enforceable, not just documented.
