from __future__ import annotations

import argparse
from pathlib import Path

from .challenge import load_challenge
from .evaluator import evaluate_challenge
from .models import ChallengeSpec, Requirement
from .reporter import print_summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate agent-generated Python code against local checks.")
    parser.add_argument("--task", help="One-off prompt for a quick run.")
    parser.add_argument("--challenge", help="Path to a JSON challenge file.")
    parser.add_argument("--project", help="Path to the Python project to evaluate.", default="sample_project")
    return parser


def build_quick_prompt(task: str) -> ChallengeSpec:
    return ChallengeSpec(
        name="Quick prompt",
        prompt=task,
        requirements=[
            Requirement(
                name="Prompt accepted",
                description=task,
                check="prompt-valid",
            )
        ],
        expected_tests=[],
        token_budget=2500,
    )


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.challenge:
        challenge = load_challenge(Path(args.challenge))
    elif args.task:
        challenge = build_quick_prompt(args.task)
    else:
        parser.error("Either --task or --challenge is required.")

    project_path = Path(args.project)
    summary = evaluate_challenge(challenge, project_path)

    print(f"Challenge: {challenge.name}")
    print(f"Prompt: {challenge.prompt}")
    print(f"Requirements: {len(challenge.requirements)}")
    print(f"Project: {project_path}")
    print_summary(summary)
    return 0
