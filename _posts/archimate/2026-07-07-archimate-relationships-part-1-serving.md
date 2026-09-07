---
title: "ArchiMate Relationships Part 1: The Serving Relationship in Aviation"
date: 2026-07-07
categories: [aviation, archimate]
tags: [archimate, enterprise-architecture, aviation, solution-architecture]
excerpt: "Starting a 10-part series on ArchiMate relationships, explained with practical, multi-layer aviation architecture examples."
header:
  teaser: /assets/images/aviation/archimate-serving-relationship.svg
toc: false
---

{% include blog-sidebar.html %}

Hello and welcome! My name is Fanish Shukla. As a Solution Architect with experience at SWISS International Air Lines and as part of the Lufthansa Group Enterprise Architecture team, I’ve spent years using **ArchiMate** to map complex aviation ecosystems. 

ArchiMate is an open standard modeling language that allows Enterprise Architects to visualize the structural relationships between strategy, business processes, applications, and technology infrastructure.

This post is **Part 1 of a 10-part series** designed to break down ArchiMate relationships step-by-step using practical aviation scenarios. Airlines are ideal subjects for EA modeling because they rely on tightly coupled business services, physical operations, and high-availability IT platforms.

---

## What Is the Serving Relationship?

In ArchiMate 3.2, the **Serving** relationship (formerly known as *Used By* in ArchiMate 1.0/2.0) models how an element provides functionality, behavior, or infrastructure to another element. 

* **Notation:** A solid line with an open arrowhead pointing toward the target element receiving the service.
* **Core Semantics:** The source element exposes a service, interface, or capability that is consumed by the target element to achieve its goals.

---

## Aviation Example: Multi-Layer Passenger Boarding

To see how the Serving relationship works in practice, let's look beyond a simple 1:1 interaction and map a cross-layer scenario: **How a Departure Control System (DCS) serves airport gate operations.**

{% include drawio.html path="/assets/images/archimate/archimate-serving-relationship.drawio" %}


### Breakdown by Layer:

1. **Application Layer to Business Layer:**
   * **Source Element:** `DCS Barcode Validation Service` *(Application Service)*
   * **Target Element:** `Passenger Gate Boarding Service` *(Business Service)*
   * **Explanation:** The background software platform validates the 2D PDF417 barcode on a boarding pass in milliseconds. It provides an application service that **serves** the broader business service.

2. **Business Layer to Business Role:**
   * **Source Element:** `Passenger Gate Boarding Service` *(Business Service)*
   * **Target Element:** `Gate Agent` *(Business Role)*
   * **Explanation:** The operational business service provides the physical and digital means for the Gate Agent to verify identity, release seat holds, and allow passenger boarding.

---

## Why Other Relationships Do Not Fit Here

A common pitfall for solution architects new to ArchiMate is selecting the wrong relationship type when connecting services to processes or roles. Here is why alternative relationships fail in this scenario:

| Relationship | Why It's Wrong in This Context |
| :--- | :--- |
| **Realization (`--\|>`)** | **Realization** means an entity creates or fulfills a concept (e.g., an Application Component *realizes* an Application Service). A `DCS System` *realizes* the software service, but the software service does not *realize* the Gate Agent—it merely **serves** them. |
| **Access (`--->`)** | **Access** models behavioral elements reading or writing Data/Business Objects (e.g., a process *accesses* a Passenger Manifest). A service isn't a data payload being read/written; it's an operational capability being consumed. |
| **Triggering (`--->`)** | **Triggering** models state-based or temporal sequence flow between behavior elements (e.g., *Check-in completed* triggers *Security Screening*). A service does not "trigger" an actor; it remains available for the actor to consume. |
| **Assignment (`o->`)** | **Assignment** links active structure elements to behaviors or roles (e.g., a specific employee *assigned* to the Gate Agent role). The DCS system is not assigned to be the agent; it provides a platform service to them. |

By using the **Serving** relationship, you explicitly define functional dependencies across enterprise layers without confusing them with data flow, process execution order, or structural ownership.

---

## Real-World Value in Enterprise Architecture

In large organizations like Lufthansa Group, clarity in service dependencies is vital. When an application team plans downtime or updates for a core system like Amadeus Altéa or Sabre DCS, running an impact analysis through the **Serving** chain immediately reveals:
* Which **Application Services** will go offline.
* Which operational **Business Services** will be degraded.
* Which ground-handling **Roles** (e.g., Ramp Agents, Gate Staff, Check-in Clerks) need manual contingency procedures.

---

## Coming Next

In **Part 2**, we will explore the **Composition** relationship. We will break down how an airline's overarching *Departure Process* is composed of discrete, structural subprocesses like security check, document verification, and boarding.

Thank you for reading! Feel free to leave your thoughts or questions in the comments below.