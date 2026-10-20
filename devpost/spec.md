---
doc: spec
status: approved
---

# Agent Eval Harness — Technical Spec

## How This Works, In Plain Language
This project is a small evaluation loop for Python code-generation tasks. A user gives the harness a task, the harness runs an AI coding agent against that task in a temporary working directory, then it runs automated tests to see whether the code actually works. After the run completes, the harness turns the results into a requirement-by-requirement scorecard that shows which checks passed, which failed, and how many tokens were used.

The reason for this shape is that the learner wants to learn the structure of a real AI evaluation workflow without building a complicated platform. The tool stays local and simple: a Python CLI, a challenge schema, a task runner, automated evaluation, and a readable result summary. That keeps the proof of concept focused on the core idea — measuring whether an agent solved the task and at what cost.

The local workflow is simple to reason about:
1. The user enters a prompt or loads a challenge file.
2. The harness validates the input with Pydantic models.
3. It creates a fresh working directory and runs the agent command against it.
4. It runs pytest against the generated code or solution.
5. It records pass/fail evidence and token usage.
6. It prints a single summary showing the quality of the run and the cost of the run.

This is intentionally more transparent than a “black box AI app.” The user is learning how to monitor an agent’s work and judge the result using real evidence.

## The Core Journey Through the System
PRD ref: `prd.md > The Core Journey`.

The user starts at the harness CLI or local app entrypoint. The flow is:

1. The user chooses a prompt or challenge file.
2. The CLI validates the task definition using a schema model.
3. The harness creates a fresh sandbox folder and passes the task to the agent.
4. The agent writes or modifies Python files in that sandbox.
5. The harness runs automated evaluation against the sandboxed project.
6. The harness aggregates the results into a requirement-by-requirement pass/fail matrix.
7. The harness logs token usage from the agent run or a supplied telemetry file.
8. The user sees an output summary showing both the quality signal and the cost signal.

This path matches the PRD's core journey without adding multi-user or hosted infrastructure.

## Stack
- Python 3.11+
- `argparse` for CLI entrypoints
- `pydantic` for task and challenge validation
- `pytest` for automated evaluation
- `json` and optional `yaml` for challenge-file parsing
- `pathlib` and `tempfile` for sandboxed local execution
- `dataclasses` or simple Python models for internal run status and scoring

Rationale:
- Python is the learner’s comfort zone and fits the project goal.
- Pydantic keeps input validation explicit and easy to understand for a small proof of concept.
- pytest is the simplest and most recognizable way to validate Python code in a developer-facing harness.
- A terminal-first CLI keeps the system lightweight, measurable, and suitable for a short demo.

Anything unverified: YAML support is optional in the PoC; JSON is the default challenge format unless the learner wants to add YAML support early.

## Where It Runs and How Someone Tries It
This project runs locally on the learner's machine as a Python CLI. No deployment is required for the proof of concept. The required demo can be recorded by running the CLI locally and showing the output summary.

Exact start commands:

Quick prompt run:
```bash
python -m agent_eval --task "Fix the function so it handles empty input gracefully" --project ./sample_project
```

Challenge file run:
```bash
python -m agent_eval --challenge ./challenges/sample.json
```

Optional YAML challenge file run:
```bash
python -m agent_eval --challenge ./challenges/sample.yaml
```

What to open:
- The terminal output containing the pass/fail matrix and token summary.
- The generated sandbox directory for inspection if needed.

No API keys are required for the default PoC if the harness is pointed at a local agent script or local workflow. If the learner later adds a hosted model or external API connection, that would be recorded here as an additional dependency.

## Look and Feel
The product should feel like a technical utility, not a consumer app. The CLI output should be compact, structured, and fast to read. Each requirement row should be easy to scan, with clear pass/fail indicators and a total summary. On screen, the result should emphasize evidence: what passed, what failed, and the cost of the run.

The visual language is intentionally minimal: a terminal-first interface with headings, compact tables, and strong status cues. If a later local web view is added, it should keep the same developer utility aesthetic rather than becoming a dashboard-heavy product.

## Components

### CLI Entry Point
Responsible for parsing the user's task input, invoking the right workflow, and printing the final report. It is the public interface for the tool.
PRD ref: `prd.md > Task Setup and Run Control` and `prd.md > Metrics and Cost Visibility`.

### Challenge Schema and Validation
Defines the accepted task structure using Pydantic models. It validates required fields before the run starts and prevents malformed inputs from reaching the evaluation system.
PRD ref: `prd.md > Task Setup and Run Control`.

### Agent Runner
Creates a sandbox directory, copies task files into it, and invokes the local code-generation agent or script. It records the output and any generated file changes.
PRD ref: `prd.md > Live Transparency`.

### Evaluator
Runs the test suite or validation checks in the sandbox and returns a structured result for each requirement or check.
PRD ref: `prd.md > Automated Evaluation`.

