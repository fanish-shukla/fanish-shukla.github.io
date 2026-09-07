---
title: "ArchiMate Relationships Part 2: The Composition Relationship in Aviation"
date: 2026-09-14
categories: [aviation, archimate]
tags: [archimate, enterprise-architecture, aviation, solution-architecture]
excerpt: "Exploring the Composition relationship in ArchiMate through an airline's departure process, detailing structural whole-part dependencies."
header:
  teaser: /assets/images/aviation/archimate-composition-relationship.svg
toc: false
---

{% include blog-sidebar.html %}

Welcome to **Part 2** of our 10-part ArchiMate series! In [Part 1]({% post_url 2026-09-07-archimate-serving-relationship-aviation %}), we covered how the **Serving** relationship links services to the roles and processes that consume them. 

Today, we delve into structural decomposition using the **Composition** relationship.

---

## What Is the Composition Relationship?

In ArchiMate 3.2, the **Composition** relationship models a strict whole-part relationship where one element consists of smaller sub-elements. 

* **Notation:** A solid line with a filled diamond at the parent ("whole") element end. Alternatively, nested boxes inside a parent container implicitly represent composition.
* **Core Semantics:** Existence dependency. If the parent element is removed, the child elements typically lose their operational context within that scope. The part can belong to only one whole at a time in a given viewpoint.

---

## Aviation Example: Airline Departure Process

A flight departure is not a single atomic event; it is an overarching business process comprised of distinct operational phases. Let's model the **Departure Process** and its subprocesses.

{% include drawio.html path="/assets/images/archimate/archimate-relationships-composition.drawio" %}


### Explicit Structural Decomposition:

* **Parent Element:** `Flight Departure Process` *(Business Process)*
* **Child Elements:** 
  * `Passenger Check-In Process` *(Business Process)*
  * `Security & Passport Control Process` *(Business Process)*
  * `Gate Boarding Process` *(Business Process)*

If the airline cancels or redesigns the overarching `Flight Departure Process`, these subprocesses lose their defined trigger sequence within this operational flow.

---

## Why Other Relationships Do Not Fit Here

Architects often confuse **Composition** with **Aggregation**, **Triggering**, or **Specialization**. Here is why those alternatives fail when defining a whole-part process breakdown:

| Relationship | Why It's Wrong in This Context |
| :--- | :--- |
| **Aggregation (`o--`)** | **Aggregation** represents a loose grouping of elements that can exist independently outside the parent (e.g., a portfolio of independent applications). In our example, `Gate Boarding` is an integral, mandatory component *of* the specific flight departure workflow. |
| **Triggering (`--->`)** | **Triggering** models the temporal sequence *between* subprocesses (e.g., `Check-In` triggers `Security Screening`). While triggering shows the timeline, **Composition** defines structural ownership—which process contains them both. |
| **Specialization (`--|>`)** | **Specialization** represents an "is-a" type inheritance (e.g., *Priority Boarding* is a special type of *Boarding*). `Security Screening` is not a type of `Flight Departure`; it is a phase *within* it. |

---

## Real-World Value in Enterprise Architecture

Understanding process composition is crucial during business process re-engineering (BPR) or core system migrations (such as updating an airport's operational database). 

By clearly mapping process composition:
* Enterprise Architects can calculate complete end-to-end process latency by summing composed subprocess durations.
* Ownership and governance can be assigned effectively (e.g., Airport Authorities owning Security Screening, while Ground Handlers own Gate Boarding).
* Solution Architects can cleanly scope API boundaries for underlying IT automation.

---

## Coming Next

In **Part 3**, we will explore the **Realization** relationship. We will look at how underlying IT components and application services realize higher-level business requirements and services.

Thank you for reading! Leave your feedback or questions in the comments below.