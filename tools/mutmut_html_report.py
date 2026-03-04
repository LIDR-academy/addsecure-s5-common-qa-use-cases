#!/usr/bin/env python3
"""Generate an HTML mutation-testing report from mutmut 3.x result files.

Reads every *.meta file under the mutants/ directory, maps exit codes to
statuses, and writes mutation_report.html at the repo root.

Usage:
    python3 tools/mutmut_html_report.py
"""

import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# ── Status map (mirrors mutmut internals) ─────────────────────────────────────

STATUS_BY_EXIT_CODE = defaultdict(lambda: "suspicious", {
    0:    "survived",
    1:    "killed",
    3:    "killed",
    5:    "no tests",
    2:    "interrupted",
    33:   "no tests",
    34:   "skipped",
    35:   "suspicious",
    36:   "timeout",
    37:   "caught by type check",
    None: "not checked",
})

STATUS_EMOJI = {
    "survived":            "🙁",
    "killed":              "🎉",
    "no tests":            "🫥",
    "interrupted":         "🛑",
    "skipped":             "🔇",
    "suspicious":          "🤔",
    "timeout":             "⏰",
    "caught by type check":"🧙",
    "not checked":         "?",
}

STATUS_CSS_CLASS = {
    "survived":   "survived",
    "killed":     "killed",
    "no tests":   "no-tests",
    "skipped":    "skipped",
    "suspicious": "suspicious",
    "timeout":    "timeout",
    "not checked":"not-checked",
    "interrupted":"not-checked",
    "caught by type check": "skipped",
}


