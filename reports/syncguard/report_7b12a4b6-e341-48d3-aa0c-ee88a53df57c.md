# SyncGuard Report — unit — 2026-03-08

## Summary

The `unit` suite was run via `make unit-test` (76 tests). On the first run, 18 tests failed — all related to the `normalize` function in `tools/compare.py` not producing 16-decimal-place output. A single-line fix was applied (restoring a deleted `quantize` call). The second run passed all 76 tests. Total iterations: 2.

## Root Cause

In `tools/compare.py`, inside the `normalize` function (line ~54), the line:

```python
d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)
```

had been deleted from within the `with localcontext() as ctx:` block. This is the only step that rounds the `Decimal` value to exactly 16 decimal places using banker's rounding. Without it, `format(d, 'f')` returned the raw, unquantized string representation (e.g., `"1"` instead of `"1.0000000000000000"`, `"0.30000000000000004"` instead of `"0.3000000000000000"`).

The `git diff` before the fix showed exactly one deleted line confirming this.

## Fix Applied

**File:** `tools/compare.py`
**Location:** inside `normalize()`, within the `with localcontext() as ctx:` block (line 55)

Before:
```python
    with localcontext() as ctx:
        ctx.prec = 50

    # Normalize -0 to 0
```

After:
```python
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0
```

Change: restored the single `d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)` line that was accidentally removed. No other lines were touched.

## Evidence

### Before (first run — 18 failures, representative samples)

```
FAILED unit/test_normalize.py::test_float_addition_rounding
  AssertionError: assert '0.30000000000000004' == '0.3000000000000000'

FAILED unit/test_normalize_mutation.py::test_exactly_16_decimal_places[1-1.0000000000000000]
  AssertionError: assert '1' == '1.0000000000000000'

FAILED unit/test_normalize_mutation.py::test_half_even_rounds_to_even_zero
  AssertionError: assert '0.00000000000000005' == '0.0000000000000000'

FAILED unit/test_properties.py::test_format_exactly_16_decimal_places
  AssertionError: Expected 16 decimal places for normalize(1.0)='1.0', got 1
```

### After (second run — all passing)

```
============================== 76 passed in 0.21s ==============================
RESULT  : PASS
Command : make unit-test
```

## Risks

No known risks identified. The restored line re-enables the exact behaviour the rest of the codebase and all tests depend on. The `localcontext()` block with `prec=50` ensures the quantize operation has sufficient precision and does not affect any other code path. The fix is a pure restoration of deleted code — no new logic was introduced.

## Next Steps

- Review git history to understand how the `quantize` line was deleted (accidental edit, incomplete merge, or intentional change that was later reverted). Ensure CI protects this suite going forward.
- Consider adding the unit suite to a pre-commit hook so regressions are caught before they reach the branch.
- No further code changes are required.
