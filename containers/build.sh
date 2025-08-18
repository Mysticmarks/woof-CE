#!/usr/bin/env bash
set -euo pipefail

IMAGE="${WOOF_CONTAINER_IMAGE:-woof-ce:local}"

if command -v podman >/dev/null 2>&1; then
  RUNTIME="${CONTAINER_RUNTIME:-podman}"
elif command -v docker >/dev/null 2>&1; then
  RUNTIME="${CONTAINER_RUNTIME:-docker}"
else
  echo "No container runtime found" >&2
  exit 1
fi

exec "$RUNTIME" build -t "$IMAGE" -f "$(dirname "$0")/Dockerfile" "$(dirname "$0")"
