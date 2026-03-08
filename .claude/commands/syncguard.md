---
name: syncguard
description: run suite, diagnose, apply minimal fix, rerun, and produce a report
argument-hint: "[suite]"
disable-model-invocation: true
allowed-tools:
  - Read
  - Edit
  - Bash
  - Grep
  - Glob
---

# SyncGuard — Automated Test-Repair Agent

**Suite:** $ARGUMENTS (default: `unit` if not provided)
**Session ID:** ${CLAUDE_SESSION_ID}

---

## Setup

Determine the suite to run:
- If `$ARGUMENTS` is empty or not provided, use `unit`.
- Valid values: `unit`, `integration`, `bdd`, `all`.
- If an unrecognised value is provided, stop and report an error.

Ensure output directories exist:
```bash
mkdir -p artifacts/syncguard reports/syncguard
```

---

## Loop (max 2 iterations)

Repeat the following steps up to **2 times**. Stop as soon as the suite passes.

### Step A — Run the suite

Execute the runner script:
```bash
bash scripts/syncguard_run.sh $ARGUMENTS
```

The script writes all output to `artifacts/syncguard/latest.log` and exits with a non-zero code on failure.

- If the exit code is **0**: the suite passes. Skip to **Step E**.
- If the exit code is **non-zero**: proceed to **Step B**.

### Step B — Triage the failure

Read the log and the current diff:
```bash
cat artifacts/syncguard/latest.log
git diff
```

Identify:
1. Which test(s) failed and the exact assertion/error message.
2. Which source file(s) are implicated by the stack trace or diff.
3. The root cause (logic bug, missing import, wrong value, etc.).

### Step C — Apply a minimal fix

- Edit **only** the file(s) directly responsible for the failure.
- Make the **smallest possible change**: fix the bug, nothing else.
- Do **not** refactor, rename, reformat, or touch unrelated lines.
- Do **not** read or modify `.env`, `.env.*`, or `secrets/**`.
- Do **not** run `git commit` or `git push`.

### Step D — Re-run

Go back to **Step A** for the next iteration.

---

## After the loop

### Step E — Generate the report

Write the report to:
```
reports/syncguard/report_${CLAUDE_SESSION_ID}.md
```

Use this exact structure:

```markdown
# SyncGuard Report — <suite> — <ISO date>

## Summary
<One paragraph: what suite was run, how many iterations, final outcome (pass/fail).>

## Root Cause
<Why the tests were failing. Reference specific files and line numbers.>

## Fix Applied
<Description of each change. Include file path, line numbers, before/after snippets.
If no fix was needed (suite passed on first run), state that.
If the suite still fails after 2 iterations, state that no conclusive fix was found.>

## Evidence
### Before
<Relevant failure lines from the first run's log.>

### After
<Relevant output from the final run (passing lines or remaining failures).>

## Risks
<Potential side effects of the fix. If none, say "No known risks identified.">

## Next Steps
<Actionable items: manual review, additional tests, or further investigation steps
if the suite still fails.>
```

### If the suite still fails after 2 iterations

- Do **not** make further code changes.
- Do **not** invent speculative fixes.
- Fill the report with the hypotheses gathered during triage and concrete next steps for the developer.
- Set the Summary to clearly state: "Suite still failing after 2 fix attempts."

---

## Constraints (always enforced)

- Never run `git push` or `git commit`.
- Never delete source files or test files.
- Never read `.env`, `.env.*`, or `secrets/**`.
- Always invoke tests through `scripts/syncguard_run.sh`, which uses Makefile targets.
- Minimal changes only — no refactors, no unrelated edits.
