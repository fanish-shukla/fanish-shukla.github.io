---
title: "ArchiMate Relationships Part 1: The Serving Relationship in Aviation"
date: 2026-09-07
categories: [Enterprise Architecture, ArchiMate]
tags: [archimate, aviation, swiss, lufthansa-group]
mermaid: true
---

Welcome to Part 1 of my 10-part series on ArchiMate relationships! 

Based on my experience working as a Solution Architect for **SWISS International Air Lines** and as part of the **Lufthansa Group Enterprise Architecture** team, I want to show how to apply ArchiMate practically in the aviation domain.

Today, we look at the **Serving Relationship**. This relationship shows that an element (like an IT system or service) serves or helps another element (like a business process).

### Aviation Example: Gate Operations

At SWISS, smooth ground operations are critical. The **Flight Information System** provides real-time data to support the **Boarding Process** at the airport gate. Without this application service, gate agents cannot verify passenger status or start boarding.

Here is how we model this in ArchiMate:

```mermaid
graph LR
    A["Flight Information Service<br/>(Application Service)"] -->|Serves| B["Gate Boarding Process<br/>(Business Process)"]
    style A fill:#d4e6f1,stroke:#1b4f72,stroke-width:2px
    style B fill:#fcf3cf,stroke:#7d6608,stroke-width:2px
