#!/usr/bin/env bash
set -euo pipefail

shellcheck --severity=error merge2out tests/*.sh
for test in tests/*.sh; do
  bash "$test"
done
