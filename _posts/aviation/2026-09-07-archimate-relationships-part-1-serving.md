---
title: "ArchiMate Relationships Part 1: The Serving Relationship in Aviation"
date: 2026-09-07
categories: [aviation, archimate]
tags: [archimate, enterprise-architecture, aviation, solution-architecture]
excerpt: "Starting a 10-part series on ArchiMate relationships, explained with simple aviation examples."
header:
  teaser: /assets/diagrams/archimate-serving-relationship.svg
toc: false
---

Hello! My name is Fanish Shukla. I work as a Solution Architect. I worked for SWISS International Air Lines. I was also part of the Lufthansa Group Enterprise Architecture (EA) team. In this team, we used a tool called ArchiMate. ArchiMate helps us draw pictures of a business. These pictures show how people, processes, and IT systems work together.

This is **Part 1** of a 10-part series. In each part, I will explain one ArchiMate relationship. I will use simple examples from the aviation world. Airlines are a great example, because they have many services — like check-in, boarding, and baggage handling.

## What Is ArchiMate?

ArchiMate is a modeling language. This means it is a way to draw pictures with clear rules. These pictures are called diagrams. Enterprise Architects use ArchiMate diagrams to show how a company works. The diagrams use boxes and arrows. Each box is called an **element**. Each arrow is called a **relationship**.

## Today's Relationship: Serving

Today we learn about the **Serving** relationship. Serving means: "One thing helps another thing." In ArchiMate, we draw Serving with a simple line and an open arrow head. The arrow points to the element that receives the help.

### Aviation Example

Let's look at an airline check-in process.

- **Check-in Service** — this is a *Business Service*. A Business Service is something the airline offers to its customers.
- **Passenger** — this is a *Business Actor*. A Business Actor is a person who uses the service.

In the diagram below, the **Check-in Service** serves the **Passenger**. This means the check-in desk exists to help the passenger. The passenger does not do work for the service — the service works for the passenger.

![ArchiMate Serving relationship example: Check-in Service serving Passenger](/assets/diagrams/archimate-serving-relationship.svg)

## Why This Matters

In real airline projects, we use Serving relationships very often. For example:

- A **Baggage Handling Service** serves the **Passenger**.
- A **Flight Booking Service** serves the **Travel Agent**.

When you draw these relationships correctly, everyone in the company understands who helps whom. This is very useful in large organizations like Lufthansa Group, where many teams and systems work together.

## How I Made This Diagram

I did not use PlantUML or Mermaid, because those tools do not draw real ArchiMate shapes. Instead, I used a free online tool called **draw.io** (also called diagrams.net).

To make your own ArchiMate diagrams:

1. Go to **app.diagrams.net** in your browser.
2. Click **More Shapes** at the bottom of the shape panel.
3. Search for **"ArchiMate"** and turn on the **ArchiMate 3** shape library.
4. Now you can drag real ArchiMate shapes and relationships onto your canvas.

No installation is needed — everything works in your browser. You can even connect draw.io directly to your GitHub repository, so your diagrams save straight into your blog's source code.

## Coming Next

In **Part 2**, we will learn about the **Composition** relationship. We will see how an airline's "Departure Process" is made of smaller steps, like check-in, security, and boarding.

Thank you for reading! If you work in aviation or enterprise architecture, I hope this series helps you understand ArchiMate step by step.
