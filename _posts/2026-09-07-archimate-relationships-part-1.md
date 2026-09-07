---
layout: default
title: "ArchiMate Relationships Part 1: The Serving Relationship in Aviation"
date: 2026-09-07
categories: ["enterprise architecture", "archimate"]
---

# ArchiMate Relationships Part 1: The Serving Relationship in Aviation

Welcome to Part 1 of my series on ArchiMate relationships!

Today we look at the **Serving Relationship**, which models an element serving or helping another.

### Aviation Example: Gate Operations

```plantuml
@startuml
!include <archimate/Archimate>

Archimate_ApplicationService(appService, "Flight Information Service")
Archimate_BusinessProcess(busProc, "Boarding Process")

Rel_Serving(appService, busProc, "Serves")
@enduml
```

### Key Rules to Remember
1. **Notation**: The serving relationship uses a dashed line with an open arrowhead pointing to the consumer.
2. **Layering**: Application Services use light blue, and Business Processes use yellow.
