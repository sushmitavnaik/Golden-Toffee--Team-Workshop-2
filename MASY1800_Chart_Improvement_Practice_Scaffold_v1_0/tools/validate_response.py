#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import sys

required = [
    "agent",
    "business_question",
    "business_answer_shown",
    "baseline_chart_assessment",
    "data_fidelity_checks",
    "principles_applied",
    "improved_chart",
    "baseline_to_improved_comparison",
    "remaining_limitations",
    "abstention_or_more_information_needed",
]
arrays = [
    "baseline_chart_assessment",
    "data_fidelity_checks",
    "principles_applied",
    "baseline_to_improved_comparison",
    "remaining_limitations",
    "abstention_or_more_information_needed",
]

parser = argparse.ArgumentParser(description="Validate the basic chart-improvement specialist response contract.")
parser.add_argument("response")
args = parser.parse_args()
path = Path(args.response)

try:
    data = json.loads(path.read_text())
except Exception as error:
    raise SystemExit(f"INVALID JSON: {error}")

errors = []
if not isinstance(data, dict):
    errors.append("Top-level response must be an object.")
else:
    extra = sorted(set(data) - set(required))
    if extra:
        errors.append("Unexpected top-level field(s): " + ", ".join(extra))
    for key in required:
        if key not in data:
            errors.append(f"Missing required field: {key}")
    for key in ["business_question", "business_answer_shown"]:
        if key in data and not isinstance(data[key], str):
            errors.append(f"{key} must be a string")
    for key in arrays:
        if key in data and not isinstance(data[key], list):
            errors.append(f"{key} must be an array")

    agent = data.get("agent")
    if not isinstance(agent, dict):
        errors.append("agent must be an object")
    else:
        for key in ["name", "specialty", "version"]:
            if not isinstance(agent.get(key), str):
                errors.append(f"agent.{key} must be a string")

    chart = data.get("improved_chart")
    if not isinstance(chart, dict):
        errors.append("improved_chart must be an object")
    else:
        if not isinstance(chart.get("artifact_created"), bool):
            errors.append("improved_chart.artifact_created must be a boolean")
        for key in ["filename", "chart_type", "title", "accessibility_notes"]:
            if not isinstance(chart.get(key), str):
                errors.append(f"improved_chart.{key} must be a string")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("VALIDATION PASSED")

