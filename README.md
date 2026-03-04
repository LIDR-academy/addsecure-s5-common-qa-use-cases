# Common Use Cases in Quality Assurance

## Problem statement

Python and C++ represent floating point numbers differently. E.g.: the number '-3' is represented as `-3` in C++ and as `-3.0` in Python. Therefore, for the same numerical inputs, the outcome of the formula `value = (a + b) * c` ends up being represented differently on each language.

## This repo

Implements a numeric equivalence validator between Python and C++ implementations of the formula `value = (a + b) * c` using IEEE 754 double-precision with 16 decimal places. When rounding is necessary, it uses ROUND_HALF_EVEN by default. 

## Examples

| a | b | c | expected value |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 9.0000000000000000 |
| 0.1 | 0.2 | 10 | 3.0000000000000000 |
| -1.5 | 2.5 | -3.0 | -3.0000000000000000 |

## Quick Start

```bash
# Install dependencies
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt

# Compile C++
make build

# Run all tests
pytest

# Run unit tests
pytest tests/unit

# Run integration tests
pytest tests/integration
```

## Normalization contract

The items below specify how both implementations should normalize numeric values under given circumstances:

### Infinity or non-numeric values (including their floating point representation)
- NaN => "NaN"
- Inf/+Inf => "+Inf"
- Inf => "-Inf"

### Regular numbers (integers or floating point)
- use Decimal(str(value))
- represent it as 1e-16 with ROUND_HALF_EVEN rounding mode
- return it as a string with **exactly** 16 decimal places
- normalize -0.0 as "0.0000000000000000"

### Unparseable numbers
- return "UNPARSABLE:<valor>"


## Test cases

The aforementioned numeric equivalence validation **MUST COVER** at least the following cases, which are compliant with the `normalization contract` above:

1. Integers: operations with integers that yield exact results
2. Representation error: decimals without a finite binary representation (0.1, 0.2, 0.3, 0.6, 0.7)
3. Large numbers: values close to 1e15–1e308, which may cause overflow to +Inf
4. Catastrophic cancellation: sums of nearly equal values with opposite signs (e.g., 1e-15 + (-1e-15)) multiplied by a large factor
5. Negative zero: -0.0 + 0.0 to verify normalization of -0.0
6. Subnormals: the value 5e-324 (smallest positive representable double)
7. Identity: (x + 0) * 1 = x to verify preservation
8. Mixed signs: combinations of positive and negative numbers
9. NaN or Infinity: NaN or Infinity must not be used as inputs (only as possible results)

Test cases should be sorted from least to most difficult.
