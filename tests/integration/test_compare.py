"""Integration test: compile C++, run both implementations, compare outputs."""

import os
import subprocess
import sys

import pytest

# All paths relative to repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUT_FILE = os.path.join(REPO_ROOT, "inputs.jsonl")
OUT_PY = os.path.join(REPO_ROOT, "out_py.jsonl")
OUT_CPP = os.path.join(REPO_ROOT, "out_cpp.jsonl")
CPP_BINARY = os.path.join(REPO_ROOT, "cpp", "run_cpp")
PY_SCRIPT = os.path.join(REPO_ROOT, "py", "run_py.py")
COMPARE_SCRIPT = os.path.join(REPO_ROOT, "tools", "compare.py")


@pytest.fixture(scope="session", autouse=True)
def build_cpp():
    """Compile the C++ binary via Makefile if it does not exist."""
    if not os.path.isfile(CPP_BINARY):
        result = subprocess.run(
            ["make", "build"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            pytest.fail(f"C++ build failed:\nstdout: {result.stdout}\nstderr: {result.stderr}")
    assert os.path.isfile(CPP_BINARY), f"Binary not found after build: {CPP_BINARY}"


def test_compare():
    """Run Python, run C++, then compare outputs."""
    # 1) Run Python implementation
    result_py = subprocess.run(
        [sys.executable, PY_SCRIPT, INPUT_FILE, OUT_PY],
        capture_output=True,
        text=True,
    )
    assert result_py.returncode == 0, (
        f"Python run failed (exit {result_py.returncode}):\n"
        f"stdout: {result_py.stdout}\nstderr: {result_py.stderr}"
    )

    # 2) Run C++ implementation
    result_cpp = subprocess.run(
        [CPP_BINARY, INPUT_FILE, OUT_CPP],
        capture_output=True,
        text=True,
    )
    assert result_cpp.returncode == 0, (
        f"C++ run failed (exit {result_cpp.returncode}):\n"
        f"stdout: {result_cpp.stdout}\nstderr: {result_cpp.stderr}"
    )

    # 3) Compare outputs
    result_cmp = subprocess.run(
        [sys.executable, COMPARE_SCRIPT, OUT_PY, OUT_CPP],
        capture_output=True,
        text=True,
    )
    if result_cmp.returncode != 0:
        pytest.fail(
            f"compare.py found differences (exit {result_cmp.returncode}):\n"
            f"{result_cmp.stdout}\n{result_cmp.stderr}"
        )
