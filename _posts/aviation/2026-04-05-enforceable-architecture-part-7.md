---
title: "Enforceable Architecture Part 7: CI/CD Gates for Architectural Compliance"
date: 2026-04-05
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "Fitness functions and policies only matter if they actually run. Part 7 shows where to place them in the pipeline."
toc: false
---

{% include blog-sidebar.html %}

We have talked about ADR-as-spec, fitness functions, policy-as-code, and exception handling. All of these ideas share one requirement: they must actually run, automatically, at the right moment. Today we look at exactly where these checks belong in a CI/CD pipeline, and why the placement matters as much as the check itself.

## Three Places to Put a Check, and Why They Are Different

A check can run in three different places: on a developer's own computer, on a pull request before merging, or on a deployment before it reaches production. Each place has a different job.

Local checks, run before a developer even commits code, catch problems fast, but they can be skipped — someone can commit anyway, ignoring a warning. Pull request checks, run automatically when code is proposed for merging, are much harder to skip, because they block the merge button itself. Deployment checks, run right before code reaches a live environment, are the last line of defense, catching anything that somehow passed earlier stages, including configuration that only becomes visible at deployment time.

### Example 1: Catching a Rule Break Before Merge, Not After

Consider the rule from Part 2: Booking Service must never call Payment Service directly. If this fitness function only runs as a local check, a developer — or an AI agent working automatically without a human at the keyboard — might commit code anyway, since nothing blocks it. If the same fitness function is placed as a required check on every pull request, the merge button itself stays locked until the check passes. This is important, because in the agent era, many changes happen without a human manually running local tests every time. The pull request stage becomes the real safety net.

### Example 2: Catching a Regional Config Problem at Deployment

Now consider the EU data residency policy from Part 4. This rule cannot always be checked from source code alone — sometimes the actual problem only appears in the deployment configuration, for example, a Kubernetes manifest pointing to the wrong cloud region. Even if the pull request check passes, because the code itself looks fine, a deployment gate re-checks the actual target region right before the loyalty service goes live. If a config file was changed after the pull request was approved — which does happen — the deployment gate catches it, stopping passenger data from ever reaching the wrong region, even for a few minutes.

## Making Checks Fast Enough That Nobody Wants to Skip Them

A common mistake is adding so many slow checks that developers start requesting exceptions just to save time, which undermines the whole system from Part 6. Good fitness functions and policy checks should run in seconds, not minutes, for most rules. Slower checks — like the flight data freshness test from Part 3, which needs a running test environment — should run in parallel with faster checks, not one after another, so the total wait time stays reasonable.

## Making Failures Clear, Not Cryptic

When a check fails, the message matters. "Build failed" tells a developer, or an agent, nothing useful. "Architecture violation: Booking Service imported payment-domain/database directly. Use payment-domain/gateway instead, per ADR-014" tells them exactly what happened and how to fix it. This clarity matters even more for AI agents, since a clear error message allows the agent to correct its own code automatically, often without any human needing to step in at all.

## Coming Next

In Part 8, we walk through a full case study: how a real layering violation — an airline's controller reaching directly into a database it should never touch — gets caught by these pipeline gates before it ever reaches passengers.
