---
title: "Enforceable Architecture Part 1: Why Architecture Rules Die When Nobody Enforces Them"
date: 2026-01-05
categories: [architecture, aviation]
tags: [adr, fitness-functions, policy-as-code, spec-driven-development, agentic-engineering, enterprise-architecture, aviation]
excerpt: "A rule that only lives in a wiki diagram is not really a rule. Part 1 of a 10-part series on enforceable architecture, with aviation examples."
toc: false
---

{% include blog-sidebar.html %}

Imagine an airline has a rule: "The check-in service must never read customer data directly from the loyalty database. It must always go through the Loyalty API." This rule sounds simple. It sounds obvious. But where does this rule actually live?

In many companies, a rule like this lives in only one place: a diagram in a wiki page, or a slide in an old architecture presentation. Nobody checks it automatically. Nobody stops a developer, or an AI coding assistant, from breaking it. The rule looks strong on paper, but in practice, it does nothing. This is the core problem this series will explore: **an architecture rule that is not enforced by a system is not really a rule at all.**

## The Problem Is Bigger Today Than Before

Ten years ago, this problem was already real. Developers sometimes skipped rules because of tight deadlines, or because they did not read the wiki. But today, the problem is much bigger, because of AI coding agents.

An AI agent does not read your company wiki. It does not know about the diagram from 2021. It only sees what is inside the code repository, and what you tell it in the current task. If your rule is not written somewhere the agent can read and check, the agent will happily write code that breaks it — not because it is careless, but because it never had the information in the first place.

### Example 1: The Check-in Service and the Loyalty Database

Let's go back to our airline example. A team is under pressure to launch a new feature: showing loyalty points during check-in. An AI coding agent is asked to build this feature quickly. The agent looks at the check-in service code, sees a database connection already configured, and takes the fastest path: it queries the loyalty database directly.

Nobody told the agent this was forbidden. The architecture rule existed, but only as a diagram nobody linked to the code. Three weeks later, the loyalty database schema changes, and the check-in service breaks in production, during a busy travel weekend. The incident review takes twenty minutes to even find the cause, because the direct database call was never expected to exist.

### Example 2: Crew Rostering and Flight Schedule Changes

Here is a second case. Airlines have a Crew Rostering Service that decides which crew members work which flights. There is a rule: "Only the Crew Rostering Service may write to the crew schedule database. Other services must request changes through its API, so that legal rest-time rules are always checked."

A new Flight Operations tool is built to let dispatchers move flights quickly during bad weather. To save time, a developer — helped by an AI agent — writes code that updates the crew schedule database directly, skipping the Crew Rostering Service. The result: a crew member is assigned two flights that break mandatory rest-time rules. This is not just a bug. In aviation, it is a safety and compliance risk.

## The Real Lesson

In both examples, the architecture rule already existed. The problem was never that nobody thought of the rule. The problem is that the rule lived somewhere a machine — human or AI — could not check it automatically.

This is the idea we will build on for the rest of this series: architecture must move from documents that describe intent, to specifications that machines can read, check, and enforce. We will cover four building blocks: **ADR-as-spec**, **fitness functions**, **policy-as-code**, and a lightweight **review process** for handling exceptions.

## Coming Next

In Part 2, we will look at **ADR-as-spec** — how to write an Architecture Decision Record that is not just a document, but a specification a system can actually check against real code.
