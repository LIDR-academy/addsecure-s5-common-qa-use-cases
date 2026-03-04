# Mutation Testing

## What is mutation testing?

Mutation testing is a technique for evaluating the quality of a test suite.
The tool — in this project, **mutmut** — automatically introduces small,
deliberate defects (_mutants_) into the production code and then runs the
existing test suite against each modified version.

A **mutant** is a copy of the source file with exactly one change applied, for
example:

| Original code | Mutant |
|---|---|
| `return "NaN"` | `return "XXNaNXX"` |
| `if value > 0` | `if value >= 0` |
| `"0" * 16` | `"0" * 17` |
| `if d == 0` | `if d != 0` |

The goal is to see whether the tests _notice_ each change.

* **Killed** — at least one test failed when the mutant was active. The test
  suite detected the defect. ✅
* **Survived** — all tests still passed despite the mutation. The defect went
  unnoticed. ❌  This is a signal that the tests are not asserting something
  they should.

The ratio `killed / total` is the **mutation score**. A higher score means a
more effective test suite.

---

## Scope

Mutations are restricted to the `normalize()` function in `tools/compare.py`.
This is configured in `setup.cfg`:

```ini
[mutmut]
paths_to_mutate = tools/compare.py
tests_dir       = tests/unit/test_normalize_mutation.py
```

Only `test_normalize_mutation.py` is run against each mutant, keeping
execution fast and the feedback focused.

---

## How to run locally

### Prerequisites

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run mutation testing

```bash
make mutate
```

This runs `mutmut run`, which:

1. Instruments `tools/compare.py` with trampolines for every generated mutant.
2. Executes `tests/unit/test_normalize_mutation.py` once per mutant.
3. Records whether the test suite killed or survived each mutant under
   `mutants/tools/compare.py.meta`.

The first run also collects stats (which tests cover which functions) before
testing mutants, so it may take a moment to start.

### View a plain-text summary

```bash
# Survived mutants only (the ones that need attention)
mutmut results

# All mutants (killed + survived)
mutmut results --all True
```

### Inspect a specific mutant diff

```bash
mutmut show <mutant-name>
# e.g. mutmut show normalize__mutmut_3
```

### Generate the HTML report

```bash
make mutate-html
```

Opens `mutation_report.html` at the repo root. The report shows:

* A summary card for total / killed / survived / skipped counts.
* The mutation score as a percentage.
* A per-mutant table with status, duration, and — for survived mutants — the
  exact code diff so you can see what was changed.

### Clean up cached files

```bash
make mutate-clean
```

Removes the `mutants/` directory and `.mutmut-cache`. Run this before a fresh
mutation run if the source code has changed significantly.

---

## Interpreting results

| Status | Meaning | Action required? |
|---|---|---|
| **Killed** 🎉 | Test suite detected the mutation. | No |
| **Survived** 🙁 | Mutation went undetected. | Yes — see below |
| **No tests** 🫥 | No test covers the mutated line. | Yes — add coverage |
| **Skipped** 🔇 | Mutant was excluded (e.g. by pragma). | No |
| **Timeout** ⏰ | Test run exceeded the time limit. | Investigate |
| **Suspicious** 🤔 | Unexpected exit code. | Investigate |

---

## What to do when a mutant survives

A surviving mutant means the test suite did not assert the specific behaviour
that was changed. Use `mutmut show <name>` to see the exact diff, then follow
the steps below.

### 1 — Read the diff carefully

Identify _what_ was changed and _what observable output_ that change would
produce if it were a real bug.

```diff
-    return "+Inf" if value > 0 else "-Inf"
+    return "+Inf" if value >= 0 else "-Inf"
```

In this example, the mutation would affect a value of exactly `0` on the
`isinf` path — but `0` is never infinite, so the branch is unreachable and the
mutant is **equivalent** (see below).

### 2 — Strengthen the assertion

If the mutant _is_ reachable, write a test that:

* Passes a concrete input that exercises the mutated line.
* Asserts the **exact** expected output, not just "it doesn't crash".

```python
# Weak — does not kill string mutations on the return value
def test_positive_inf():
    result = normalize(float("inf"))
    assert result is not None          # ❌ survived by "XXNaNXX" mutant

# Strong — exact match kills every string mutation
def test_positive_inf():
    assert normalize(float("inf")) == "+Inf"   # ✅
```

### 3 — Cover boundary conditions

Many mutants survive because tests only cover the "happy path". Add tests for:

* Half-way rounding values (`5e-17`, `2.5e-16`) to catch rounding-mode
  mutations.
* Both `+0.0` and `-0.0` to catch `== 0` → `!= 0` mutations.
* All case variants of string inputs (`"nan"`, `"NaN"`, `"NAN"`) to catch
  string-literal mutations.
* Exact string equality (`assert result == "NaN"`) instead of partial checks
  (`assert "N" in result`) to catch XX-wrap mutations.

### 4 — Accept equivalent mutants

Some mutations produce **equivalent mutants** — code that looks different but
behaves identically for all possible inputs. Common examples in `normalize()`:

* `value > 0` → `value >= 0` inside `if math.isinf(value)`: no finite value
  is `0` and also infinite, so the two conditions are indistinguishable.
* Removing `rounding=ROUND_HALF_EVEN` when the Decimal context already
  defaults to `ROUND_HALF_EVEN`.

Equivalent mutants cannot be killed by any test. They should be documented and
accepted rather than worked around with artificial test inputs.

### 5 — Re-run after adding tests

```bash
make mutate-clean   # clear old cache
make mutate         # re-run from scratch
make mutate-html    # refresh the report
```
