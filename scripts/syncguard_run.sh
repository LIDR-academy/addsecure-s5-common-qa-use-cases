#!/usr/bin/env bash
# scripts/syncguard_run.sh
# Idempotent test runner for SyncGuard.
# Usage: bash scripts/syncguard_run.sh [suite]
#   suite: unit (default) | integration | bdd | all

set -euo pipefail

SUITE="${1:-unit}"
LOG_DIR="artifacts/syncguard"
LOG_FILE="${LOG_DIR}/latest.log"

mkdir -p "${LOG_DIR}"

# Map suite to Makefile target
case "${SUITE}" in
  unit)        TARGET="unit-test" ;;
  integration) TARGET="integration-test" ;;
  bdd)         TARGET="bdd-test" ;;
  all)         TARGET="test" ;;
  *)
    echo "ERROR: Unknown suite '${SUITE}'. Valid values: unit, integration, bdd, all" >&2
    exit 2
    ;;
esac

COMMAND="make ${TARGET}"

echo "=== SyncGuard run ==="
echo "Suite   : ${SUITE}"
echo "Command : ${COMMAND}"
echo "Log     : ${LOG_FILE}"
echo "Started : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "====================="

# Run and capture all output; preserve exit code
set +e
{ ${COMMAND}; } 2>&1 | tee "${LOG_FILE}"
EXIT_CODE=${PIPESTATUS[0]}
set -e

echo ""
echo "====================="
if [ "${EXIT_CODE}" -eq 0 ]; then
  echo "RESULT  : PASS"
else
  echo "RESULT  : FAIL (exit code ${EXIT_CODE})"
fi
echo "Command : ${COMMAND}"
echo "Log     : ${LOG_FILE}"
echo "====================="

exit "${EXIT_CODE}"
