from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Requirement(BaseModel):
    name: str
    description: str
    check: Optional[str] = None


class ChallengeSpec(BaseModel):
    name: str = Field(default="Challenge")
    prompt: str
    requirements: List[Requirement] = Field(default_factory=list)
    expected_tests: List[str] = Field(default_factory=list)
    token_budget: int = 2500


class RequirementResult(BaseModel):
    name: str
    passed: bool
    details: str = ""
    evidence: Optional[str] = None


class RunSummary(BaseModel):
    status: str
    total_requirements: int
    passed_count: int
    failed_count: int
    token_usage: int
    duration_seconds: float
    result_rows: List[RequirementResult]
