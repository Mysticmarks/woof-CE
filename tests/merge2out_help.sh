#!/usr/bin/env bash
set -euo pipefail

if ! output=$(./merge2out --help 2>&1); then
  echo "merge2out --help failed" >&2
  exit 1
fi
if [[ $output != *"build system"* ]] || [[ $output != *"Usage"* ]]; then
  echo "Unexpected output from merge2out --help" >&2
  exit 1
fi
