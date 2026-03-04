"""Unit tests for tools.compare.normalize — explicit cases for the normalization contract."""

import pytest

from tools.compare import normalize


# 1) apply rounding to 16 decimal places
def test_float_addition_rounding():
    # In Python, 0.1 + 0.2 == 0.30000000000000004
    # After normalization to 16 decimals: "0.3000000000000000"
    result = normalize(0.1 + 0.2)
    assert result == "0.3000000000000000"


# 2) -0.0 -> "0.0000000000000000"
def test_negative_zero():
    assert normalize(-0.0) == "0.0000000000000000"


# 3) NaN -> "NaN"
def test_nan():
    assert normalize(float("nan")) == "NaN"


# 4) +Inf -> "+Inf"
def test_positive_inf():
    assert normalize(float("inf")) == "+Inf"


# 5) -Inf -> "-Inf"
def test_negative_inf():
    assert normalize(float("-inf")) == "-Inf"


# 6) Idempotency: normalize(normalize(x)) == normalize(x)
IDEMPOTENCE_VALUES = [
    0.0,
    -0.0,
    1.0,
    -1.5,
    0.1 + 0.2,
    1e15,
    1e-10,
    42,
    0.3,
    999.999,
]


@pytest.mark.parametrize("value", IDEMPOTENCE_VALUES, ids=[str(v) for v in IDEMPOTENCE_VALUES])
def test_idempotence(value):
    once = normalize(value)
    twice = normalize(once)
    assert twice == once, (
        f"Not idempotent: normalize({value!r}) = {once!r}, "
        f"normalize({once!r}) = {twice!r}"
    )
