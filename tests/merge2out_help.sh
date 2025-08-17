#!/usr/bin/env bash
set -euo pipefail

output=$(./merge2out --help 2>&1 || true)
if [[ $output != *"build system"* ]]; then
  echo "Unexpected output from merge2out --help" >&2
  exit 1
fi
