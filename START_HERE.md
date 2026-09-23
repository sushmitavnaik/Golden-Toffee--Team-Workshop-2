# START HERE

## A. Create the baseline artifact outside the agent

1. Obtain the instructor-supplied spreadsheet and business question.
2. In ordinary ChatGPT, upload the spreadsheet and ask ChatGPT to answer the question and create one chart that communicates the answer.
3. Download the chart exactly as produced. Do not improve it yet.

## B. Open and inspect the frozen practice scaffold

1. Keep the original ZIP unchanged and unzip a separate working copy.
2. Place the working copy in your own GitHub repository and commit the unchanged starting point.
3. Run:

   `python tools/check_frozen_core.py`

4. Open the working folder in ChatGPT/Codex.
5. Give Codex this instruction before asking it to edit anything:

   > Inspect this Chart Improvement Practice Scaffold. Identify two categories: (1) the FROZEN CORE files that establish the common architecture and must not be changed, and (2) the student-editable files that will define and test my chart-improvement specialist. Do not edit anything yet. List the files in each category and explain the purpose of each student-editable file.

## C. Create and specialize the agent

1. Create the working agent folder:

   `python tools/new_agent.py chart_improvement_agent "Business Chart Improvement Agent" --specialty "evidence-preserving business visualization improvement"`

2. Put the unchanged baseline chart in:

   `agents/chart_improvement_agent/assets/baseline_chart.png`

3. Confirm that the instructor-supplied spreadsheet, business question, visualization-principles document, and applied case study are available in `course_materials/`.
4. Edit only these student files:

   - `agents/chart_improvement_agent/specialist_instructions.md`
   - `agents/chart_improvement_agent/agent_metadata.json`
   - `agents/chart_improvement_agent/cases/primary.json`
   - `agents/chart_improvement_agent/records/agent_record.md`

5. Add a `Source Roles and Authority` section to `specialist_instructions.md`. Treat the principles document as the governing framework and the case study as an illustrative calibration source. If they appear to conflict, the principles govern.
6. Translate the supplied visualization principles into operational rules in `specialist_instructions.md`. Do not merely copy definitions or reproduce case-specific chart changes.

## D. Build, run, validate, and revise

1. Build the prompt packet:

   `python tools/build_prompt.py --agent agents/chart_improvement_agent --case agents/chart_improvement_agent/cases/primary.json`

2. In ChatGPT, submit the generated prompt packet together with the five required inputs named in the case: baseline chart, source spreadsheet, business question, visualization-principles document, and applied case study.
3. Ask ChatGPT to create the improved chart file and then return the structured JSON report required by the prompt packet.
4. Save the JSON as:

   `agents/chart_improvement_agent/responses/primary_response.json`

5. Save the improved chart as:

   `agents/chart_improvement_agent/responses/improved_chart.png`

6. Validate the response:

   `python tools/validate_response.py agents/chart_improvement_agent/responses/primary_response.json`

7. Compare the two charts. Identify one weak or unsupported behavior, revise the specialist instructions, rerun the same case, and preserve the before/after evidence.
8. Run `python tools/check_frozen_core.py` again and commit the tested agent.

The scaffold does not call the OpenAI API and does not require an API key.
