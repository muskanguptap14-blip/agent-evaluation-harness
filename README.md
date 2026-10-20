# Agent Eval Harness

A lightweight local Python CLI for evaluating code-generation tasks against automated tests and reporting pass/fail results with token-usage visibility.

## What it does

- Accepts either a quick prompt or a structured JSON challenge file
- Validates the task definition before running
- Creates a temporary sandboxed copy of the target project
- Runs pytest against the sandboxed code
- Produces a requirement-by-requirement pass/fail matrix
- Summarizes token usage and overall evaluation status

## Why this exists

This project is a proof-of-concept harness for developers who want a small, local way to compare AI-generated code against a test suite without needing a hosted service or UI-heavy workflow.

## Local run

```bash
python -m pip install -e .
python -m agent_eval --help
python -m agent_eval --challenge challenges/sample.json --project sample_project
```

## Project structure

- `agent_eval/` – CLI, validation models, runner, evaluator, and reporting
- `challenges/` – example challenge definitions
- `sample_project/` – local sample project used to verify the harness
- `devpost/` – planning and build artifacts

## Privacy note

The file `devpost/learner-profile.md` contains personal learning notes and is intentionally excluded from version control by default. Keep it private and do not publish it to a public repository.

## License

This project is provided as a local learning/prototype project.
