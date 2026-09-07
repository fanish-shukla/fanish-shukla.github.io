---
title: "Enforceable Architecture Part 5: Spec-Driven Development in the Agent Era"
date: 2026-03-05
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "AI agents write code fast. Spec-Driven Development makes sure they write the right code, not just fast code."
toc: false
---

{% include blog-sidebar.html %}

Over the last four parts, we built three pieces: ADR-as-spec (Part 2), fitness functions (Part 3), and policy-as-code (Part 4). Today we step back and look at the bigger idea these pieces support: **Spec-Driven Development**, often shortened to **SDD**.

Spec-Driven Development means this: before an AI agent — or a human developer — writes code, there is a clear, structured specification describing what the code must do, and what rules it must follow. The agent's job is to satisfy the specification, not to guess at intent from a short chat message. This sounds obvious, but it is a real change from how many teams work with AI agents today.

## The Problem SDD Solves

A common way teams use AI agents right now looks like this: someone writes a short instruction, such as "add a discount code feature to the booking flow," and the agent writes code based on that one sentence. The agent has no specification of business rules, no fitness functions to check against, no policy to follow. It guesses, using patterns from its training and whatever it finds in the repository. Sometimes the guess is good. Sometimes it quietly breaks a rule nobody told it about.

SDD flips this. Before the agent starts, there is a specification: what the feature must do, which ADRs apply, which fitness functions must still pass, and which policies must be respected. The agent generates code against this specification, and the same automated checks from Parts 3 and 4 verify the result — whether a human or an AI wrote it.

### Example 1: Adding a Discount Code Feature

Consider our airline's booking flow again. A product manager asks for a new discount code feature. Under the old approach, an agent might implement this by adding a new field to the Booking Service and writing directly to the Payment Service's database, to apply the discount before payment — breaking the rule from Part 2 that forbids direct payment domain access.

Under SDD, the task given to the agent includes the relevant specification: "Add discount code support. Must call Payment Gateway only, per ADR-014. Fitness function `no-direct-payment-calls` must pass." The agent now has the actual constraint, not just the feature request. If it still tries a shortcut, the fitness function from Part 3 catches it immediately, before the code is even reviewed by a human.

### Example 2: Building a New Delay Notification Service

Here is a second case. An airline wants a new service that sends passengers a notification when their flight is delayed by more than fifteen minutes. Without a specification, an AI agent might connect this new service directly to the airport's local display system for speed — the exact problem we saw in Part 2's baggage handling example.

With SDD, the specification given to the agent states clearly: "Delay data must come only from Flight Operations Service, per ADR-009. Data must be refreshed at least every two minutes, per the freshness fitness function from Part 3." The agent builds the notification service against this specification from the start, and the same automated checks confirm the result. The specification does the work that used to depend on a developer remembering, or reading, an old wiki page.

## Why This Matters for Leaders, Not Just Engineers

As a Solution Architect or an Enterprise Architecture leader, SDD changes your role. You are no longer only reviewing finished code. You help define the specifications, ADRs, and policies that shape what gets built in the first place — for both human developers and AI agents. This is a more strategic role, and it scales much better across a large organization than manual code review alone.

## Coming Next

In Part 6, we look at what happens when a rule genuinely needs to be broken for a good reason — and how to build an **exception-driven review board** that handles this without slowing everything down.