def get_mutant_diff(mutant_name: str) -> str:
    """Return the diff for a given mutant via `mutmut show`, or empty string."""
    try:
        result = subprocess.run(
            ["mutmut", "show", mutant_name],
            capture_output=True, text=True, timeout=10,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def load_all_results(mutants_dir: Path) -> list[dict]:
    """Walk mutants/ and collect all mutant results from *.meta files."""
    rows = []
    for meta_path in sorted(mutants_dir.rglob("*.meta")):
        try:
            with open(meta_path) as f:
                meta = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            continue

        source_path = str(meta_path.relative_to(mutants_dir)).removesuffix(".meta")
        for key, exit_code in meta.get("exit_code_by_key", {}).items():
            status = STATUS_BY_EXIT_CODE[exit_code]
            duration = meta.get("durations_by_key", {}).get(key)
            rows.append({
                "source": source_path,
                "mutant": key,
                "status": status,
                "exit_code": exit_code,
                "duration": f"{duration:.3f}s" if duration else "—",
            })
    return rows


def build_html(rows: list[dict]) -> str:
    total = len(rows)
    by_status: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_status[row["status"]].append(row)

    killed   = len(by_status.get("killed", []))
    survived = len(by_status.get("survived", []))
    skipped  = len(by_status.get("skipped", []))
    no_tests = len(by_status.get("no tests", []))
    other    = total - killed - survived - skipped - no_tests

    score = f"{killed / total * 100:.1f}%" if total > 0 else "n/a"

    # ── summary cards ──────────────────────────────────────────────────────────
    def card(label, count, css):
        return f'<div class="card {css}"><div class="count">{count}</div><div class="label">{label}</div></div>'

    cards = "".join([
        card("Total",    total,    "neutral"),
        card("Killed 🎉", killed,   "killed"),
        card("Survived 🙁", survived, "survived"),
        card("Skipped",  skipped,  "skipped"),
        card("No tests", no_tests, "no-tests"),
        card("Other",    other,    "neutral"),
    ])

    # ── per-mutant rows ────────────────────────────────────────────────────────
    table_rows = []
    for row in rows:
        css = STATUS_CSS_CLASS.get(row["status"], "neutral")
        emoji = STATUS_EMOJI.get(row["status"], "")
        diff_html = ""
        if row["status"] == "survived":
            diff = get_mutant_diff(row["mutant"])
            if diff:
                escaped = diff.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                diff_html = f'<pre class="diff">{escaped}</pre>'
        table_rows.append(
            f'<tr class="{css}">'
            f'<td>{row["source"]}</td>'
            f'<td class="mono">{row["mutant"]}</td>'
            f'<td>{emoji} {row["status"]}</td>'
            f'<td>{row["duration"]}</td>'
            f'</tr>'
            + (f'<tr class="{css} diff-row"><td colspan="4">{diff_html}</td></tr>' if diff_html else "")
        )

    table_body = "\n".join(table_rows) if table_rows else (
        '<tr><td colspan="4" class="empty">No results found — run <code>make mutate</code> first.</td></tr>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mutation Testing Report — normalize()</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{ font-family: system-ui, sans-serif; margin: 2rem; background: #f5f5f5; color: #222; }}
    h1   {{ margin-bottom: .25rem; }}
    .subtitle {{ color: #666; margin-bottom: 1.5rem; font-size: .9rem; }}
    .score {{ font-size: 2rem; font-weight: bold; margin-bottom: 1.5rem; }}
    .cards {{ display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem; }}
    .card  {{ padding: 1rem 1.5rem; border-radius: 8px; background: #fff;
              box-shadow: 0 1px 3px rgba(0,0,0,.1); min-width: 110px; text-align: center; }}
    .card .count {{ font-size: 2rem; font-weight: bold; }}
    .card .label {{ font-size: .8rem; color: #555; margin-top: .25rem; }}
    .card.killed   .count {{ color: #1a9c34; }}
    .card.survived .count {{ color: #c0392b; }}
    .card.skipped  .count {{ color: #888; }}
    .card.no-tests .count {{ color: #e67e22; }}
    table {{ width: 100%; border-collapse: collapse; background: #fff;
             box-shadow: 0 1px 3px rgba(0,0,0,.1); border-radius: 8px; overflow: hidden; }}
    th    {{ text-align: left; padding: .75rem 1rem; background: #333; color: #fff; font-size: .85rem; }}
    td    {{ padding: .6rem 1rem; border-bottom: 1px solid #eee; font-size: .85rem; }}
    .mono {{ font-family: monospace; }}
    tr.killed   td:nth-child(3) {{ color: #1a9c34; font-weight: bold; }}
    tr.survived td:nth-child(3) {{ color: #c0392b; font-weight: bold; }}
    tr.survived {{ background: #fff5f5; }}
    tr.skipped  td:nth-child(3) {{ color: #888; }}
    tr:hover    {{ background: #f0f0f0; }}
    tr.survived:hover {{ background: #ffe8e8; }}
    pre.diff    {{ background: #1e1e1e; color: #d4d4d4; padding: 1rem;
                  border-radius: 4px; overflow-x: auto; font-size: .78rem;
                  margin: .5rem 0; white-space: pre; }}
    .diff-row td {{ background: #fff8f8; }}
    .empty      {{ text-align: center; color: #888; padding: 2rem; }}
  </style>
</head>
<body>
  <h1>Mutation Testing Report</h1>
  <div class="subtitle">Target: <code>tools/compare.py</code> → <code>normalize()</code> &nbsp;|&nbsp;
    Test suite: <code>tests/unit/test_normalize_mutation.py</code></div>
  <div class="score">Mutation score: {score}</div>
  <div class="cards">{cards}</div>
  <table>
    <thead>
      <tr>
        <th>Source file</th>
        <th>Mutant</th>
        <th>Status</th>
        <th>Duration</th>
      </tr>
    </thead>
    <tbody>
{table_body}
    </tbody>
  </table>
</body>
</html>
"""


def main():
    repo_root = Path(__file__).parent.parent
    mutants_dir = repo_root / "mutants"

    if not mutants_dir.exists():
        print(
            "ERROR: mutants/ directory not found.\n"
            "Run 'make mutate' first to generate mutation results.",
            file=sys.stderr,
        )
        sys.exit(1)

    rows = load_all_results(mutants_dir)
    html = build_html(rows)

    out_path = repo_root / "mutation_report.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Report written to: {out_path}")

    # Print a quick summary to stdout as well
    total    = len(rows)
    killed   = sum(1 for r in rows if r["status"] == "killed")
    survived = sum(1 for r in rows if r["status"] == "survived")
    print(f"Total mutants : {total}")
    print(f"Killed        : {killed}")
    print(f"Survived      : {survived}")
    if total:
        print(f"Mutation score: {killed / total * 100:.1f}%")


if __name__ == "__main__":
    main()
