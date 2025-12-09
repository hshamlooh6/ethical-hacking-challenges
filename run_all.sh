#!/usr/bin/env bash
# Runs every runnable solver/demo. Requires: python3, pip install -r requirements.txt
set -e
cd "$(dirname "$0")/challenges"
for f in */solve.py */demo.py */analyze.py; do
  [ -f "$f" ] || continue
  echo "===== $f ====="
  python3 "$f"
  echo
done
