# Agent Eval Harness

A small, local Python command-line tool that runs a project's tests in a temporary copy and displays a clear evaluation summary.

## Try it in a few minutes

You will need **Python 3.11 or newer** and an internet connection for the one-time package installation.

### 1. Download the project

Choose either option:

- **Download ZIP:** Select the green **Code** button on this GitHub page, choose **Download ZIP**, then extract the downloaded file.
- **Use Git:** Open a terminal and run:

  ```bash
  git clone https://github.com/muskanguptap14-blip/agent-evaluation-harness.git
  cd agent-evaluation-harness
  ```

If you downloaded the ZIP, open a terminal in the extracted `agent-evaluation-harness` folder before continuing.

### 2. Install the project

Run these commands from the project folder:

```bash
python -m pip install -e .
```

On Windows, if `python` is not recognized, use the Python launcher instead:

```powershell
py -m pip install -e .
```

### 3. Run the sample evaluation

```bash
python -m agent_eval --challenge challenges/sample.json --project sample_project
```

On Windows, use `py` instead of `python` if needed:

```powershell
py -m agent_eval --challenge challenges/sample.json --project sample_project
```

You should see an output like this:

```text
Challenge: String cleaning challenge
Prompt: Improve the function so it cleans whitespace and handles empty input safely.
Requirements: 2
Project: sample_project

=== Evaluation Summary ===
Status: PASSED
Total requirements: 2
Passed: 2
Failed: 0
Token usage: 174
Duration: 0.00s

Requirement matrix:
- Whitespace cleanup: PASS — pytest passed
  Evidence: ..                                                                       [100%]
2 passed in 0.05s
- Empty input safety: PASS — pytest passed
  Evidence: ..                                                                       [100%]
2 passed in 0.05s
```

The exact duration and pytest timing may vary. The harness makes a temporary copy of the project, runs pytest there, and removes the temporary copy when the run ends.

### 4. See the available options

```bash
python -m agent_eval --help
```

You can also provide a one-off task:

```bash
python -m agent_eval --task "Check the sample project" --project sample_project
```

## What this proof of concept does

- Accepts a quick task or a JSON challenge file
- Runs pytest against the chosen local Python project in a temporary copy
- Displays the overall test result, requirement rows, and test output

**Current limitation:** this proof of concept evaluates a project that already exists; it does not call an AI model or generate code. All requirement rows currently reflect the overall pytest result, rather than running a separate test for each requirement. The displayed token-usage value is an estimate from the available text, not usage reported by an AI provider.

## Project layout

- `agent_eval/` - CLI, challenge validation, test runner, and report
- `challenges/` - sample JSON challenge
- `sample_project/` - small project used for the sample run
- `devpost/` - project planning and build artifacts

## Privacy

Personal learner-profile notes are not included in this public repository.
