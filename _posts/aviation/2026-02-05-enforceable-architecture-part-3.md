---
title: "Enforceable Architecture Part 3: Fitness Functions — Automated Tests for Your Architecture"
date: 2026-02-05
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "You already test your code. Part 3 explains fitness functions — the equivalent tests for your architecture."
toc: false
---

{% include blog-sidebar.html %}

In Part 2, we turned architecture decisions into small, structured rules — ADR-as-spec. But a rule written down, even in a structured format, does nothing by itself. Something has to actually read it and check the real code against it. That "something" is a **fitness function**.

A fitness function is simply an automated test, but instead of testing whether a feature works correctly, it tests whether your architecture still matches your intended design. You already run unit tests and integration tests on every code change. A fitness function is the same idea, applied to structure, not behavior.

## What a Fitness Function Actually Does

A fitness function reads the rule from your ADR-as-spec (Part 2), scans the codebase, and answers one question: does the code still follow this rule? If yes, the build passes. If no, the build fails, and the developer — or the AI agent — sees the failure immediately, in the same place they see a failed unit test.

This is powerful because it does not depend on anyone remembering the rule. It does not depend on a human doing a manual architecture review once a quarter. It runs automatically, every time code changes, exactly like your test suite.

### Example 1: Checking the Booking-to-Payment Rule

Remember the rule from Part 2: the Booking Service must never call the Payment Service directly, only through the Payment Gateway. A fitness function for this rule is a small script that scans all import statements in the booking codebase. If it finds any import from `payment-domain` that is not `payment-domain/gateway`, the build fails with a clear message: "Architecture violation: direct payment domain access is forbidden. Use the Payment Gateway."

This check takes a few seconds to run. It runs on every pull request, including pull requests created or modified by an AI coding agent. If an agent, trying to "optimize" the booking flow, adds a direct payment call, the fitness function catches it before a human reviewer even opens the pull request — and long before it reaches production and affects real passengers making real payments.

### Example 2: Checking Flight Data Freshness Rules

Airlines often have a rule like this: "Any service showing flight departure times to passengers must refresh its data from Flight Operations at least every two minutes. Cached data older than this is not allowed to be displayed." This rule protects passengers from seeing outdated gate or delay information.

A fitness function for this rule does not just check code structure — it can run a lightweight check against a test environment, asking a display service for its data, then checking the timestamp attached to that data. If the timestamp is older than two minutes, the fitness function fails the build. This catches a real, dangerous problem early: a caching layer added later by a well-meaning developer, which quietly breaks the freshness guarantee, gets caught in minutes, not discovered after a passenger complains about a wrong gate number.

## Why Fitness Functions Matter More With AI Agents

A human developer sometimes questions a shortcut and pauses to ask, "Is this allowed?" An AI agent, by default, does not pause. It optimizes for the task it was given. Fitness functions give the agent — and the whole team — fast, automatic feedback, so the architecture stays correct even when nobody manually reviewed every line.

## Coming Next

In Part 4, we move up one level: **policy-as-code**, where we take many fitness functions and organize them into a shared, reusable set of rules that apply across an entire airline's technology landscape, not just one service.
