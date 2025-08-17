#!/usr/bin/env bash
set -euo pipefail

if output=$(su nobody -s /bin/bash -c 'GITHUB_ACTIONS=1 ./merge2out' 2>&1); then
  echo "merge2out should fail when not run as root" >&2
  exit 1
fi
if [[ $output != *"Must be root"* ]]; then
  echo "Unexpected output: $output" >&2
  exit 1
fi
