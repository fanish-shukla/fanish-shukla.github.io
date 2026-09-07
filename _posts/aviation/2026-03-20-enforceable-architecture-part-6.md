---
title: "Enforceable Architecture Part 6: Building an Exception-Driven Review Board"
date: 2026-03-20
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "Not every rule should be absolute. Part 6 shows how to build a fast, lightweight process for handling real exceptions."
toc: false
---

{% include blog-sidebar.html %}

So far in this series, we made architecture rules strict: fitness functions block a build, policies block a deployment. This is good most of the time. But sometimes a rule genuinely needs to be broken, for a good reason. A rigid system that never allows exceptions eventually gets a reputation for being an obstacle, and teams start looking for ways around it instead of through it. Today we look at how to handle exceptions properly, without losing the benefits of enforcement.

## Why "No Exceptions Ever" Does Not Work

Imagine a rule says every internal API call must declare an explicit version number, from Part 4. Now imagine a genuine emergency: a critical security patch must go out within the hour, and the only fast fix touches a service that still calls another service using "latest," for legacy reasons nobody has had time to clean up yet. If the policy blocks this deployment with no way through, the team either misses the security fix, or — more likely — someone quietly disables the policy check entirely, which is worse than having no policy at all.

The answer is not to remove enforcement. The answer is a clear, fast process for requesting a temporary, tracked exception.

## What an Exception-Driven Review Board Looks Like

Instead of a slow, monthly architecture review meeting, an exception-driven review board only meets, or responds, when someone actually requests an exception. The request itself is small and structured: which rule, which system, why, and for how long. Most exceptions should be reviewed within hours, not weeks — because the whole point is that most of the time, the automated checks from Parts 3 and 4 already handle everything without any human involvement at all.

### Example 1: The Emergency Security Patch

Going back to our API versioning example: a developer, supported by an AI agent, submits an exception request: "Rule `explicit-api-version-required` — requesting temporary exception for Auth Service, to ship a critical security patch within one hour. Will be fixed properly within five business days." A small review board — perhaps two senior architects — approves this within thirty minutes, because the request is specific, time-boxed, and low-risk given the emergency. The policy engine records this exception, allowing the deployment, but automatically flags the service again after five days if the version call has not been fixed.

### Example 2: A Temporary Data Residency Exception

Consider the EU data residency policy from Part 4. Suppose an airline is migrating its loyalty program to a new cloud region, and for a two-week migration window, some passenger data will briefly pass through a non-EU staging environment for testing, with encryption and no real passenger data used. A request goes to the review board: "Rule `eu-data-residency` — requesting exception for loyalty-service staging environment, two weeks, test data only, encrypted." The board approves quickly, because the risk is clearly limited and the exception has a firm end date, after which the policy automatically re-applies with no exception.

## Why This Keeps Trust in the System

An exception-driven review board works because it treats exceptions as normal, tracked, and time-limited — not as failures of the system. Teams trust the fitness functions and policies more, not less, when they know a fast, fair path exists for the rare cases where a rule genuinely should not apply yet. Without this, enforcement eventually gets quietly bypassed, and you are back to the original problem from Part 1: rules that exist on paper but do nothing in practice.

## Coming Next

In Part 7, we look at where all of this actually runs: building these checks directly into your **CI/CD pipeline**, so architecture compliance is checked automatically on every single change.
