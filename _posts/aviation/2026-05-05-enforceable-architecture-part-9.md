---
title: "Enforceable Architecture Part 9: Versioning Policies as Your Architecture Evolves"
date: 2026-05-05
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "Architecture is not fixed forever. Part 9 shows how to change a rule safely, without breaking everything that depended on the old one."
header:
  teaser: /assets/images/aviation/T9.png
toc: false
---

{% include blog-sidebar.html %}

Every rule we have discussed in this series feels permanent while it is active. But architecture changes. A rule that made sense two years ago can become outdated as an airline adopts new technology, restructures teams, or changes strategy. Today we look at how to change a policy safely, without it silently blocking good new work, or silently allowing something it should still forbid.

## The Danger of Changing a Rule Carelessly

Imagine the API versioning policy from Part 4 needs to change: previously, services declared versions as plain numbers, like `v1`, `v2`. Now the company adopts a new standard using dates, like `2026-01-15`. If you simply edit the existing policy in place, every service still using the old numbered format suddenly fails its check, all at once, across the entire company. Dozens of unrelated pull requests break overnight, for a reason that has nothing to do with the actual change being proposed in each one. Teams lose trust in the system, exactly the outcome we tried to avoid in Part 6.

## Versioning Policies Like You Version APIs

The solution is familiar to any Solution Architect: version the policy itself, the same way you would version an API. An old policy version keeps applying to existing services until they are ready to migrate. A new policy version applies to new services from the start, and existing services adopt it on their own schedule, with a clear deadline.

### Example 1: Migrating the API Versioning Format

The new date-based versioning policy is introduced as `api-versioning-policy v2`, while the old numbered format remains valid under `api-versioning-policy v1`, for now. New services, and any service undergoing significant rework, must use v2. Existing services keep passing under v1, but the policy engine adds a visible, non-blocking warning: "This service uses api-versioning-policy v1, which will be retired on 2026-09-01. Please migrate to v2 before this date." Six months later, when v1 is formally retired, every remaining service using it fails its check, but by then, every team has had fair warning and time to plan the change.

### Example 2: Tightening a Data Residency Rule

Consider a case where a rule needs to become stricter, not looser. Suppose the EU data residency policy from Part 4 originally allowed passenger data to be processed anywhere in the EU. A new regulation requires data to stay specifically within one member state for certain passenger categories. Instead of instantly blocking every existing service, a new policy version, `eu-data-residency v2`, is introduced with a defined rollout: it applies immediately to any new service, and existing services receive a ninety-day grace period, tracked automatically, with the review board from Part 6 handling any service that genuinely cannot meet the new deadline in time.

## Retiring Old Policies Cleanly

A policy version should always have a clear owner and a clear retirement date once a replacement exists. Leaving old policy versions active forever, "just in case," slowly turns your policy engine into the same kind of forgotten wiki diagram we described back in Part 1 — except now there are two versions, and nobody is sure which one is actually being followed where.

## Why This Matters for Long-Term Trust

A system that changes rules carefully, with warnings and migration windows, earns trust from engineering teams. A system that changes rules abruptly teaches teams to fear policy updates, which slows down architecture improvement exactly when it is needed most — as the organization adopts new patterns, new regulations, and new ways of working with AI agents.

## Coming Next

In the final part of this series, Part 10, we bring every piece together — ADR-as-spec, fitness functions, policy-as-code, exceptions, CI/CD gates, and policy versioning — into one complete, enforceable architecture pipeline.
