"""Mutation-targeted unit tests for tools.compare.normalize.

Each test is designed to kill one or more specific mutants that mutmut may
introduce into the normalize function.  The table below maps test groups to
the mutation operators they target:

  Test group                         Targeted mutations
  ─────────────────────────────────  ──────────────────────────────────────────
  Return-value exactness             String literal mutations on "NaN", "+Inf",
                                     "-Inf" (XX-wrap, case-swap)
  String-encoded special values      Mutations of comparison string literals
                                     inside the lower-in-(...) checks
  Unparseable handling               Mutation of "UNPARSABLE:" prefix literal
  Exactly 16 decimal places          Number mutation 16 → 17 or 16 → 15 in
                                     "0" * 16
  Negative-zero normalization        Operator mutation == → != on (d == 0)
  Rounding mode                      Arg-removal of rounding=ROUND_HALF_EVEN
                                     from quantize call
  Regular-number canonical form      Assignment mutation d = d.quantize() → None
  Idempotency                        All of the above combined (second pass)
  Sign correctness                   Operator mutation > → >= in inf-sign branch
"""

import pytest

from tools.compare import normalize


# ─────────────────────────────────────────────────────────────────────────────
# Return-value exactness
# Kills string mutations on the three special return literals:
#   "NaN"  → "XXNaNXX", "nan", "NAN"
#   "+Inf" → "XX+InfXX", "+inf", "+INF"
#   "-Inf" → "XX-InfXX", "-inf", "-INF"
# ─────────────────────────────────────────────────────────────────────────────

def test_nan_return_exact():
    assert normalize(float("nan")) == "NaN"


def test_positive_inf_return_exact():
    assert normalize(float("inf")) == "+Inf"


def test_negative_inf_return_exact():
    assert normalize(float("-inf")) == "-Inf"


# ─────────────────────────────────────────────────────────────────────────────
# Sign distinction on infinities
# Kills operator mutation > → >= on the `value > 0` branch.
# +inf and -inf must never normalize to the same string.
# ─────────────────────────────────────────────────────────────────────────────

def test_inf_sign_never_equal():
    assert normalize(float("inf")) != normalize(float("-inf"))


def test_positive_inf_has_plus_prefix():
    assert normalize(float("inf")).startswith("+")


def test_negative_inf_has_minus_prefix():
    assert normalize(float("-inf")).startswith("-")


# ─────────────────────────────────────────────────────────────────────────────
# String-encoded special values
# Kills mutations of the comparison string literals inside the
# `lower in (...)` checks, including case-swap of .lower() → .upper().
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("raw", ["nan", "NaN", "NAN", "Nan"])
def test_string_nan_all_cases(raw):
    assert normalize(raw) == "NaN"


@pytest.mark.parametrize("raw", [
    "+inf", "inf", "infinity", "+infinity",
    "+Inf", "Inf", "Infinity", "+Infinity", "+INFINITY",
])
def test_string_positive_inf_all_cases(raw):
    assert normalize(raw) == "+Inf"


@pytest.mark.parametrize("raw", ["-inf", "-infinity", "-Inf", "-Infinity", "-INFINITY"])
def test_string_negative_inf_all_cases(raw):
    assert normalize(raw) == "-Inf"


# ─────────────────────────────────────────────────────────────────────────────
# Unparseable input
# Kills mutations of the "UNPARSABLE:" prefix literal
# (e.g. "XXUNPARSABLE:XX", "unparsable:").
# ─────────────────────────────────────────────────────────────────────────────

def test_unparseable_exact_output():
    assert normalize("not_a_number") == "UNPARSABLE:not_a_number"


def test_unparseable_prefix_is_uppercase():
    result = normalize("xyz")
    assert result.startswith("UNPARSABLE:")
    assert not result.startswith("unparsable:")
    assert not result.startswith("XXUNPARSABLE:")


def test_unparseable_preserves_original_value():
    assert normalize("hello world") == "UNPARSABLE:hello world"


