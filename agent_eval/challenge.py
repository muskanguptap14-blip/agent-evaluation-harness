from __future__ import annotations

import json
from pathlib import Path

from .models import ChallengeSpec


def load_challenge(path: str | Path) -> ChallengeSpec:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "requirements" in data and data["requirements"] and isinstance(data["requirements"][0], str):
        data["requirements"] = [
            {"name": f"Requirement {index + 1}", "description": item}
            for index, item in enumerate(data["requirements"])
        ]
    return ChallengeSpec.model_validate(data)
