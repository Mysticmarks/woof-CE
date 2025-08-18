#!/usr/bin/env bash
set -euo pipefail

IMAGE="${WOOF_CONTAINER_IMAGE:-woof-ce:local}"

if command -v podman >/dev/null 2>&1; then
  RUNTIME="${CONTAINER_RUNTIME:-podman}"
elif command -v docker >/dev/null 2>&1; then
  RUNTIME="${CONTAINER_RUNTIME:-docker}"
else
  echo "Neither podman nor docker is available" >&2
  exit 1
fi

exec "$RUNTIME" run --rm -it \
  -v "$PWD":/workspace \
  -w /workspace \
  "$IMAGE" \
  "$@"
