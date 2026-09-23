# MASY1-GC 1800 Chart Improvement Practice Scaffold v1.0

This package is a short training scaffold for learning the same frozen-core workflow used later in the MASY1-GC 1800 Emerging Technologies specialist-agent assignments.

The agent built here has one bounded job: **improve an existing business chart** using a supplied visualization framework and an applied case study while preserving the chart's factual relationship to the source data and business question.

The agent does **not** create the baseline chart. Students first use ordinary ChatGPT to answer the supplied business question from the supplied spreadsheet and save the resulting chart. That chart becomes an input to the specialist agent built with this scaffold.

## What is frozen

- `core/` contains the common intake, behavior, and output contracts.
- `tools/` contains the common prompt-building, integrity-checking, and response-validation utilities.
- The hashes of those files are recorded in `FROZEN_CORE_SHA256.txt`.

## What students edit

Students create a new folder from `agents/_template/`, then edit only files inside that new agent folder. The important work is translating the supplied visualization principles into explicit specialist instructions, distinguishing the authority of the principles from the illustrative role of the case study, adding the saved baseline chart, completing the case, testing the result, and documenting one meaningful revision.

## Important boundary

This is a practice scaffold. It does not replace `MASY1800_ET_Agent_Scaffold_v1_0.zip`, whose frozen input and output contracts are specific to emerging-technology analysis.

Start with `START_HERE.md`.
