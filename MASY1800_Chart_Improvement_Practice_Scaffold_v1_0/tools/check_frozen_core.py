#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[1]
manifest = root / "FROZEN_CORE_SHA256.txt"
errors = []

for line in manifest.read_text().splitlines():
    if not line.strip():
        continue
    expected, rel = line.split("  ", 1)
    path = root / rel
    if not path.exists():
        errors.append(f"MISSING: {rel}")
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        errors.append(f"CHANGED: {rel}")

if errors:
    print("FROZEN CORE CHECK FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("FROZEN CORE INTACT")

