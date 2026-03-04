# Common Use Cases in Quality Assurance

## Problem statement

Python and C++ represent floating point numbers differently. E.g.: the number '-3' is represented as `-3` in C++ and as `-3.0` in Python. Therefore, for the same numerical inputs, the outcome of the formula `value = (a + b) * c` ends up being represented differently on each language.

## This repo

Implements a numeric equivalence validator between Python and C++ implementations of the formula `value = (a + b) * c` using IEEE 754 double-precision.

## Quick Start

```bash
# Install dependencies
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt

# Compile C++
make build

# Run all tests
make test
```
