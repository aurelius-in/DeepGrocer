#!/usr/bin/env bash
set -euo pipefail
psql postgresql://dg:dgpass@localhost:5432/deepgrocer -f infra/sql/001_init.sql
psql postgresql://dg:dgpass@localhost:5432/deepgrocer -f infra/sql/002_receipts.sql
python scripts/seed_synthetic_day.py
echo "Smoke OK"

