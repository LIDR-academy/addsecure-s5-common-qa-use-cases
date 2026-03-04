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


def normalize(value):
    """Normalize a raw value to a canonical string for comparison."""
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


def compare_naive(py_data, cpp_data, all_ids):
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


def compare_contract(py_data, cpp_data, all_ids):
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


def print_report(failures, total, mode):
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


def main():
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


if __name__ == "__main__":
    main()
