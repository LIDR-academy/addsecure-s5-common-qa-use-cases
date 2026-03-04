#!/usr/bin/env python3
"""Compare out_py.jsonl vs out_cpp.jsonl using normalized values.

Normalization contract v1:
  - NaN  -> "NaN"
  - +Inf -> "+Inf",  -Inf -> "-Inf"
  - -0.0 -> "0.0000000000000000"
  - Numbers: Decimal with 16 decimal places, ROUND_HALF_EVEN

Exit code 0 if all cases match, 1 if any differ.
"""

import argparse
import json
import math
import sys
from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation, localcontext
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def normalize(value):
    args = [value]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_normalize__mutmut_orig, x_normalize__mutmut_mutants, args, kwargs, None)


def x_normalize__mutmut_orig(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_1(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(None):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_2(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "XXNaNXX"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_3(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "nan"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_4(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NAN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_5(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(None):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_6(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "XX+InfXX" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_7(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_8(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+INF" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_9(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value >= 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_10(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 1 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_11(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "XX-InfXX"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_12(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_13(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-INF"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_14(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = None

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_15(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(None).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_16(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = None
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_17(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.upper()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_18(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower != "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_19(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "XXnanXX":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_20(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "NAN":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_21(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "XXNaNXX"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_22(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "nan"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_23(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NAN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_24(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower not in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_25(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("XX+infXX", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_26(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+INF", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_27(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "XXinfXX", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_28(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "INF", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_29(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "XXinfinityXX", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_30(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "INFINITY", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_31(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "XX+infinityXX"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_32(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+INFINITY"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_33(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "XX+InfXX"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_34(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_35(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+INF"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_36(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower not in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_37(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("XX-infXX", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_38(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-INF", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_39(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "XX-infinityXX"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_40(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-INFINITY"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_41(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "XX-InfXX"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_42(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_43(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-INF"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_44(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = None
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_45(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(None)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_46(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "XXNaNXX"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_47(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "nan"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_48(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NAN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_49(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "XX+InfXX" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_50(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_51(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+INF" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_52(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d >= 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_53(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 1 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_54(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "XX-InfXX"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_55(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_56(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-INF"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_57(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = None
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_58(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal(None)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_59(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." - "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_60(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("XX1.XX" + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_61(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" / 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_62(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "XX0XX" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_63(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 17)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_64(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = None
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_65(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 51
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_66(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = None

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_67(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(None, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_68(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=None)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_69(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_70(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, )

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_71(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d != 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_72(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 1:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_73(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = None

    return format(d, 'f')


def x_normalize__mutmut_74(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(None)

    return format(d, 'f')


def x_normalize__mutmut_75(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal(None).quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_76(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("XX0XX").quantize(quantize_exp)

    return format(d, 'f')


def x_normalize__mutmut_77(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(None, 'f')


def x_normalize__mutmut_78(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, None)


def x_normalize__mutmut_79(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format('f')


def x_normalize__mutmut_80(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, )


def x_normalize__mutmut_81(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'XXfXX')


def x_normalize__mutmut_82(value):
    """Normalize a raw value to a canonical string for comparison."""
    # Handle float NaN / Inf directly
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "+Inf" if value > 0 else "-Inf"

    s = str(value).strip()

    # Handle string-encoded special values (case-insensitive)
    lower = s.lower()
    if lower == "nan":
        return "NaN"
    if lower in ("+inf", "inf", "infinity", "+infinity"):
        return "+Inf"
    if lower in ("-inf", "-infinity"):
        return "-Inf"

    # Parse to Decimal
    try:
        d = Decimal(s)
    except InvalidOperation:
        return f"UNPARSABLE:{value}"

    if d.is_nan():
        return "NaN"
    if d.is_infinite():
        return "+Inf" if d > 0 else "-Inf"

    # Quantize to 16 decimal places with banker's rounding
    quantize_exp = Decimal("1." + "0" * 16)
    with localcontext() as ctx:
        ctx.prec = 50
        d = d.quantize(quantize_exp, rounding=ROUND_HALF_EVEN)

    # Normalize -0 to 0 (after quantize, so small negatives that round to zero are caught)
    if d == 0:
        d = Decimal("0").quantize(quantize_exp)

    return format(d, 'F')

x_normalize__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_normalize__mutmut_1': x_normalize__mutmut_1, 
    'x_normalize__mutmut_2': x_normalize__mutmut_2, 
    'x_normalize__mutmut_3': x_normalize__mutmut_3, 
    'x_normalize__mutmut_4': x_normalize__mutmut_4, 
    'x_normalize__mutmut_5': x_normalize__mutmut_5, 
    'x_normalize__mutmut_6': x_normalize__mutmut_6, 
    'x_normalize__mutmut_7': x_normalize__mutmut_7, 
    'x_normalize__mutmut_8': x_normalize__mutmut_8, 
    'x_normalize__mutmut_9': x_normalize__mutmut_9, 
    'x_normalize__mutmut_10': x_normalize__mutmut_10, 
    'x_normalize__mutmut_11': x_normalize__mutmut_11, 
    'x_normalize__mutmut_12': x_normalize__mutmut_12, 
    'x_normalize__mutmut_13': x_normalize__mutmut_13, 
    'x_normalize__mutmut_14': x_normalize__mutmut_14, 
    'x_normalize__mutmut_15': x_normalize__mutmut_15, 
    'x_normalize__mutmut_16': x_normalize__mutmut_16, 
    'x_normalize__mutmut_17': x_normalize__mutmut_17, 
    'x_normalize__mutmut_18': x_normalize__mutmut_18, 
    'x_normalize__mutmut_19': x_normalize__mutmut_19, 
    'x_normalize__mutmut_20': x_normalize__mutmut_20, 
    'x_normalize__mutmut_21': x_normalize__mutmut_21, 
    'x_normalize__mutmut_22': x_normalize__mutmut_22, 
    'x_normalize__mutmut_23': x_normalize__mutmut_23, 
    'x_normalize__mutmut_24': x_normalize__mutmut_24, 
    'x_normalize__mutmut_25': x_normalize__mutmut_25, 
    'x_normalize__mutmut_26': x_normalize__mutmut_26, 
    'x_normalize__mutmut_27': x_normalize__mutmut_27, 
    'x_normalize__mutmut_28': x_normalize__mutmut_28, 
    'x_normalize__mutmut_29': x_normalize__mutmut_29, 
    'x_normalize__mutmut_30': x_normalize__mutmut_30, 
    'x_normalize__mutmut_31': x_normalize__mutmut_31, 
    'x_normalize__mutmut_32': x_normalize__mutmut_32, 
    'x_normalize__mutmut_33': x_normalize__mutmut_33, 
    'x_normalize__mutmut_34': x_normalize__mutmut_34, 
    'x_normalize__mutmut_35': x_normalize__mutmut_35, 
    'x_normalize__mutmut_36': x_normalize__mutmut_36, 
    'x_normalize__mutmut_37': x_normalize__mutmut_37, 
    'x_normalize__mutmut_38': x_normalize__mutmut_38, 
    'x_normalize__mutmut_39': x_normalize__mutmut_39, 
    'x_normalize__mutmut_40': x_normalize__mutmut_40, 
    'x_normalize__mutmut_41': x_normalize__mutmut_41, 
    'x_normalize__mutmut_42': x_normalize__mutmut_42, 
    'x_normalize__mutmut_43': x_normalize__mutmut_43, 
    'x_normalize__mutmut_44': x_normalize__mutmut_44, 
    'x_normalize__mutmut_45': x_normalize__mutmut_45, 
    'x_normalize__mutmut_46': x_normalize__mutmut_46, 
    'x_normalize__mutmut_47': x_normalize__mutmut_47, 
    'x_normalize__mutmut_48': x_normalize__mutmut_48, 
    'x_normalize__mutmut_49': x_normalize__mutmut_49, 
    'x_normalize__mutmut_50': x_normalize__mutmut_50, 
    'x_normalize__mutmut_51': x_normalize__mutmut_51, 
    'x_normalize__mutmut_52': x_normalize__mutmut_52, 
    'x_normalize__mutmut_53': x_normalize__mutmut_53, 
    'x_normalize__mutmut_54': x_normalize__mutmut_54, 
    'x_normalize__mutmut_55': x_normalize__mutmut_55, 
    'x_normalize__mutmut_56': x_normalize__mutmut_56, 
    'x_normalize__mutmut_57': x_normalize__mutmut_57, 
    'x_normalize__mutmut_58': x_normalize__mutmut_58, 
    'x_normalize__mutmut_59': x_normalize__mutmut_59, 
    'x_normalize__mutmut_60': x_normalize__mutmut_60, 
    'x_normalize__mutmut_61': x_normalize__mutmut_61, 
    'x_normalize__mutmut_62': x_normalize__mutmut_62, 
    'x_normalize__mutmut_63': x_normalize__mutmut_63, 
    'x_normalize__mutmut_64': x_normalize__mutmut_64, 
    'x_normalize__mutmut_65': x_normalize__mutmut_65, 
    'x_normalize__mutmut_66': x_normalize__mutmut_66, 
    'x_normalize__mutmut_67': x_normalize__mutmut_67, 
    'x_normalize__mutmut_68': x_normalize__mutmut_68, 
    'x_normalize__mutmut_69': x_normalize__mutmut_69, 
    'x_normalize__mutmut_70': x_normalize__mutmut_70, 
    'x_normalize__mutmut_71': x_normalize__mutmut_71, 
    'x_normalize__mutmut_72': x_normalize__mutmut_72, 
    'x_normalize__mutmut_73': x_normalize__mutmut_73, 
    'x_normalize__mutmut_74': x_normalize__mutmut_74, 
    'x_normalize__mutmut_75': x_normalize__mutmut_75, 
    'x_normalize__mutmut_76': x_normalize__mutmut_76, 
    'x_normalize__mutmut_77': x_normalize__mutmut_77, 
    'x_normalize__mutmut_78': x_normalize__mutmut_78, 
    'x_normalize__mutmut_79': x_normalize__mutmut_79, 
    'x_normalize__mutmut_80': x_normalize__mutmut_80, 
    'x_normalize__mutmut_81': x_normalize__mutmut_81, 
    'x_normalize__mutmut_82': x_normalize__mutmut_82
}
x_normalize__mutmut_orig.__name__ = 'x_normalize'


def load_jsonl(path):
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_load_jsonl__mutmut_orig, x_load_jsonl__mutmut_mutants, args, kwargs, None)


def x_load_jsonl__mutmut_orig(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_1(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = None
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_2(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(None, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_3(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, None) as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_4(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open("r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_5(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, ) as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_6(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "XXrXX") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_7(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "R") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_8(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(None, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_9(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, None):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_10(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_11(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, ):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_12(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 2):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_13(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = None
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_14(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_15(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    break
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_16(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = None
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_17(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(None)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_18(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(None, file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_19(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=None)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_20(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_21(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", )
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_22(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(None)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_23(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(2)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_24(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = None
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_25(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get(None)
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_26(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("XXcase_idXX")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_27(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("CASE_ID")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_28(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is not None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_29(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(None, file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_30(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=None)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_31(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_32(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", )
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_33(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(None)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_34(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(2)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_35(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid not in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_36(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(None, file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_37(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=None)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_38(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_39(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", )
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_40(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = None
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_41(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get(None)
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_42(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("XXvalueXX")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_43(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("VALUE")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_44(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(None, file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_45(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=None)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_46(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(file=sys.stderr)
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_47(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", )
        sys.exit(1)
    return records


def x_load_jsonl__mutmut_48(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(None)
    return records


def x_load_jsonl__mutmut_49(path):
    """Load a JSONL file and return a dict keyed by case_id with raw values."""
    records = {}
    try:
        with open(path, "r") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error: invalid JSON in {path} at line {lineno}: {e}", file=sys.stderr)
                    sys.exit(1)
                cid = record.get("case_id")
                if cid is None:
                    print(f"FAIL: missing case_id in {path} at line {lineno}", file=sys.stderr)
                    sys.exit(1)
                if cid in records:
                    print(f"Warning: duplicate case_id '{cid}' in {path} at line {lineno}", file=sys.stderr)
                records[cid] = record.get("value")
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(2)
    return records

x_load_jsonl__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_load_jsonl__mutmut_1': x_load_jsonl__mutmut_1, 
    'x_load_jsonl__mutmut_2': x_load_jsonl__mutmut_2, 
    'x_load_jsonl__mutmut_3': x_load_jsonl__mutmut_3, 
    'x_load_jsonl__mutmut_4': x_load_jsonl__mutmut_4, 
    'x_load_jsonl__mutmut_5': x_load_jsonl__mutmut_5, 
    'x_load_jsonl__mutmut_6': x_load_jsonl__mutmut_6, 
    'x_load_jsonl__mutmut_7': x_load_jsonl__mutmut_7, 
    'x_load_jsonl__mutmut_8': x_load_jsonl__mutmut_8, 
    'x_load_jsonl__mutmut_9': x_load_jsonl__mutmut_9, 
    'x_load_jsonl__mutmut_10': x_load_jsonl__mutmut_10, 
    'x_load_jsonl__mutmut_11': x_load_jsonl__mutmut_11, 
    'x_load_jsonl__mutmut_12': x_load_jsonl__mutmut_12, 
    'x_load_jsonl__mutmut_13': x_load_jsonl__mutmut_13, 
    'x_load_jsonl__mutmut_14': x_load_jsonl__mutmut_14, 
    'x_load_jsonl__mutmut_15': x_load_jsonl__mutmut_15, 
    'x_load_jsonl__mutmut_16': x_load_jsonl__mutmut_16, 
    'x_load_jsonl__mutmut_17': x_load_jsonl__mutmut_17, 
    'x_load_jsonl__mutmut_18': x_load_jsonl__mutmut_18, 
    'x_load_jsonl__mutmut_19': x_load_jsonl__mutmut_19, 
    'x_load_jsonl__mutmut_20': x_load_jsonl__mutmut_20, 
    'x_load_jsonl__mutmut_21': x_load_jsonl__mutmut_21, 
    'x_load_jsonl__mutmut_22': x_load_jsonl__mutmut_22, 
    'x_load_jsonl__mutmut_23': x_load_jsonl__mutmut_23, 
    'x_load_jsonl__mutmut_24': x_load_jsonl__mutmut_24, 
    'x_load_jsonl__mutmut_25': x_load_jsonl__mutmut_25, 
    'x_load_jsonl__mutmut_26': x_load_jsonl__mutmut_26, 
    'x_load_jsonl__mutmut_27': x_load_jsonl__mutmut_27, 
    'x_load_jsonl__mutmut_28': x_load_jsonl__mutmut_28, 
    'x_load_jsonl__mutmut_29': x_load_jsonl__mutmut_29, 
    'x_load_jsonl__mutmut_30': x_load_jsonl__mutmut_30, 
    'x_load_jsonl__mutmut_31': x_load_jsonl__mutmut_31, 
    'x_load_jsonl__mutmut_32': x_load_jsonl__mutmut_32, 
    'x_load_jsonl__mutmut_33': x_load_jsonl__mutmut_33, 
    'x_load_jsonl__mutmut_34': x_load_jsonl__mutmut_34, 
    'x_load_jsonl__mutmut_35': x_load_jsonl__mutmut_35, 
    'x_load_jsonl__mutmut_36': x_load_jsonl__mutmut_36, 
    'x_load_jsonl__mutmut_37': x_load_jsonl__mutmut_37, 
    'x_load_jsonl__mutmut_38': x_load_jsonl__mutmut_38, 
    'x_load_jsonl__mutmut_39': x_load_jsonl__mutmut_39, 
    'x_load_jsonl__mutmut_40': x_load_jsonl__mutmut_40, 
    'x_load_jsonl__mutmut_41': x_load_jsonl__mutmut_41, 
    'x_load_jsonl__mutmut_42': x_load_jsonl__mutmut_42, 
    'x_load_jsonl__mutmut_43': x_load_jsonl__mutmut_43, 
    'x_load_jsonl__mutmut_44': x_load_jsonl__mutmut_44, 
    'x_load_jsonl__mutmut_45': x_load_jsonl__mutmut_45, 
    'x_load_jsonl__mutmut_46': x_load_jsonl__mutmut_46, 
    'x_load_jsonl__mutmut_47': x_load_jsonl__mutmut_47, 
    'x_load_jsonl__mutmut_48': x_load_jsonl__mutmut_48, 
    'x_load_jsonl__mutmut_49': x_load_jsonl__mutmut_49
}
x_load_jsonl__mutmut_orig.__name__ = 'x_load_jsonl'


def compare_naive(py_data, cpp_data, all_ids):
    args = [py_data, cpp_data, all_ids]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_compare_naive__mutmut_orig, x_compare_naive__mutmut_mutants, args, kwargs, None)


def x_compare_naive__mutmut_orig(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_1(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = None
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_2(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_3(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append(None)
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_4(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "XX<MISSING>XX", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_5(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<missing>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_6(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(None)))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_7(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            break
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_8(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_9(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append(None)
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_10(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(None), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_11(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "XX<MISSING>XX"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_12(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<missing>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_13(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            break

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_14(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = None
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_15(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = None

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_16(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = None
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_17(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) or isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_18(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp and str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_19(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py == raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_20(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(None) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_21(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) == str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_22(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(None):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_23(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append(None)
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_24(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(None), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_25(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(None)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_26(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(None) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_27(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) == str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_28(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(None):
                failures.append((cid, str(raw_py), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_29(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append(None)
    return failures


def x_compare_naive__mutmut_30(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(None), str(raw_cpp)))
    return failures


def x_compare_naive__mutmut_31(py_data, cpp_data, all_ids):
    """Compare raw values strictly (no normalization)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]

        both_numeric = isinstance(raw_py, (int, float)) and isinstance(raw_cpp, (int, float))
        if both_numeric:
            if raw_py != raw_cpp or str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(raw_cpp)))
        else:
            if str(raw_py) != str(raw_cpp):
                failures.append((cid, str(raw_py), str(None)))
    return failures

x_compare_naive__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_compare_naive__mutmut_1': x_compare_naive__mutmut_1, 
    'x_compare_naive__mutmut_2': x_compare_naive__mutmut_2, 
    'x_compare_naive__mutmut_3': x_compare_naive__mutmut_3, 
    'x_compare_naive__mutmut_4': x_compare_naive__mutmut_4, 
    'x_compare_naive__mutmut_5': x_compare_naive__mutmut_5, 
    'x_compare_naive__mutmut_6': x_compare_naive__mutmut_6, 
    'x_compare_naive__mutmut_7': x_compare_naive__mutmut_7, 
    'x_compare_naive__mutmut_8': x_compare_naive__mutmut_8, 
    'x_compare_naive__mutmut_9': x_compare_naive__mutmut_9, 
    'x_compare_naive__mutmut_10': x_compare_naive__mutmut_10, 
    'x_compare_naive__mutmut_11': x_compare_naive__mutmut_11, 
    'x_compare_naive__mutmut_12': x_compare_naive__mutmut_12, 
    'x_compare_naive__mutmut_13': x_compare_naive__mutmut_13, 
    'x_compare_naive__mutmut_14': x_compare_naive__mutmut_14, 
    'x_compare_naive__mutmut_15': x_compare_naive__mutmut_15, 
    'x_compare_naive__mutmut_16': x_compare_naive__mutmut_16, 
    'x_compare_naive__mutmut_17': x_compare_naive__mutmut_17, 
    'x_compare_naive__mutmut_18': x_compare_naive__mutmut_18, 
    'x_compare_naive__mutmut_19': x_compare_naive__mutmut_19, 
    'x_compare_naive__mutmut_20': x_compare_naive__mutmut_20, 
    'x_compare_naive__mutmut_21': x_compare_naive__mutmut_21, 
    'x_compare_naive__mutmut_22': x_compare_naive__mutmut_22, 
    'x_compare_naive__mutmut_23': x_compare_naive__mutmut_23, 
    'x_compare_naive__mutmut_24': x_compare_naive__mutmut_24, 
    'x_compare_naive__mutmut_25': x_compare_naive__mutmut_25, 
    'x_compare_naive__mutmut_26': x_compare_naive__mutmut_26, 
    'x_compare_naive__mutmut_27': x_compare_naive__mutmut_27, 
    'x_compare_naive__mutmut_28': x_compare_naive__mutmut_28, 
    'x_compare_naive__mutmut_29': x_compare_naive__mutmut_29, 
    'x_compare_naive__mutmut_30': x_compare_naive__mutmut_30, 
    'x_compare_naive__mutmut_31': x_compare_naive__mutmut_31
}
x_compare_naive__mutmut_orig.__name__ = 'x_compare_naive'


def compare_contract(py_data, cpp_data, all_ids):
    args = [py_data, cpp_data, all_ids]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_compare_contract__mutmut_orig, x_compare_contract__mutmut_mutants, args, kwargs, None)


def x_compare_contract__mutmut_orig(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_1(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = None
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_2(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_3(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append(None)
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_4(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "XX<MISSING>XX", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_5(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<missing>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_6(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(None), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_7(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "XX<MISSING>XX", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_8(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<missing>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_9(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(None)))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_10(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            break
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_11(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_12(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append(None)
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_13(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(None), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_14(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "XX<MISSING>XX", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_15(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<missing>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_16(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(None), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_17(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "XX<MISSING>XX"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_18(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<missing>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_19(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            break

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_20(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = None
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_21(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = None
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_22(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = None
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_23(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(None)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_24(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = None

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_25(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(None)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_26(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py == norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_27(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append(None)
    return failures


def x_compare_contract__mutmut_28(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(None), str(raw_cpp), norm_py, norm_cpp))
    return failures


def x_compare_contract__mutmut_29(py_data, cpp_data, all_ids):
    """Compare using normalized values (contract v1)."""
    failures = []
    for cid in all_ids:
        if cid not in py_data:
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", normalize(cpp_data[cid])))
            continue
        if cid not in cpp_data:
            failures.append((cid, str(py_data[cid]), "<MISSING>", normalize(py_data[cid]), "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(None), norm_py, norm_cpp))
    return failures

x_compare_contract__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_compare_contract__mutmut_1': x_compare_contract__mutmut_1, 
    'x_compare_contract__mutmut_2': x_compare_contract__mutmut_2, 
    'x_compare_contract__mutmut_3': x_compare_contract__mutmut_3, 
    'x_compare_contract__mutmut_4': x_compare_contract__mutmut_4, 
    'x_compare_contract__mutmut_5': x_compare_contract__mutmut_5, 
    'x_compare_contract__mutmut_6': x_compare_contract__mutmut_6, 
    'x_compare_contract__mutmut_7': x_compare_contract__mutmut_7, 
    'x_compare_contract__mutmut_8': x_compare_contract__mutmut_8, 
    'x_compare_contract__mutmut_9': x_compare_contract__mutmut_9, 
    'x_compare_contract__mutmut_10': x_compare_contract__mutmut_10, 
    'x_compare_contract__mutmut_11': x_compare_contract__mutmut_11, 
    'x_compare_contract__mutmut_12': x_compare_contract__mutmut_12, 
    'x_compare_contract__mutmut_13': x_compare_contract__mutmut_13, 
    'x_compare_contract__mutmut_14': x_compare_contract__mutmut_14, 
    'x_compare_contract__mutmut_15': x_compare_contract__mutmut_15, 
    'x_compare_contract__mutmut_16': x_compare_contract__mutmut_16, 
    'x_compare_contract__mutmut_17': x_compare_contract__mutmut_17, 
    'x_compare_contract__mutmut_18': x_compare_contract__mutmut_18, 
    'x_compare_contract__mutmut_19': x_compare_contract__mutmut_19, 
    'x_compare_contract__mutmut_20': x_compare_contract__mutmut_20, 
    'x_compare_contract__mutmut_21': x_compare_contract__mutmut_21, 
    'x_compare_contract__mutmut_22': x_compare_contract__mutmut_22, 
    'x_compare_contract__mutmut_23': x_compare_contract__mutmut_23, 
    'x_compare_contract__mutmut_24': x_compare_contract__mutmut_24, 
    'x_compare_contract__mutmut_25': x_compare_contract__mutmut_25, 
    'x_compare_contract__mutmut_26': x_compare_contract__mutmut_26, 
    'x_compare_contract__mutmut_27': x_compare_contract__mutmut_27, 
    'x_compare_contract__mutmut_28': x_compare_contract__mutmut_28, 
    'x_compare_contract__mutmut_29': x_compare_contract__mutmut_29
}
x_compare_contract__mutmut_orig.__name__ = 'x_compare_contract'


def print_report(failures, total, mode):
    args = [failures, total, mode]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_print_report__mutmut_orig, x_print_report__mutmut_mutants, args, kwargs, None)


def x_print_report__mutmut_orig(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_1(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = None
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_2(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total + len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_3(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(None)
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_4(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(None)
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_5(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(None)
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_6(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(None)

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_7(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = None
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_8(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(None, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_9(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, None)
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_10(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_11(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, )
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_12(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(11, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_13(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(None)
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_14(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode != "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_15(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "XXnaiveXX":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_16(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "NAIVE":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_17(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(None)
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_18(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'XXcase_idXX':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_19(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'CASE_ID':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_20(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'XXraw_pyXX':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_21(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'RAW_PY':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_22(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'XXraw_cppXX':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_23(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'RAW_CPP':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_24(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(None)
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_25(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-' / 10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_26(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'XX-XX'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_27(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*11} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_28(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-' / 28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_29(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'XX-XX'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_30(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*29} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_31(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-' / 28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_32(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'XX-XX'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_33(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*29}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_34(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(None)
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_35(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(None)
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_36(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'XXcase_idXX':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_37(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'CASE_ID':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_38(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'XXraw_pyXX':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_39(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'RAW_PY':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_40(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'XXraw_cppXX':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_41(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'RAW_CPP':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_42(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'XXnorm_pyXX':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_43(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'NORM_PY':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_44(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'XXnorm_cppXX':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_45(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'NORM_CPP':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_46(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(None)
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_47(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-' / 10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_48(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'XX-XX'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_49(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*11} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_50(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-' / 24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_51(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'XX-XX'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_52(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*25} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_53(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-' / 24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_54(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'XX-XX'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_55(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*25} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_56(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-' / 22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_57(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'XX-XX'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_58(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*23} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_59(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-' / 22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_60(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'XX-XX'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_61(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*23}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_62(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(None)
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_63(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(None)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_64(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(2)
    else:
        print("\nAll cases match.")
        sys.exit(0)


def x_print_report__mutmut_65(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print(None)
        sys.exit(0)


def x_print_report__mutmut_66(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("XX\nAll cases match.XX")
        sys.exit(0)


def x_print_report__mutmut_67(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nall cases match.")
        sys.exit(0)


def x_print_report__mutmut_68(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nALL CASES MATCH.")
        sys.exit(0)


def x_print_report__mutmut_69(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(None)


def x_print_report__mutmut_70(failures, total, mode):
    """Print summary and top 10 differences."""
    passed = total - len(failures)
    print(f"Mode        : {mode}")
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        if mode == "naive":
            print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28}")
            print(f"  {'-'*10} {'-'*28} {'-'*28}")
            for cid, raw_py, raw_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28}")
        else:
            print(f"  {'case_id':<10} {'raw_py':>24} {'raw_cpp':>24} {'norm_py':>22} {'norm_cpp':>22}")
            print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*22} {'-'*22}")
            for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
                print(f"  {cid:<10} {raw_py:>24} {raw_cpp:>24} {norm_py:>22} {norm_cpp:>22}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(1)

x_print_report__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_print_report__mutmut_1': x_print_report__mutmut_1, 
    'x_print_report__mutmut_2': x_print_report__mutmut_2, 
    'x_print_report__mutmut_3': x_print_report__mutmut_3, 
    'x_print_report__mutmut_4': x_print_report__mutmut_4, 
    'x_print_report__mutmut_5': x_print_report__mutmut_5, 
    'x_print_report__mutmut_6': x_print_report__mutmut_6, 
    'x_print_report__mutmut_7': x_print_report__mutmut_7, 
    'x_print_report__mutmut_8': x_print_report__mutmut_8, 
    'x_print_report__mutmut_9': x_print_report__mutmut_9, 
    'x_print_report__mutmut_10': x_print_report__mutmut_10, 
    'x_print_report__mutmut_11': x_print_report__mutmut_11, 
    'x_print_report__mutmut_12': x_print_report__mutmut_12, 
    'x_print_report__mutmut_13': x_print_report__mutmut_13, 
    'x_print_report__mutmut_14': x_print_report__mutmut_14, 
    'x_print_report__mutmut_15': x_print_report__mutmut_15, 
    'x_print_report__mutmut_16': x_print_report__mutmut_16, 
    'x_print_report__mutmut_17': x_print_report__mutmut_17, 
    'x_print_report__mutmut_18': x_print_report__mutmut_18, 
    'x_print_report__mutmut_19': x_print_report__mutmut_19, 
    'x_print_report__mutmut_20': x_print_report__mutmut_20, 
    'x_print_report__mutmut_21': x_print_report__mutmut_21, 
    'x_print_report__mutmut_22': x_print_report__mutmut_22, 
    'x_print_report__mutmut_23': x_print_report__mutmut_23, 
    'x_print_report__mutmut_24': x_print_report__mutmut_24, 
    'x_print_report__mutmut_25': x_print_report__mutmut_25, 
    'x_print_report__mutmut_26': x_print_report__mutmut_26, 
    'x_print_report__mutmut_27': x_print_report__mutmut_27, 
    'x_print_report__mutmut_28': x_print_report__mutmut_28, 
    'x_print_report__mutmut_29': x_print_report__mutmut_29, 
    'x_print_report__mutmut_30': x_print_report__mutmut_30, 
    'x_print_report__mutmut_31': x_print_report__mutmut_31, 
    'x_print_report__mutmut_32': x_print_report__mutmut_32, 
    'x_print_report__mutmut_33': x_print_report__mutmut_33, 
    'x_print_report__mutmut_34': x_print_report__mutmut_34, 
    'x_print_report__mutmut_35': x_print_report__mutmut_35, 
    'x_print_report__mutmut_36': x_print_report__mutmut_36, 
    'x_print_report__mutmut_37': x_print_report__mutmut_37, 
    'x_print_report__mutmut_38': x_print_report__mutmut_38, 
    'x_print_report__mutmut_39': x_print_report__mutmut_39, 
    'x_print_report__mutmut_40': x_print_report__mutmut_40, 
    'x_print_report__mutmut_41': x_print_report__mutmut_41, 
    'x_print_report__mutmut_42': x_print_report__mutmut_42, 
    'x_print_report__mutmut_43': x_print_report__mutmut_43, 
    'x_print_report__mutmut_44': x_print_report__mutmut_44, 
    'x_print_report__mutmut_45': x_print_report__mutmut_45, 
    'x_print_report__mutmut_46': x_print_report__mutmut_46, 
    'x_print_report__mutmut_47': x_print_report__mutmut_47, 
    'x_print_report__mutmut_48': x_print_report__mutmut_48, 
    'x_print_report__mutmut_49': x_print_report__mutmut_49, 
    'x_print_report__mutmut_50': x_print_report__mutmut_50, 
    'x_print_report__mutmut_51': x_print_report__mutmut_51, 
    'x_print_report__mutmut_52': x_print_report__mutmut_52, 
    'x_print_report__mutmut_53': x_print_report__mutmut_53, 
    'x_print_report__mutmut_54': x_print_report__mutmut_54, 
    'x_print_report__mutmut_55': x_print_report__mutmut_55, 
    'x_print_report__mutmut_56': x_print_report__mutmut_56, 
    'x_print_report__mutmut_57': x_print_report__mutmut_57, 
    'x_print_report__mutmut_58': x_print_report__mutmut_58, 
    'x_print_report__mutmut_59': x_print_report__mutmut_59, 
    'x_print_report__mutmut_60': x_print_report__mutmut_60, 
    'x_print_report__mutmut_61': x_print_report__mutmut_61, 
    'x_print_report__mutmut_62': x_print_report__mutmut_62, 
    'x_print_report__mutmut_63': x_print_report__mutmut_63, 
    'x_print_report__mutmut_64': x_print_report__mutmut_64, 
    'x_print_report__mutmut_65': x_print_report__mutmut_65, 
    'x_print_report__mutmut_66': x_print_report__mutmut_66, 
    'x_print_report__mutmut_67': x_print_report__mutmut_67, 
    'x_print_report__mutmut_68': x_print_report__mutmut_68, 
    'x_print_report__mutmut_69': x_print_report__mutmut_69, 
    'x_print_report__mutmut_70': x_print_report__mutmut_70
}
x_print_report__mutmut_orig.__name__ = 'x_print_report'


def main():
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs, None)


def x_main__mutmut_orig():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_1():
    parser = None
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_2():
    parser = argparse.ArgumentParser(
        description=None
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_3():
    parser = argparse.ArgumentParser(
        description="XXCompare out_py.jsonl vs out_cpp.jsonlXX"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_4():
    parser = argparse.ArgumentParser(
        description="compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_5():
    parser = argparse.ArgumentParser(
        description="COMPARE OUT_PY.JSONL VS OUT_CPP.JSONL"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_6():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument(None, help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_7():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help=None)
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_8():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument(help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_9():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", )
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_10():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("XXpy_jsonlXX", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_11():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("PY_JSONL", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_12():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="XXPath to Python output JSONLXX")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_13():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="path to python output jsonl")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_14():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="PATH TO PYTHON OUTPUT JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_15():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument(None, help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_16():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help=None)
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_17():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument(help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_18():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", )
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_19():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("XXcpp_jsonlXX", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_20():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("CPP_JSONL", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_21():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="XXPath to C++ output JSONLXX")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_22():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="path to c++ output jsonl")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_23():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="PATH TO C++ OUTPUT JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_24():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        None,
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_25():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=None,
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_26():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default=None,
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_27():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help=None,
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_28():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_29():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_30():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_31():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_32():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "XX--modeXX",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_33():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--MODE",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_34():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["XXnaiveXX", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_35():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["NAIVE", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_36():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "XXcontractXX"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_37():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "CONTRACT"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_38():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="XXcontractXX",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_39():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="CONTRACT",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_40():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="XXComparison mode: naive (raw strict) or contract (normalized, default)XX",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_41():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_42():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="COMPARISON MODE: NAIVE (RAW STRICT) OR CONTRACT (NORMALIZED, DEFAULT)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_43():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = None

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_44():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = None
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_45():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(None)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_46():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = None

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_47():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(None)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_48():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = None
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_49():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(None)
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_50():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) & set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_51():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(None) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_52():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(None))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_53():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = None

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_54():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total != 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_55():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 1:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_56():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print(None)
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_57():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("XXNo cases found.XX")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_58():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("no cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_59():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("NO CASES FOUND.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_60():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(None)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_61():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(1)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_62():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode != "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_63():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "XXnaiveXX":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_64():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "NAIVE":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_65():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = None
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_66():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(None, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_67():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, None, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_68():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, None)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_69():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_70():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_71():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, )
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_72():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = None

    print_report(failures, total, args.mode)


def x_main__mutmut_73():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(None, cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_74():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, None, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_75():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, None)

    print_report(failures, total, args.mode)


def x_main__mutmut_76():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(cpp_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_77():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, all_ids)

    print_report(failures, total, args.mode)


def x_main__mutmut_78():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, )

    print_report(failures, total, args.mode)


def x_main__mutmut_79():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(None, total, args.mode)


def x_main__mutmut_80():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, None, args.mode)


def x_main__mutmut_81():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, None)


def x_main__mutmut_82():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(total, args.mode)


def x_main__mutmut_83():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, args.mode)


def x_main__mutmut_84():
    parser = argparse.ArgumentParser(
        description="Compare out_py.jsonl vs out_cpp.jsonl"
    )
    parser.add_argument("py_jsonl", help="Path to Python output JSONL")
    parser.add_argument("cpp_jsonl", help="Path to C++ output JSONL")
    parser.add_argument(
        "--mode",
        choices=["naive", "contract"],
        default="contract",
        help="Comparison mode: naive (raw strict) or contract (normalized, default)",
    )
    args = parser.parse_args()

    py_data = load_jsonl(args.py_jsonl)
    cpp_data = load_jsonl(args.cpp_jsonl)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    if args.mode == "naive":
        failures = compare_naive(py_data, cpp_data, all_ids)
    else:
        failures = compare_contract(py_data, cpp_data, all_ids)

    print_report(failures, total, )

x_main__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13, 
    'x_main__mutmut_14': x_main__mutmut_14, 
    'x_main__mutmut_15': x_main__mutmut_15, 
    'x_main__mutmut_16': x_main__mutmut_16, 
    'x_main__mutmut_17': x_main__mutmut_17, 
    'x_main__mutmut_18': x_main__mutmut_18, 
    'x_main__mutmut_19': x_main__mutmut_19, 
    'x_main__mutmut_20': x_main__mutmut_20, 
    'x_main__mutmut_21': x_main__mutmut_21, 
    'x_main__mutmut_22': x_main__mutmut_22, 
    'x_main__mutmut_23': x_main__mutmut_23, 
    'x_main__mutmut_24': x_main__mutmut_24, 
    'x_main__mutmut_25': x_main__mutmut_25, 
    'x_main__mutmut_26': x_main__mutmut_26, 
    'x_main__mutmut_27': x_main__mutmut_27, 
    'x_main__mutmut_28': x_main__mutmut_28, 
    'x_main__mutmut_29': x_main__mutmut_29, 
    'x_main__mutmut_30': x_main__mutmut_30, 
    'x_main__mutmut_31': x_main__mutmut_31, 
    'x_main__mutmut_32': x_main__mutmut_32, 
    'x_main__mutmut_33': x_main__mutmut_33, 
    'x_main__mutmut_34': x_main__mutmut_34, 
    'x_main__mutmut_35': x_main__mutmut_35, 
    'x_main__mutmut_36': x_main__mutmut_36, 
    'x_main__mutmut_37': x_main__mutmut_37, 
    'x_main__mutmut_38': x_main__mutmut_38, 
    'x_main__mutmut_39': x_main__mutmut_39, 
    'x_main__mutmut_40': x_main__mutmut_40, 
    'x_main__mutmut_41': x_main__mutmut_41, 
    'x_main__mutmut_42': x_main__mutmut_42, 
    'x_main__mutmut_43': x_main__mutmut_43, 
    'x_main__mutmut_44': x_main__mutmut_44, 
    'x_main__mutmut_45': x_main__mutmut_45, 
    'x_main__mutmut_46': x_main__mutmut_46, 
    'x_main__mutmut_47': x_main__mutmut_47, 
    'x_main__mutmut_48': x_main__mutmut_48, 
    'x_main__mutmut_49': x_main__mutmut_49, 
    'x_main__mutmut_50': x_main__mutmut_50, 
    'x_main__mutmut_51': x_main__mutmut_51, 
    'x_main__mutmut_52': x_main__mutmut_52, 
    'x_main__mutmut_53': x_main__mutmut_53, 
    'x_main__mutmut_54': x_main__mutmut_54, 
    'x_main__mutmut_55': x_main__mutmut_55, 
    'x_main__mutmut_56': x_main__mutmut_56, 
    'x_main__mutmut_57': x_main__mutmut_57, 
    'x_main__mutmut_58': x_main__mutmut_58, 
    'x_main__mutmut_59': x_main__mutmut_59, 
    'x_main__mutmut_60': x_main__mutmut_60, 
    'x_main__mutmut_61': x_main__mutmut_61, 
    'x_main__mutmut_62': x_main__mutmut_62, 
    'x_main__mutmut_63': x_main__mutmut_63, 
    'x_main__mutmut_64': x_main__mutmut_64, 
    'x_main__mutmut_65': x_main__mutmut_65, 
    'x_main__mutmut_66': x_main__mutmut_66, 
    'x_main__mutmut_67': x_main__mutmut_67, 
    'x_main__mutmut_68': x_main__mutmut_68, 
    'x_main__mutmut_69': x_main__mutmut_69, 
    'x_main__mutmut_70': x_main__mutmut_70, 
    'x_main__mutmut_71': x_main__mutmut_71, 
    'x_main__mutmut_72': x_main__mutmut_72, 
    'x_main__mutmut_73': x_main__mutmut_73, 
    'x_main__mutmut_74': x_main__mutmut_74, 
    'x_main__mutmut_75': x_main__mutmut_75, 
    'x_main__mutmut_76': x_main__mutmut_76, 
    'x_main__mutmut_77': x_main__mutmut_77, 
    'x_main__mutmut_78': x_main__mutmut_78, 
    'x_main__mutmut_79': x_main__mutmut_79, 
    'x_main__mutmut_80': x_main__mutmut_80, 
    'x_main__mutmut_81': x_main__mutmut_81, 
    'x_main__mutmut_82': x_main__mutmut_82, 
    'x_main__mutmut_83': x_main__mutmut_83, 
    'x_main__mutmut_84': x_main__mutmut_84
}
x_main__mutmut_orig.__name__ = 'x_main'


if __name__ == "__main__":
    main()
