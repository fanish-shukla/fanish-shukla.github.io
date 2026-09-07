---
title: "Enforceable Architecture Part 8: Case Study — Catching a Layering Violation Before It Ships"
date: 2026-04-20
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "A walkthrough of one violation, from the moment code is written to the moment a fitness function catches it."
toc: false
---

{% include blog-sidebar.html %}

We have covered each piece separately: ADR-as-spec, fitness functions, policy-as-code, exceptions, and CI/CD gates. Today, in Part 8, we walk through one complete story, step by step, showing how all these pieces work together to catch a real problem before it reaches passengers.

## The Setup

Our airline's Check-in Service has a rule, written as an ADR-as-spec back in Part 2: "Check-in Service must never call the Loyalty Database directly. It must always go through the Loyalty API, because the API applies rate limits and data masking rules that protect passenger privacy." This rule has an attached fitness function, and it runs as a required pull request check, as we described in Part 7.

## Step One: The Task Is Given to an AI Agent

A product manager asks for a small feature: "Show the passenger's loyalty tier during check-in, so gate agents can prioritize boarding correctly." Under Spec-Driven Development from Part 5, this task is written with its relevant constraints attached: "Must use Loyalty API only, per ADR-014. Fitness function `no-direct-loyalty-db-access` must pass." An AI coding agent is assigned this task inside the check-in repository.

## Step Two: The Agent Writes Code

The agent looks at the check-in service and, honestly, finds two ways to get the loyalty tier: call the Loyalty API, which requires an extra network request and a small amount of new code, or query the loyalty database directly, since a database connection already exists in the codebase for an older, unrelated feature. Without the specification, many agents would pick the second option — it is faster to write and appears to work in local testing. But the specification given to the agent explicitly states the constraint, so the agent generates code using the Loyalty API, as instructed.

## Step Three: A Second Agent Makes a Different Change

Two days later, a different engineer, working on a separate task, asks an AI agent to fix a slow-loading issue on the check-in screen. This agent, focused only on speed, and without the same specification attached to its task, decides to remove the "unnecessary" Loyalty API call and replace it with a direct database read, believing this improves performance. This code passes the engineer's own local tests, because the database is reachable in the development environment.

## Step Four: The Fitness Function Catches It

The engineer opens a pull request. The required CI/CD check from Part 7 runs the `no-direct-loyalty-db-access` fitness function automatically. It scans the changed files, finds a new import connecting directly to the loyalty database, and fails the build with a clear message: "Architecture violation: Check-in Service imports loyalty-domain/database directly. Use loyalty-domain/api instead, per ADR-014." The pull request cannot be merged until this is fixed.

## Step Five: The Fix, or the Exception

The engineer has two paths. If the direct database access was truly a mistake, made only to fix a perceived performance problem, the fix is simple: restore the Loyalty API call, and investigate the real cause of slowness separately. If there is a genuine, urgent reason the API cannot be used right now — perhaps the API itself is having an outage — the engineer follows Part 6's process, requesting a time-boxed exception from the review board, rather than quietly bypassing the rule.

## Why This Story Matters

Nobody in this story acted badly. The second agent optimized reasonably, given what it was told. The engineer trusted their local tests. But because the rule was written as ADR-as-spec, checked by a fitness function, and enforced as a required pull request gate, the violation was caught automatically, within minutes, long before it could affect a real passenger's data privacy during check-in.

## Coming Next

In Part 9, we look at what happens when architecture itself needs to change: how to version your policies safely, so an old rule does not silently block a legitimate new pattern forever.
