---
doc: scope
status: approved
---

# Agent Eval Harness

A lightweight developer tool that runs Python coding tasks in a controlled sandbox, evaluates agent output with automated tests, and shows pass/fail matrices, individual checks, and token usage so the user can judge whether a run is efficient and reliable.

## The Unique Kernel
The distinctive part is not just “run tests” — it is a controlled evaluation loop between the user and the coding agent. The harness interrupts the agent run, executes automated checks, records the pass/fail matrix for each test case or requirement, tracks token usage, and makes the cost and effectiveness of a run visible before the agent wanders too far off track. It turns a fuzzy AI workflow into something measurable.

## Who It's For
A Python developer or technical builder who is testing AI coding agents on small tasks and wants more visibility into whether the model is actually solving the task, not just generating plausible code. Today they may rely on ad hoc prompts, repeated agent runs, and manual checking; this tool gives them a structured way to judge reliability and token cost.

## The Core Loop
The user defines a task or sample challenge, the harness runs the agent in a sandboxed environment, the agent writes or edits Python code, the harness executes automated checks, and then it reports the results: which tests passed, which failed, how many tokens were used, and whether the run stayed within a useful threshold. The user then iterates on prompts or constraints based on the scorecard.

## Inspiration & Identity
The project feels like a developer tool for debugging AI workflows rather than a polished product for end users. The energy is practical, analytical, and “AI engineering for real work”: minimal friction, clear signals, and fast feedback. It should feel focused and useful, with a terminal-first or lightweight dashboard view rather than a consumer app aesthetic.

## Why This Matters to the Learner
This matters because the learner wants to understand the structure and workflow of building an AI harness rather than just making an app. They want a firsthand way to learn how an agent can be constrained, evaluated, and monitored, especially in the early phases of building AI systems.

## What "Working" Looks Like
The proof of concept is a small harness that can take a Python task, run a code-generation agent against it, and automatically evaluate the result using unit tests. The compelling moment is seeing a run produce a readable pass/fail matrix—such as each requirement or test outcome marked passed or failed—alongside a summary of total tests, failed checks, and token usage. That makes the quality and cost of the run immediately understandable.

## The POC Boundary
In scope:
- a simple task runner for Python scripts
- an evaluation loop with automated unit tests
- structured pass/fail matrix tracking for individual checks or tests
- summary metrics such as total tests, passed tests, failed tests, and success rate
- token usage tracking for a run
- a small CLI or lightweight UI that presents the results clearly

Out of scope for the hackathon:
- full multi-agent orchestration
- persistent benchmarking databases or historical analytics dashboards
- deployment as a hosted service
- wide support for many languages or complex sandboxing

## Later
- richer scoring models with weighted metrics
- result history and trend charts over many runs
- task templates and benchmark suites
- richer sandboxing and security hardening
- agent retries and smarter prompt interventions

## Explicitly Cut
- Full-blown agent marketplace or user auth: not necessary for the proof of concept and not aligned with the core learning objective.
- Production-grade distributed execution: too large for this project and not required to demonstrate the harness concept.
- Large polished dashboard with many analytics views: useful later, but the early proof should stay minimal and focused on the evaluation loop.
