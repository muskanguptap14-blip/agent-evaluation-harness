from __future__ import annotations

from .models import RunSummary


def print_summary(summary: RunSummary) -> None:
    print("\n=== Evaluation Summary ===")
    print(f"Status: {summary.status.upper()}")
    print(f"Total requirements: {summary.total_requirements}")
    print(f"Passed: {summary.passed_count}")
    print(f"Failed: {summary.failed_count}")
    print(f"Token usage: {summary.token_usage}")
    print(f"Duration: {summary.duration_seconds:.2f}s")
    print("\nRequirement matrix:")
    for row in summary.result_rows:
        status = "PASS" if row.passed else "FAIL"
        print(f"- {row.name}: {status} — {row.details}")
        if row.evidence:
            print(f"  Evidence: {row.evidence}")
