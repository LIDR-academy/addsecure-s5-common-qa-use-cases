# SyncGuard

SyncGuard is an automated test-repair agent for this repository. Its job is to run a test suite, diagnose failures, apply a minimal fix, rerun, and produce a structured report — all in one command.

## What SyncGuard does

1. **Run** the requested test suite via `scripts/syncguard_run.sh <suite>`
2. **Triage** failures by reading `artifacts/syncguard/latest.log` and `git diff`
3. **Apply a minimal fix** — the smallest code change that makes the failing tests pass
4. **Rerun** the suite to confirm the fix (max 2 iterations)
5. **Create a report** in `reports/syncguard/report_<session>.md`

If after 2 iterations the suite still fails, SyncGuard stops, does **not** invent further changes, and leaves a report with hypotheses and suggested next steps.

## Rules

- **Minimal changes only.** Touch only the lines needed to fix the failing tests. No refactors, no style cleanups, no unrelated edits.
- **No credentials.** Do not read, modify, or log `.env`, `.env.*`, or anything under `secrets/`.
- **No pushes.** Never run `git push` or any command that writes to the remote.
- **No deletions.** Do not delete source files, test files, or any project asset.
- **No commits.** Do not run `git commit`. All changes remain as working-tree edits for the developer to review.
- **Respect the Makefile.** Always invoke tests through the Makefile targets, never call `pytest` or `python3 -m pytest` directly.

## Suite → Makefile target mapping

| Suite         | Makefile target       |
|---------------|-----------------------|
| `unit`        | `make unit-test`      |
| `integration` | `make integration-test` |
| `bdd`         | `make bdd-test`       |
| `all`         | `make test`           |

## Report format

Every SyncGuard report must follow this structure:

```markdown
# SyncGuard Report — <suite> — <date>

## Summary
One-paragraph description of what happened: suite run, outcome, whether a fix was applied.

## Root Cause
Concise explanation of why the tests were failing.

## Fix Applied
Description of the change(s) made, with file paths and line numbers.

## Evidence
- Before: relevant log lines or assertion errors
- After: passing test output (or continued failure output if unresolved)

## Risks
Any potential side effects of the fix. If none are identified, state that explicitly.

## Next Steps
Actionable items for the developer: manual review, additional tests, follow-up work, or investigation if the suite still fails.
```

## File layout

```
artifacts/
  syncguard/
    latest.log          ← stdout+stderr from the most recent run
reports/
  syncguard/
    report_<session>.md ← one report per SyncGuard session
scripts/
  syncguard_run.sh      ← idempotent runner script
.claude/
  commands/
    syncguard.md        ← Claude Code slash command definition
  settings.json         ← permission overrides for SyncGuard
```
