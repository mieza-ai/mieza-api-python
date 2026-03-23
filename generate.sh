#!/usr/bin/env bash
# Generate the TackTech GTO Python SDK from a fixed OpenAPI schema path.

set -o errexit
set -o pipefail
set -o nounset

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GTO_DIR="$SCRIPT_DIR/../gto"
SCHEMA_PATH="$GTO_DIR/resources/openapi.yaml"
OUT_DIR="$SCRIPT_DIR/.openapi_out"
TARGET_DIR="$SCRIPT_DIR/python_gt_client"

# Verify the schema file exists and is non-empty
if [[ ! -s "$SCHEMA_PATH" ]]; then
  echo "OpenAPI spec not found at $SCHEMA_PATH" >&2
  exit 1
fi

openapi-python-client generate \
  --path "$SCHEMA_PATH" \
  --config "$SCRIPT_DIR/openapi-python-client-config.yaml" \
  --output-path "$OUT_DIR" \
  --overwrite

SRC_DIR="$OUT_DIR/python_gt_client"
mkdir -p "$TARGET_DIR"

# Check if the source directory exists before copying
if [[ -d "$SRC_DIR" ]]; then
  cp -R "$SRC_DIR/"* "$TARGET_DIR/"
else
  echo "Generated SDK source directory not found at $SRC_DIR" >&2
  exit 1
fi
