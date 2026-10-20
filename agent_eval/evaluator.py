from __future__ import annotations

from pathlib import Path

from .models import ChallengeSpec, RequirementResult, RunSummary
from .runner import run_pytest


def evaluate_challenge(challenge: ChallengeSpec, project_path: str | Path) -> RunSummary:
    exit_code, stdout, stderr = run_pytest(project_path)

    rows = []
    requirements = challenge.requirements or [{"name": "Challenge requirement", "description": challenge.prompt}]

    for requirement in requirements:
        passed = exit_code == 0
        details = "pytest passed" if passed else "pytest failed"
        rows.append(
            RequirementResult(
                name=requirement["name"] if isinstance(requirement, dict) else requirement.name,
                passed=passed,
                details=details,
                evidence=(stdout.strip() or stderr.strip())[:300],
            )
        )

    summary = RunSummary(
        status="passed" if exit_code == 0 else "failed",
        total_requirements=len(rows),
        passed_count=sum(1 for row in rows if row.passed),
        failed_count=sum(1 for row in rows if not row.passed),
        token_usage=max(1, len(challenge.prompt) + len(stdout) + len(stderr) // 3),
        duration_seconds=0.0,
        result_rows=rows,
    )
    return summary
