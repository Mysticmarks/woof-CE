#!/usr/bin/env bash
set -euo pipefail

output=$(python3 build-manifest/parser.py build-manifest/examples/kernel.yaml)
echo "$output" | head -n 1 | grep -Fq "Build order: ['fetch-kernel', 'compile-kernel', 'package-kernel']"

output=$(python3 build-manifest/parser.py build-manifest/examples/package.yaml)
echo "$output" | head -n 1 | grep -Fq "Build order: ['fetch-src', 'build', 'install']"
