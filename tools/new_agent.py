#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description="Create a chart-improvement specialist folder from the frozen practice template.")
parser.add_argument("slug", help="Folder name, for example chart_improvement_agent")
parser.add_argument("display_name", help="Agent display name")
parser.add_argument("--specialty", default="REPLACE WITH BOUNDED CHART-IMPROVEMENT SPECIALTY")
args = parser.parse_args()

if not re.fullmatch(r"[A-Za-z0-9_-]+", args.slug):
    raise SystemExit("Slug may contain only letters, numbers, underscore, and hyphen.")

source = root / "agents" / "_template"
destination = root / "agents" / args.slug
if destination.exists():
    raise SystemExit(f"{destination} already exists")

shutil.copytree(source, destination)
metadata_path = destination / "agent_metadata.json"
metadata = json.loads(metadata_path.read_text())
metadata["name"] = args.display_name
metadata["specialty"] = args.specialty
metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")

case_path = destination / "cases" / "primary.json"
case = json.loads(case_path.read_text())
case["baseline_chart_file"] = f"agents/{args.slug}/assets/baseline_chart.png"
case_path.write_text(json.dumps(case, indent=2) + "\n")

print(f"Created {destination}")
print("Next: add baseline_chart.png, specialize the instructions, and complete the primary case.")

