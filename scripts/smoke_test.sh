#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="$ROOT_DIR/src"

mkdir -p "$ROOT_DIR/artifacts"

python3 -m uber_hotzone_ml.bootstrap.cli \
  --pickup-csv "$ROOT_DIR/data/raw/uber-trip-data/uber-raw-data-sep14.csv" \
  --output-csv "$ROOT_DIR/artifacts/hotzones.csv" \
  --top-k 25

ROOT_DIR_ENV="$ROOT_DIR" python3 - <<'PY'
import os
from pathlib import Path

output_path = Path(os.environ["ROOT_DIR_ENV"]) / "artifacts" / "hotzones.csv"
if not output_path.exists():
    raise SystemExit("Missing hotzones.csv")

line_count = sum(1 for _ in output_path.open("r", encoding="utf-8"))
if line_count < 2:
    raise SystemExit("Hotzone report is unexpectedly empty")
print(f"Smoke test OK: {line_count - 1} hotspot rows")
PY