# ─────────────────────────────────────────────────────────────────────────────
# Exactly 16 decimal places
# Kills number mutation 16 → 17 (or 15) in `"0" * 16`.
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("value, expected", [
    (1,     "1.0000000000000000"),
    (0,     "0.0000000000000000"),
    (-1,    "-1.0000000000000000"),
    (42,    "42.0000000000000000"),
    (0.5,   "0.5000000000000000"),
    (-0.5,  "-0.5000000000000000"),
    (100,   "100.0000000000000000"),
])
def test_exactly_16_decimal_places(value, expected):
    result = normalize(value)
    assert result == expected
    assert len(result.split(".")[1]) == 16


# ─────────────────────────────────────────────────────────────────────────────
# Negative-zero normalization
# Kills operator mutation == → != on the `if d == 0` guard that converts
# Decimal negative-zero to positive zero.
# ─────────────────────────────────────────────────────────────────────────────

def test_negative_zero_becomes_positive_zero():
    """Core kill: with == → !=, -0.0 would return "-0.0000000000000000"."""
    result = normalize(-0.0)
    assert result == "0.0000000000000000"
    assert not result.startswith("-")


def test_positive_zero_unchanged():
    assert normalize(0.0) == "0.0000000000000000"


def test_negative_zero_string_input():
    """String "-0.0" must also normalize to positive zero."""
    assert normalize("-0.0") == "0.0000000000000000"
    assert not normalize("-0.0").startswith("-")


# ─────────────────────────────────────────────────────────────────────────────
# Rounding mode (ROUND_HALF_EVEN / banker's rounding)
# Kills arg-removal mutation that drops rounding=ROUND_HALF_EVEN from the
# quantize call, which would fall back to the context default (ROUND_UP in
# some environments) and give wrong results at half-way points.
# ─────────────────────────────────────────────────────────────────────────────

def test_half_even_rounds_to_even_zero():
    """5e-17 is exactly 0.5 × 1e-16; ROUND_HALF_EVEN rounds to 0 (even)."""
    assert normalize(5e-17) == "0.0000000000000000"


def test_half_even_rounds_to_even_two():
    """2.5e-16 is exactly 2.5 × 1e-16; ROUND_HALF_EVEN rounds to 2 (even)."""
    assert normalize(2.5e-16) == "0.0000000000000002"


def test_representation_error_rounds_to_16_dp():
    """0.1 + 0.2 = 0.30000000000000004 in float; rounds to 0.3000000000000000."""
    assert normalize(0.1 + 0.2) == "0.3000000000000000"


# ─────────────────────────────────────────────────────────────────────────────
# Regular-number canonical form
# Kills assignment mutation d = d.quantize(...) → d = None (would raise TypeError).
# Also ensures the decimal format string is correct.
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("value, expected", [
    (1e15,   "1000000000000000.0000000000000000"),
    (1e-10,  "0.0000000001000000"),
    (-1.5,   "-1.5000000000000000"),
    (0.3,    "0.3000000000000000"),
    (999.0,  "999.0000000000000000"),
    (-3,     "-3.0000000000000000"),
    (3,      "3.0000000000000000"),
])
def test_regular_numbers_canonical_form(value, expected):
    assert normalize(value) == expected


# ─────────────────────────────────────────────────────────────────────────────
# Idempotency
# Already-normalized strings must pass through unchanged.
# Kills any mutation that makes the string path diverge from the float path.
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("value", [
    "NaN",
    "+Inf",
    "-Inf",
    "0.0000000000000000",
    "1.0000000000000000",
    "-1.5000000000000000",
    "999.0000000000000000",
    "1000000000000000.0000000000000000",
])
def test_idempotency(value):
    assert normalize(value) == value


# ─────────────────────────────────────────────────────────────────────────────
# Cross-category sanity checks
# Ensures special values are never confused with each other.
# ─────────────────────────────────────────────────────────────────────────────

def test_nan_is_not_inf():
    assert normalize(float("nan")) != "+Inf"
    assert normalize(float("nan")) != "-Inf"


def test_inf_is_not_nan():
    assert normalize(float("inf")) != "NaN"
    assert normalize(float("-inf")) != "NaN"


def test_zero_is_not_special():
    assert normalize(0.0) != "NaN"
    assert normalize(0.0) != "+Inf"
    assert normalize(0.0) != "-Inf"
