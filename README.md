# 📌 Daily Task Prioritization Agent

A lightweight Python-based task prioritization system that reads tasks
from a CSV file, scores them intelligently, and generates a structured
daily execution plan in both JSON and text formats.

------------------------------------------------------------------------

## 📂 Project Structure

. ├── agent.py \# Main prioritization engine ├── tasks.csv \# Input
tasks file ├── plan.json \# Generated structured plan (machine-readable)
├── plan.txt \# Generated human-readable summary └── README.md \#
Project documentation

------------------------------------------------------------------------

## 🚀 Overview

This system:

1.  Reads tasks from `tasks.csv`
2.  Calculates priority scores based on:
    -   Urgency (deadline proximity)
    -   Importance (impact level)
    -   Quick win bonus (low effort tasks)
    -   Blocked task penalty
3.  Sorts tasks intelligently
4.  Generates:
    -   `plan.json` → Structured output
    -   `plan.txt` → Clean readable summary

------------------------------------------------------------------------

## 🧠 Scoring Logic

### Score Formula

Score = (urgency_weight × urgency) + (importance_weight × impact) +
quickwin_bonus − blocked_penalty

### Default Weights

  Factor              Value
  ------------------- -------
  Urgency Weight      2.0
  Importance Weight   3.0
  Quick Win Bonus     +1.0
  Blocked Penalty     −5.0

------------------------------------------------------------------------

## 📥 Input: `tasks.csv`

### Required Columns

  Column        Description            Example
  ------------- ---------------------- ---------------------------
  title         Task title             Fix login bug
  description   Task details           Reproduce and patch issue
  deadline      YYYY-MM-DD format      2025-12-24
  effort        S / M / L / minutes    25m
  impact        low / medium / high    high
  blocked       yes / no               no
  tags          comma-separated tags   work,backend

------------------------------------------------------------------------

### Effort Defaults

  Code   Minutes
  ------ ---------
  S      15
  M      45
  L      90

------------------------------------------------------------------------

## 📤 Output Files

### 1️⃣ plan.json

Structured machine-readable output containing:

-   Generated date
-   Top 3 tasks
-   Next 5 tasks
-   Blocked tasks (Unblock section)
-   Deferred tasks
-   Assumptions & weights
-   Score breakdown per task

------------------------------------------------------------------------

### 2️⃣ plan.txt

Human-readable daily execution summary.

Example format:

Daily Task Prioritization Plan (YYYY-MM-DD)

TOP 3 (Do these first) 1. Task Name \| deadline: YYYY-MM-DD \| effort:
Xm \| score: X.X Why: Explanation

------------------------------------------------------------------------

## 🏗 Task Categories

  Section   Description
  --------- --------------------------------
  TOP 3     Highest priority tasks
  NEXT 5    Next important tasks
  UNBLOCK   Blocked tasks needing action
  DEFER     Low urgency & low impact tasks

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
python agent.py
```

After execution:

-   `plan.json` will be generated
-   `plan.txt` will be generated
-   Summary will print in terminal

------------------------------------------------------------------------

## ⚙️ Customization

You can tweak the following in `agent.py`:

-   WEIGHTS
-   EFFORT_DEFAULTS_MIN
-   IMPACT_MAP
-   TOP3_COUNT
-   NEXT5_COUNT

------------------------------------------------------------------------

## 📊 Features

✅ Deadline-aware scoring\
✅ Impact-based prioritization\
✅ Quick-win detection\
✅ Blocked task penalty\
✅ Smart sorting (score → effort → title)\
✅ JSON + readable output\
✅ Fully configurable

------------------------------------------------------------------------

## 🛠 Requirements

-   Python 3.8+
-   No external dependencies (uses only standard library)

------------------------------------------------------------------------

## 📌 Summary

This project implements a configurable, intelligent task prioritization
engine that transforms raw task data into a structured, actionable daily
execution plan.

It is simple, extensible, and production-ready for lightweight planning
workflows.
