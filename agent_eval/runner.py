from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Tuple


def prepare_project(project_path: str | Path, sandbox_dir: Path) -> None:
    src = Path(project_path)
    if not src.exists():
        raise FileNotFoundError(f"Project directory not found: {src}")
    shutil.copytree(src, sandbox_dir, dirs_exist_ok=True)


def run_pytest(project_path: str | Path) -> Tuple[int, str, str]:
    with TemporaryDirectory(prefix="agent_eval_") as tmpdir:
        sandbox = Path(tmpdir)
        prepare_project(project_path, sandbox)
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=sandbox,
            capture_output=True,
            text=True,
        )
        return proc.returncode, proc.stdout, proc.stderr
