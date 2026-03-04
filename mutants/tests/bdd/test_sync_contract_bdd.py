"""BDD tests for Python/C++ numeric equivalence — driven by features/sync_contract.feature."""

import json
import os
import subprocess
import sys
import tempfile

import pytest
from pytest_bdd import given, when, then, scenarios, parsers

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FEATURE_FILE   = os.path.join(REPO_ROOT, "features", "sync_contract.feature")
INPUT_FILE     = os.path.join(REPO_ROOT, "inputs.jsonl")
CPP_BINARY     = os.path.join(REPO_ROOT, "cpp", "run_cpp")
PY_SCRIPT      = os.path.join(REPO_ROOT, "py", "run_py.py")
COMPARE_SCRIPT = os.path.join(REPO_ROOT, "tools", "compare.py")

# ── Pre-load inputs index ──────────────────────────────────────────────────────

def _load_inputs():
    cases = []
    with open(INPUT_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases

_INPUTS = _load_inputs()

# ── Session fixture: build C++ once ───────────────────────────────────────────

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
            pytest.fail(
                f"C++ build failed:\nstdout: {result.stdout}\nstderr: {result.stderr}"
            )
    assert os.path.isfile(CPP_BINARY), f"Binary not found after build: {CPP_BINARY}"

# ── Shared scenario context ────────────────────────────────────────────────────

@pytest.fixture
def ctx():
    """Per-scenario mutable context shared across step definitions."""
    return {}

# ── Bind all scenarios from the feature file ──────────────────────────────────

scenarios(FEATURE_FILE)

# ── Step definitions ───────────────────────────────────────────────────────────

@given(
    "the normalization contract uses IEEE 754 double-precision with 16 decimal places and ROUND_HALF_EVEN"
)
def normalization_contract():
    """Background step — normalization rules are enforced by compare.py."""


@given(parsers.re(r"the inputs a=(?P<a>[^,]+), b=(?P<b>[^,]+), c=(?P<c>.+)"))
def the_inputs(a, b, c, ctx):
    """Locate the matching case in inputs.jsonl and write a single-case temp file."""
    a_f, b_f, c_f = float(a), float(b), float(c)

    record = next(
        (
            r for r in _INPUTS
            if float(r["a"]) == a_f
            and float(r["b"]) == b_f
            and float(r["c"]) == c_f
        ),
        None,
    )
    assert record is not None, (
        f"No case found in inputs.jsonl for a={a}, b={b}, c={c}"
    )

    tmp = tempfile.mkdtemp()
    input_path = os.path.join(tmp, "input.jsonl")
    with open(input_path, "w") as f:
        json.dump(record, f)
        f.write("\n")

    ctx["case_id"]    = record["case_id"]
    ctx["input_path"] = input_path
    ctx["out_py"]     = os.path.join(tmp, "out_py.jsonl")
    ctx["out_cpp"]    = os.path.join(tmp, "out_cpp.jsonl")


@when("Python evaluates (a + b) * c")
def python_evaluates(ctx):
    """Run the Python implementation against the single-case input file."""
    result = subprocess.run(
        [sys.executable, PY_SCRIPT, ctx["input_path"], ctx["out_py"]],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Python run failed for {ctx['case_id']}:\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


@when("C++ evaluates (a + b) * c")
def cpp_evaluates(ctx):
    """Run the C++ implementation against the single-case input file."""
    result = subprocess.run(
        [CPP_BINARY, ctx["input_path"], ctx["out_cpp"]],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"C++ run failed for {ctx['case_id']}:\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


@then("the normalized outputs of Python and C++ are equal")
def normalized_outputs_equal(ctx):
    """Invoke compare.py and assert both outputs normalize to the same value."""
    result = subprocess.run(
        [sys.executable, COMPARE_SCRIPT, ctx["out_py"], ctx["out_cpp"]],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.fail(
            f"compare.py found differences for {ctx['case_id']} "
            f"(exit {result.returncode}):\n"
            f"{result.stdout}\n{result.stderr}"
        )
