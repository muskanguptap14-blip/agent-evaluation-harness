---
doc: checklist
status: approved
---

# Build Checklist

Build mode: learn

## Slices

- [x] **1. A task can be validated and run from a single CLI entry**
  Becomes usable: The harness accepts a prompt or challenge file, validates it, and boots a runnable local evaluation flow. It can start without crashing and show the user exactly what input it accepted.
  Why now: This proves the project shape and the data contract early, which is the minimum foundation for any real agent-run evaluation.
  PRD ref: `prd.md > Task Setup and Run Control`, `prd.md > The Core Journey`
  Spec ref: `spec.md > Components`, `spec.md > Data Model`, `spec.md > Where It Runs and How Someone Tries It`
  Build: Create the Python package structure, add the Pydantic models for input validation, build the CLI entry, and support both quick prompt and challenge-file inputs.
  Verify (mechanical): Run `python -m agent_eval --help` and run a minimal valid challenge file; confirm the app accepts the input without validation errors.
  Learner check: Open the CLI and try a quick prompt and a challenge file; decide whether the flow feels straightforward and intentional.
  Commit: `Add CLI and challenge validation`

- [x] **2. The harness can run a sandboxed evaluation and show pass/fail results**
  Becomes usable: The app can execute a local task in a temporary sandbox, run pytest, and report which requirements passed or failed.
  Why now: This is the unique kernel of the project — showing real evidence about the agent's result instead of a vague AI answer.
  PRD ref: `prd.md > Automated Evaluation`, `prd.md > What We're Building`
  Spec ref: `spec.md > Agent Runner`, `spec.md > Evaluator`, `spec.md > Result Reporter`
  Build: Add the sandbox execution path, run pytest against the sample project, and translate test outcomes into a requirement-by-requirement pass/fail matrix.
  Verify (mechanical): Run the evaluator against the sample project and confirm it prints a pass/fail matrix with clear totals.
  Learner check: Run the harness once and tell me whether the output makes the result clear enough to trust.
  Commit: `Add sandboxed test evaluation`

- [x] **3. Token usage and summary metrics are visible in the run report**
  Becomes usable: A final summary includes total pass/fail counts, the matrix, and token usage so the user can judge both correctness and cost.
  Why now: A scorecard without cost is not the full evaluation loop the learner wants, and this is the feature that makes the tool useful as a developer benchmark.
  PRD ref: `prd.md > Metrics and Cost Visibility`, `prd.md > The Core Journey`
  Spec ref: `spec.md > Metrics Collector`, `spec.md > Data Model`
  Build: Add metrics collection for token usage and run duration, then print a concise summary alongside the pass/fail matrix.
  Verify (mechanical): Run the full flow and confirm the output includes token usage and a final status summary.
  Learner check: Review the final summary and say whether it explains the evaluation clearly enough to use for a quick decision.
  Commit: `Add token metrics and summary report`

## Hands-on Checkpoints

- [x] Early usable behavior explored — first CLI validation and task entry run
- [x] Final kick-the-tires exploration and feedback completed

## Final Review

- [x] Final review complete — feedback resolved and learner confirms ready to ship

## Code Tour and App Map

- [x] Learning activity complete — guided route through the CLI entry, challenge validation, sandbox runner, and evaluation report; the reusable pattern was defining the evidence before the mechanism.
- [x] Optional edit and transfer reflection addressed — offered and left open as a brief prompt; no extra exercise required.
- [x] `devpost/app-map.html` generated from finished code, checked, and shown, including a project-grounded practice to reuse

Activity and evidence: The harness was exercised by running `python -m agent_eval --challenge challenges/sample.json --project sample_project`, which produced a requirement-by-requirement pass/fail matrix and a token-usage summary. The evidence is in the output and in the files `agent_eval/cli.py`, `agent_eval/evaluator.py`, and `agent_eval/reporter.py`.
Route and stops: CLI entry → validation models → challenge loader → sandbox runner → evaluator → reporter. The relevant paths are `agent_eval/cli.py`, `agent_eval/models.py`, `agent_eval/challenge.py`, `agent_eval/runner.py`, `agent_eval/evaluator.py`, and `agent_eval/reporter.py`.
Edit outcome: No edits were required after the verified run; the app already matched the agreed behavior.
Reflection: Offered briefly as a transfer question about what the learner would do differently next time with an agent; no forced response or quiz was given.
Activity mode: live app and editor verification via the local CLI.

## Revisions