### Metrics Collector
Captures token usage, run duration, pass/fail totals, and summary information. This is what turns a raw outcome into a scorecard.
PRD ref: `prd.md > Metrics and Cost Visibility`.

### Result Reporter
Formats the pass/fail matrix and summary metrics into a readable terminal report.
PRD ref: `prd.md > Automated Evaluation` and `prd.md > Metrics and Cost Visibility`.

## Data Model
The project will use a small set of clear Python models.

### ChallengeSpec
Represents a single task or evaluation bundle.
- `id`: unique identifier for the challenge
- `name`: human-readable name
- `prompt`: quick prompt for a single-task run
- `requirements`: list of requirement objects to be evaluated
- `expected_tests`: optional pytest targets or validation commands
- `token_budget`: optional limit used for reporting or comparison

### RequirementResult
Represents one requirement or evaluation row.
- `name`: requirement label
- `passed`: boolean
- `details`: human-readable explanation or error summary
- `evidence`: optional test output or files touched

### RunSummary
Represents the final output of a run.
- `status`: passed / failed / error
- `total_requirements`: integer
- `passed_count`: integer
- `failed_count`: integer
- `token_usage`: integer or optional float
- `duration_seconds`: float
- `result_rows`: list of `RequirementResult`

### AgentResult
Represents the output from the agent run.
- `stdout`: agent output captured during execution
- `stderr`: errors or warnings
- `files_changed`: list of modified files
- `working_dir`: sandbox path

The data is local to the run. It does not need a database for the PoC. It can be kept in memory and written to a JSON report file when the run completes.

## File Structure
```text
project/
├── agent_eval/                     # main package
│   ├── __init__.py
│   ├── __main__.py                 # CLI entry point
│   ├── cli.py                      # argparse wiring and run flow
│   ├── models.py                   # Pydantic schema and run result models
│   ├── challenge.py                # challenge loading and validation
│   ├── runner.py                   # sandbox and agent execution
│   ├── evaluator.py                # pytest or validation execution
│   ├── metrics.py                  # token usage and summary aggregation
│   ├── reporter.py                 # pass/fail matrix and console output
│   └── utils.py                    # filesystem and temporary dir helpers
├── challenges/                     # example challenge files
│   ├── sample.json
│   └── sample.yaml                 # optional if YAML support is added
├── sample_project/                 # demo Python project for evaluation
│   ├── app.py
│   ├── test_app.py
│   └── requirements.txt
├── devpost/                       # Devpost learning workspace
├── README.md
├── pyproject.toml                 # project config and dependencies
└── .gitignore
```

## External Services and Dependencies
This PoC intentionally avoids external services for the critical path. The only external dependency is the local Python environment and the test runner. If a real agent provider is added later, it would be a separate integration layer and should be treated as optional.

Current dependencies:
- Python standard library: built-in modules only for the initial PoC
- Pytest: used for validation
- Pydantic: used for schema validation
- Optional PyYAML: only if YAML challenge files are included in the first pass

No database, auth, payments, or hosted deployment are required for this version.

## Important Failure Modes
- **Agent run fails before code is written** → the harness shows a clear failure status and includes the stderr output so the user can understand what broke.
- **Challenge file is invalid** → the CLI exits early with a validation error and lists the field that failed to satisfy the schema.
- **Tests fail after the agent run** → the harness marks each requirement as failed, keeps the test output, and still prints the summary metrics.
- **Token telemetry is missing** → the harness runs without crashing and shows a warning that usage data is unavailable for that run.

## What Was Simplified and Why
- **Local file-based evaluation instead of a hosted benchmark service** — the project is meant to prove the evaluation loop and the scorecard, not to build a cloud analytics platform.
- **Terminal-first reporting instead of a full web dashboard** — the learner wants visibility and structure, not a polished product interface, and the terminal is the fastest valid way to prove the idea.
- **Challenge files as JSON-first, with optional YAML later** — JSON is the simplest valid input format for a small proof of concept, while YAML remains a later enhancement if needed.
- **No persistent history** — the proof of concept is about measuring one run clearly, not storing hundreds of benchmark histories.

## Decisions and Open Issues
Decisions made here:
- Chosen runtime: terminal-first Python CLI.
- Chosen stack: Python + Pydantic + pytest.
- Chosen input model: both quick prompt entry and challenge file support.
- Chosen result model: requirement-by-requirement scorecard with token usage summary.
- Chosen simplification: no database, no hosted services, and no deployment requirement for the PoC.

One genuine learner uncertainty discussed and clarified:
- The learner was unsure whether the tool should be terminal-only or a local web UI. After discussing the scope and learning goal, they chose terminal-first because the project is primarily about the harness workflow and proof of evidence, not the interface polish.

Open issues carried forward from the PRD:
- The final challenge file format should be chosen as JSON-first with optional YAML compatibility if the learner wants to expand it later.
- The exact reporting format of the token metrics can be finalized during implementation, but the product requirement is already clear: both correctness and cost must be visible.
