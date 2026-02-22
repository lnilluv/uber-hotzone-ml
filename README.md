# Uber Hotzone ML

Production-ready hotzone recommendation project based on Uber NYC pickup data.

## Portfolio highlights

- Split from a larger monorepo into an independent deployable service repo
- Refactored into hexagonal architecture for maintainability and clean dependency direction
- Added deterministic CLI report generation (`--top-k` hotspots)
- Added unit tests for hotspot aggregation and application orchestration
- Added local and Docker smoke tests for real runtime verification
- Added security baseline (`.env.example`, artifact ignore rules, dependency audit path)

## Project layout

- `src/uber_hotzone_ml/domain/`: hotspot aggregation rules
- `src/uber_hotzone_ml/application/`: use cases and ports
- `src/uber_hotzone_ml/adapters/`: CSV loaders/writers
- `src/uber_hotzone_ml/bootstrap/`: CLI wiring
- `tests/unit/`: unit tests
- `scripts/smoke_test.sh`: end-to-end smoke run
- `data/raw/uber-trip-data/`: source datasets

## Quick start

```bash
export PYTHONPATH=src
python3 -m unittest discover -s tests/unit -p 'test_*.py'
./scripts/smoke_test.sh
```

## CLI usage

```bash
python3 -m uber_hotzone_ml.bootstrap.cli \
  --pickup-csv data/raw/uber-trip-data/uber-raw-data-sep14.csv \
  --output-csv artifacts/hotzones.csv \
  --top-k 50
```

## Docker

```bash
docker build -t uber-hotzone-ml:local .
docker run --rm -v "$PWD/artifacts:/app/artifacts" uber-hotzone-ml:local \
  --pickup-csv /app/data/raw/uber-trip-data/uber-raw-data-sep14.csv \
  --output-csv /app/artifacts/hotzones.csv \
  --top-k 50
```

## Verification commands

```bash
python3 -m unittest discover -s tests/unit -p 'test_*.py'
./scripts/smoke_test.sh
docker build -t uber-hotzone-ml:local .
```
