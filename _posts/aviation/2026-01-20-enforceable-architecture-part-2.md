---
title: "Enforceable Architecture Part 2: ADR-as-Spec — Decisions a Machine Can Actually Check"
date: 2026-01-20
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "Most Architecture Decision Records are just prose nobody re-reads. Part 2 shows how to turn them into specs a system can check."
toc: false
---

{% include blog-sidebar.html %}

In Part 1, we saw that a rule nobody enforces is not really a rule. Today we look at the first building block for fixing this: the **Architecture Decision Record**, or **ADR**.

Most teams already write ADRs. An ADR is a short document that explains a decision: what was decided, why, and what other options were rejected. This is useful. But a normal ADR is just text. A developer, or an AI agent, has to read it, understand it, and remember to follow it. As we saw before, this often does not happen.

**ADR-as-spec** means something different. It means writing the ADR so that, alongside the human-readable explanation, there is a small, precise, machine-checkable rule attached to it. The ADR still explains the "why" for people. But it also states the "what" in a form a tool can test automatically.

## What an ADR-as-Spec Looks Like

A traditional ADR might say: "Services in the booking domain must not call services in the payment domain directly. All payment requests must go through the Payment Gateway."

An ADR-as-spec keeps that sentence, but adds a small block underneath, written in a simple, structured format, such as:

```
rule: no-direct-payment-calls
applies_to: booking-domain/*
forbids: import from payment-domain/* except payment-domain/gateway
severity: blocking
```

This block is not just documentation. It is input for an automated check — something we will explore fully in Part 3, when we talk about fitness functions. The key idea today is simpler: **the ADR itself becomes the source of truth for both humans and machines.**

### Example 1: Booking and Payment Domains

Consider an airline's booking platform. A rule states that the Booking Service must never call the Payment Service's internal database functions directly — it must always go through the public Payment Gateway API, because the gateway handles fraud checks and currency conversion rules that differ by country.

Without ADR-as-spec, this rule sits in a document. An AI agent asked to "speed up the booking flow" might bypass the gateway to save a network call, breaking fraud checks without anyone noticing until a chargeback dispute appears weeks later. With ADR-as-spec, the same rule is attached to a checkable pattern: any import from the payment domain, outside the gateway module, fails a check before the code is even merged.

### Example 2: Baggage Handling and Airport Systems

Here is a second case. An airline's Baggage Handling Service must only receive flight status updates from the official Flight Operations Service — never from a third-party airport display system, because airport-provided data is sometimes delayed or incorrect. An ADR captures this decision: "Baggage Handling accepts flight status only from Flight Operations Service."

Written as a normal ADR, this is easy to forget six months later, when a new integration team, wanting a quick fix for a data gap, connects Baggage Handling directly to an airport's local system. Written as ADR-as-spec, the allowed data source is a structured rule: `baggage-handling accepts flight-status only from flight-ops-service`. Any new code path violating this can be caught automatically, long before a bag gets sent to the wrong gate because of bad data.

## Why This Matters for Solution Architects

As a Solution Architect, you already write these decisions. The shift is small in effort, but large in impact: instead of writing a decision only for humans to read once, you write it so the decision keeps applying, automatically, to every future change — including changes made by an AI agent that has never read your original document.

## Coming Next

In Part 3, we will look closely at **fitness functions** — the automated checks that actually read these ADR specs and test real code against them, continuously.
