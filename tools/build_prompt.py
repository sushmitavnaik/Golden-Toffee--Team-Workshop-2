#!/usr/bin/env python3
from pathlib import Path
import argparse
import json

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description="Build a ChatGPT-ready chart-improvement specialist prompt packet.")
parser.add_argument("--agent", required=True, help="Agent folder, for example agents/chart_improvement_agent")
parser.add_argument("--case", required=True, help="Case JSON file")
parser.add_argument("--out", help="Output .txt path; defaults to work/<agent>_<case>_prompt.txt")
args = parser.parse_args()

agent = (root / args.agent).resolve() if not Path(args.agent).is_absolute() else Path(args.agent)
case_path = (root / args.case).resolve() if not Path(args.case).is_absolute() else Path(args.case)

common = (root / "core" / "common_instructions.md").read_text()
schema = json.loads((root / "core" / "output_schema.json").read_text())
metadata = json.loads((agent / "agent_metadata.json").read_text())
specialist = (agent / "specialist_instructions.md").read_text()
case = json.loads(case_path.read_text())

attachment_keys = [
    "business_question_file",
    "source_data_file",
    "baseline_chart_file",
    "visualization_principles_file",
    "application_case_study_file",
]
attachments = "\n".join(f"- {case[key]}" for key in attachment_keys)

packet = f"""MASY1-GC 1800 EMERGING TECHNOLOGIES - CHART IMPROVEMENT PRACTICE RUN

{common}

# AGENT METADATA
{json.dumps(metadata, indent=2)}

# STUDENT-SPECIALIZED ANALYTICAL INSTRUCTIONS
{specialist}

# CASE CONTEXT AND FILE MANIFEST
{json.dumps(case, indent=2)}

# REQUIRED INPUT FILES
The following files must be available to you in the same ChatGPT/Codex run. Read them before acting:
{attachments}

# REQUIRED OUTPUT SCHEMA
{json.dumps(schema, indent=2)}

Create the improved chart artifact using the requested filename. Then return the required JSON object only. Do not place the JSON in a Markdown code fence. If you cannot read any required file or create the chart artifact, do not invent a result; use the abstention fields and set artifact_created to false.
"""

output = Path(args.out) if args.out else root / "work" / f"{agent.name}_{case_path.stem}_prompt.txt"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(packet)
print(output)
