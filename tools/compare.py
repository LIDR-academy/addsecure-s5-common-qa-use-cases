#!/usr/bin/env python3
"""Naïve compare: out_py.jsonl vs out_cpp.jsonl WITHOUT normalization.

Strict comparison:
  - If both values are numbers: fail if (py != cpp) or str(py) != str(cpp)
  - If case_id is missing in either file: fail
  - Compares raw JSON values as-is (no rounding, no canonical forms)

Exit code 0 if all cases match, 1 if any differ.
"""

import json
import math
import sys
from decimal import Context, Decimal, ROUND_HALF_EVEN, InvalidOperation

_Q16 = Decimal("1E-16")
_CTX = Context(prec=40, rounding=ROUND_HALF_EVEN)
_SPECIAL_STRINGS = {
    "nan": "NaN",
    "inf": "+Inf",
    "+inf": "+Inf",
    "-inf": "-Inf",
    "infinity": "+Inf",
    "+infinity": "+Inf",
    "-infinity": "-Inf",
}


def normalize(value):
    # TODO implement this function properly
    return str(value)


def load_jsonl(path):
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


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <out_py.jsonl> <out_cpp.jsonl>", file=sys.stderr)
        sys.exit(1)

    py_path = sys.argv[1]
    cpp_path = sys.argv[2]

    py_data = load_jsonl(py_path)
    cpp_data = load_jsonl(cpp_path)

    all_ids = sorted(set(py_data.keys()) | set(cpp_data.keys()))
    total = len(all_ids)

    if total == 0:
        print("No cases found.")
        sys.exit(0)

    failures = []
    for cid in all_ids:
        if cid not in py_data:
            norm_cpp = normalize(cpp_data[cid])
            failures.append((cid, "<MISSING>", str(cpp_data[cid]), "<MISSING>", norm_cpp))
            continue
        if cid not in cpp_data:
            norm_py = normalize(py_data[cid])
            failures.append((cid, str(py_data[cid]), "<MISSING>", norm_py, "<MISSING>"))
            continue

        raw_py = py_data[cid]
        raw_cpp = cpp_data[cid]
        norm_py = normalize(raw_py)
        norm_cpp = normalize(raw_cpp)

        if norm_py != norm_cpp:
            failures.append((cid, str(raw_py), str(raw_cpp), norm_py, norm_cpp))

    passed = total - len(failures)
    print(f"Total cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failures    : {len(failures)}")

    if failures:
        n = min(10, len(failures))
        print(f"\nTop {n} differences:")
        print(f"  {'case_id':<10} {'raw_py':>28} {'raw_cpp':>28} {'norm_py':>28} {'norm_cpp':>28}")
        print(f"  {'-'*10} {'-'*28} {'-'*28} {'-'*28} {'-'*28}")
        for cid, raw_py, raw_cpp, norm_py, norm_cpp in failures[:n]:
            print(f"  {cid:<10} {raw_py:>28} {raw_cpp:>28} {norm_py:>28} {norm_cpp:>28}")
        sys.exit(1)
    else:
        print("\nAll cases match.")
        sys.exit(0)


if __name__ == "__main__":
    main()
