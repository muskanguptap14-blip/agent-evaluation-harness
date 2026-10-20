---
doc: prd
status: approved
---

# Agent Eval Harness — Product Requirements

A lightweight developer tool that sits between the user and their coding agent, runs Python tasks in a sandbox, evaluates the agent's output with tests, and turns the results into a readable scorecard for reliability, failure points, and token usage.
Source: `scope.md > The Core Loop`, `scope.md > The Unique Kernel`, and `scope.md > What "Working" Looks Like`.

## The Core Journey
1. The user opens the harness and sees a clean workspace for a task: a task description or prompt area, a way to set the project/test context, and a status panel showing the run state.
2. They define a coding task or input scenario for the AI agent, usually a small Python coding challenge or bugfix request.
3. The harness launches the agent in a controlled sandbox and starts tracking the run. The user can see what the agent is doing, which files are changing, and the current status of the task.
4. When the agent finishes, the harness runs automated evaluation checks against the work. It compares the result to the expected test suite and records which checks passed and which failed.
5. The harness presents a concise scorecard: the pass/fail matrix, summary totals, and token usage. The user can quickly tell whether the run succeeded, where it failed, and whether the cost was acceptable.
6. The user uses the results to refine prompts, constraints, or task scope and retries until the agent output is reliable enough to trust.

## Screens and Layout
This is a small developer tool, not a broad dashboard. The interaction surface is a single workspace with a few key areas:
- A task input area or prompt panel where the user enters the task and optional constraints.
- A live run panel showing the current state of the agent run, file changes, and progress.
- A result panel showing automated checks, pass/fail status, and a summary of the run.
- A lightweight metrics area for token usage and overall run health.

The layout should feel practical and readable rather than decorative: information is grouped by state and immediately actionable.

## Look and Feel
The product should feel like a serious developer utility, not a consumer app. The tone is practical, minimal, and transparent. It should feel like a debugging tool for AI workflows: confident, observably honest about failures, and fast to understand. The interface should favor clear structure, strong contrast, and readable output over visual flourish.

## Features and Behavior

### Task Setup and Run Control
The user can define the task to be executed, choose the relevant project or test context, and start a run. The tool should make it obvious when a run is active, completed, or failed.

- As a developer testing an AI coding agent, I want to start a task run with a clear prompt and context so that I can evaluate the agent without manual setup.
  - [ ] Acceptance criterion — the user can enter a task description and start a run from the main interface
  - [ ] Acceptance criterion — the harness indicates the run status clearly while the agent is working

### Live Transparency
The harness should show what changed during the run without overwhelming the user. It should surface the agent's progress in a way that helps the user understand whether the agent is drifting, making progress, or failing.

- As a developer, I want to see what the agent is doing while the run is in progress so that I can know whether the task is moving in the right direction.
  - [ ] Acceptance criterion — the user can view the current task state and the files or code areas being touched
  - [ ] Acceptance criterion — the interface makes active progress readable without requiring full log scrolling

### Automated Evaluation
Once the task finishes, the harness evaluates the output using automated tests. It records which checks passed or failed and surfaces that clearly.

- As a developer, I want to see pass/fail results for each automated test or requirement so that I can judge the quality of the agent's output.
  - [ ] Acceptance criterion — a pass/fail matrix is visible after a run completes
  - [ ] Acceptance criterion — each test or requirement is labeled as pass or fail, with enough detail to understand the result

### Metrics and Cost Visibility
The harness tracks token usage alongside test outcomes. The user can quickly compare performance and cost to decide whether the run was worthwhile.

- As a developer, I want to know how many tokens were used and whether the run succeeded so that I can decide whether the cost is acceptable.
  - [ ] Acceptance criterion — the result summary includes token usage and a success/failure indicator
  - [ ] Acceptance criterion — the summary makes the tradeoff between correctness and cost understandable at a glance

## States and Boundaries
- **Idle** — the user is ready to define a task or review a previous run. No active agent execution is in progress.
- **Running** — the agent is executing, the harness is tracking changes and status, and the user can monitor progress.
- **Evaluating** — the agent run has ended, and the system is executing automated checks and compiling results.
- **Completed** — the harness displays the pass/fail matrix, summary metrics, and token usage.
- **Failure** — the task did not meet the required checks or the harness could not complete a valid run; the user sees which failures blocked success.
- **Empty state** — before the first run, the user sees the task input and a clear prompt to begin, rather than a blank or confusing screen.

## Product Decisions
- The harness supports both a quick single-prompt run and a structured challenge file (for example, a JSON or YAML input) because the learner wants maximum flexibility: fast manual testing for quick checks and a batch-style challenge format for more serious evaluation.
- The scorecard is requirement-by-requirement rather than raw test-by-test because the learner wants to judge whether the agent is meeting each stated requirement and constraint, including things like token budget adherence.
- The interface is intentionally minimal and terminal-friendly rather than a polished consumer dashboard because the product is first and foremost a developer evaluation tool.
- The user is focused on structured quality and cost signal, not on broad analytics or heavy experimentation, so the harness prioritizes clarity over visual sophistication.
- The product should be small and repeatable for short tasks so it can prove the idea in a single demo and remain useful for learning how AI agent evaluation works.

## What We're Building
The proof of concept must include:
- a task entry flow for a small Python coding challenge
- a run lifecycle with start, active status, and completion
- automated evaluation against unit tests or checks
- a visible pass/fail matrix for each test or requirement
- a summary of pass/fail totals and token usage
- a simple interface that makes results readable to a developer

## Deferred From the POC
- Persistent history across many runs and benchmark comparisons
- Multi-agent orchestration or advanced retry logic
- Security hardening for full sandbox isolation beyond the small demo scope
- User accounts, shared workspaces, or collaborative runs
- Expensive dashboard features like historical trend charts or rich analytics

## Possible Later Enhancements
- Benchmark suites across many task types
- Weighted scoring for different types of tests or requirements
- Historical run comparisons and trend analysis
- Smarter prompts or agent guidance based on previous failures
- Better sandbox isolation and environment templating

## Non-Goals
- A general-purpose AI coding platform for all users
- A consumer-facing app with polished design and multi-user workflows
- Full production-grade agent orchestration or deployment infrastructure
- Broad language support beyond the Python proof-of-concept scope

## Open Questions
- The exact task input format and whether the harness will support a single prompt, a challenge file, or both — the learner has already chosen both, so this is now a confirmed product decision and should be reflected in the spec.
- The exact shape of the pass/fail matrix: requirement-by-requirement rows are the chosen model, with each row representing a specific requirement or check.
- Whether the result summary should be terminal output only or include a lightweight dashboard view — this can be decided in the technical plan without changing the product intent.
