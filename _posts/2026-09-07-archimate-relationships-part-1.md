---
title: "ArchiMate Relationships Part 1: The Serving Relationship in Aviation"
date: 2026-09-07
layout: post
categories: [Enterprise Architecture, ArchiMate]
tags: [archimate, aviation, swiss, lufthansa-group]
---

Welcome to Part 1 of my 10-part series on ArchiMate relationships!

Based on my experience working as a Solution Architect for **SWISS International Air Lines** and as part of the **Lufthansa Group Enterprise Architecture** group, I want to show how to apply ArchiMate practically in the aviation domain.

Today, we look at the **Serving Relationship**. This relationship shows that an element (like an IT system or service) serves or helps another element (like a business process).

### Aviation Example: Gate Operations

At SWISS, smooth ground operations are critical. The **Flight Information System** provides real-time data to support the **Boarding Process** at the airport gate. Without this application service, gate agents cannot verify passenger status or start boarding.

Here is the exact ArchiMate 3.0 model:

```plantuml
@startuml
!include <archimate/Archimate>

' Elements
Archimate_ApplicationService(appService, "Flight Information Service")
Archimate_BusinessProcess(busProc, "Boarding Process")

' Relationship
Rel_Serving(appService, busProc, "Serves")
@enduml
```

### Key Rules to Remember

1. **Notation:** The serving relationship uses a dashed line with an open arrowhead pointing from the provider to the consumer.
2. **Layering:** Application Services use light blue, and Business Processes use yellow.

In Part 2, we will explore the **Assignment Relationship** for airport ground handling teams!
