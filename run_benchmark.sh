#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$ROOT/scripts/generate_dataset.py"   --config "$ROOT/config/default.yaml"   --output "$ROOT/generated/benchmark_dataset"   --mode benchmark
python3 "$ROOT/scripts/validate_dataset.py" "$ROOT/generated/benchmark_dataset"
