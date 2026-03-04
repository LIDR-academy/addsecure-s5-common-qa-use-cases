#!/usr/bin/env python3
"""Read inputs.jsonl and compute value = (a + b) * c, write results to output JSONL."""

import json
import math
import sys


def compute(a, b, c):
    return (a + b) * c


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.jsonl> <output.jsonl>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        with open(input_path, "r") as fin:
            lines = fin.readlines()
    except FileNotFoundError:
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    results = []
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Error: invalid JSON at line {lineno}: {e}", file=sys.stderr)
            sys.exit(1)

        for field in ("case_id", "a", "b", "c"):
            if field not in record:
                print(f"Error: missing field '{field}' at line {lineno}", file=sys.stderr)
                sys.exit(1)

        try:
            a = float(record["a"])
            b = float(record["b"])
            c = float(record["c"])
        except (ValueError, TypeError) as e:
            print(f"Error: non-numeric value at line {lineno}: {e}", file=sys.stderr)
            sys.exit(1)

        value = compute(a, b, c)

        if math.isnan(value):
            value_out = "NaN"
        elif math.isinf(value):
            value_out = "+Inf" if value > 0 else "-Inf"
        else:
            if value == 0.0:
                value = 0.0  # normalize -0.0 to +0.0
            value_out = value

        results.append({"case_id": record["case_id"], "value": value_out})

    with open(output_path, "w") as fout:
        for r in results:
            fout.write(json.dumps(r) + "\n")

    print(f"Wrote {len(results)} results to {output_path}")


if __name__ == "__main__":
    main()
