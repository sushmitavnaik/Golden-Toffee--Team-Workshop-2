# ChatGPT + Codex Reference Workflow

ChatGPT is the course AI environment. Codex is the supported development path.

1. Use ordinary ChatGPT first to create the baseline chart from the spreadsheet and business question.
2. Open the unzipped scaffold as a working folder in ChatGPT/Codex.
3. Ask Codex to inspect the package and distinguish FROZEN CORE from student-editable files before editing.
4. Create a new agent from `agents/_template/` with `tools/new_agent.py`.
5. Give Codex both visualization sources. Direct it to treat the principles document as the governing framework and the case study as illustrative calibration rather than a template to copy.
6. Ask Codex to add that source hierarchy to the student-editable specialist instructions and translate the six dimensions and eighteen elements into operational rules.
7. Keep the agent's responsibility bounded to improving the supplied chart. The source data are available for verification, not for creating a new baseline analysis.
8. Complete the case JSON, build the prompt packet with `tools/build_prompt.py`, and run it in ChatGPT with all required attachments.
9. Save the improved PNG and structured JSON response; validate the JSON with `tools/validate_response.py`.
10. Diagnose one important weakness, revise only the specialist files, rerun, compare, and record the judgment.
11. Verify that FROZEN CORE remains intact before committing.

The reference scaffold does not call the OpenAI API.
