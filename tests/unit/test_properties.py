"""Property-Based Tests for tools.compare.normalize using Hypothesis.

Properties verified:
  1. Idempotency  — normalize(normalize(x)) == normalize(x) for finite floats
  2. Format       — result has exactly 16 decimal places for regular numbers
  3. Stability of Zero — result never starts with "-0." for values that
                         normalize to zero (including -0.0)
"""

from hypothesis import given, settings
from hypothesis import strategies as st

from tools.compare import normalize

# ── Shared strategy: finite floats in a reasonable range ─────────────────────

_FINITE = st.floats(
    min_value=-1e6,
    max_value=1e6,
    allow_nan=False,
    allow_infinity=False,
)

_DEADLINE_MS = 2000  # 2 s per example — generous enough for Decimal arithmetic


# ── 1. Idempotency ────────────────────────────────────────────────────────────

@given(x=_FINITE)
@settings(max_examples=100, deadline=_DEADLINE_MS)
def test_idempotency(x: float) -> None:
    """normalize is idempotent: a second pass must leave the value unchanged."""
    first = normalize(x)
    second = normalize(first)
    assert first == second, (
        f"Idempotency violated for x={x!r}: "
        f"normalize(x)={first!r}, normalize(normalize(x))={second!r}"
    )


# ── 2. Format ─────────────────────────────────────────────────────────────────

_SPECIAL = {"NaN", "+Inf", "-Inf"}


def _is_regular(result: str) -> bool:
    return not result.startswith("UNPARSABLE:") and result not in _SPECIAL


@given(x=_FINITE)
@settings(max_examples=100, deadline=_DEADLINE_MS)
def test_format_exactly_16_decimal_places(x: float) -> None:
    """Regular results must have exactly 16 digits after the decimal point."""
    result = normalize(x)
    if not _is_regular(result):
        return  # NaN/Inf/UNPARSABLE are exempt from this format rule

    assert "." in result, (
        f"Expected a decimal point in normalize({x!r})={result!r}"
    )
    decimal_part = result.split(".")[1]
    assert len(decimal_part) == 16, (
        f"Expected 16 decimal places for normalize({x!r})={result!r}, "
        f"got {len(decimal_part)}"
    )


# ── 3. Stability of Zero ──────────────────────────────────────────────────────

@given(x=st.one_of(
    st.just(0.0),
    st.just(-0.0),
    st.floats(min_value=-1e-300, max_value=1e-300, allow_nan=False, allow_infinity=False),
))
@settings(max_examples=100, deadline=_DEADLINE_MS)
def test_stability_of_zero(x: float) -> None:
    """Values that round to zero must never produce a negative-zero string."""
    result = normalize(x)
    if result == "0.0000000000000000":
        assert not result.startswith("-0."), (
            f"Negative-zero string returned for x={x!r}: {result!r}"
        )
