# Habit Tracking Agent 🧠✅

Smart habit tracking and analysis tool that turns your daily check-ins into actionable insights.

---

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

---

## 📚 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Key Features](#-key-features)
4. [Tech Stack](#-tech-stack)
5. [System Architecture / Workflow](#-system-architecture--workflow)
6. [Installation Guide](#-installation-guide)
7. [Usage Guide](#-usage-guide)
8. [Project Folder Structure](#-project-folder-structure)
9. [API Documentation](#-api-documentation)
10. [Dataset Information](#-dataset-information)
11. [Screenshots / Demo](#-screenshots--demo)
12. [Future Enhancements](#-future-enhancements)
13. [Contribution Guidelines](#-contribution-guidelines)
14. [License](#-license)
15. [Author](#-author)

---

## 🧩 Project Overview

**Habit Tracking Agent** is a lightweight Python tool that analyzes your daily habit logs from a CSV file and generates:

- A detailed JSON report with per-habit statistics.
- A human-readable text summary with insights and recommendations.

This makes it easier to understand how consistent you are with your habits and where you can improve.

---

## ❗ Problem Statement

Building and maintaining good habits is hard because:

- Raw habit logs (spreadsheets, notes, checklists) are difficult to interpret.
- It is not obvious which habits are consistent and which need attention.
- People rarely get **data-driven feedback** about their routines.

This project converts simple daily habit check-ins into **clear metrics** and **actionable feedback**, helping users stay accountable and make informed improvements.

**Target Users:**

- Students building study, fitness, or sleep routines.
- Professionals tracking productivity or wellness habits.
- Anyone maintaining daily/weekly routines and wanting simple, offline analysis.

---

## 🌟 Key Features

- ✅ CSV-based habit input (works with `habit`, `date`, `completed`, `notes` columns).
- 📊 Per-habit statistics: total days, completed days, and consistency percentage.
- 🔁 Current streak calculation (consecutive completed days).
- 🧾 Automatic JSON report (`habits.json`) for programmatic use.
- 📄 Readable text summary (`habits.txt`) with:
  - Insight (e.g., *"Strong habit consistency."*)
  - Recommendation (e.g., *"Reduce difficulty or change timing."*)
- 🛡️ Robust handling of column name variations (`Habit` vs `habit`, etc.).

---

## 🛠 Tech Stack

- **Language:** Python 3.8+
- **Standard Libraries:**
  - `csv` — for reading habit logs from CSV files.
  - `json` — for generating structured reports.
  - `datetime` — for parsing and handling dates.
  - `collections.defaultdict` — for grouping records by habit.

No external dependencies are required.

---

## 🧬 System Architecture / Workflow

At a high level, the workflow is:

1. **Input**: User provides a CSV file (`habits.csv`) with daily habit records.
2. **Parsing**: The script reads and normalizes habit data.
3. **Analysis**: Per-habit metrics (consistency, streaks, missed days) are calculated.
4. **Output**:
   - Machine-readable report in `habits.json`.
   - Human-friendly summary in `habits.txt`.

```mermaid
flowchart LR
    A[habits.csv] --> B[read_habits()]
    B --> C[analyze_habits()]
    C --> D[habits.json]
    C --> E[habits.txt]
```

---

## 📥 Installation Guide

1. **Clone or download** this repository:

```bash
git clone https://github.com/your-username/habit-tracking-agent.git
cd "habit-tracking agent"
```

2. **Ensure Python is installed** (version 3.8 or higher):

```bash
python --version
```

3. (Optional) **Create and activate a virtual environment**:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

No extra packages are required since the project only uses Python's standard library.

---

## ▶️ Usage Guide

1. Prepare a `habits.csv` file in the project directory.

Below is an example that matches the sample run in the screenshot:

```csv
habit,date,completed,notes
Morning walk,2025-03-01,yes,Felt energized
Morning walk,2025-03-02,yes,
Morning walk,2025-03-03,no,Too busy
Morning walk,2025-03-04,yes,
Morning walk,2025-03-05,yes,
Read 20 pages,2025-03-01,yes,
Read 20 pages,2025-03-02,no,Tired
Read 20 pages,2025-03-03,no,
Read 20 pages,2025-03-04,yes,
```

- `habit` / `Habit`: Name of the habit (for example, `Morning walk`, `Read 20 pages`).
- `date` / `Date`: Date in `YYYY-MM-DD` format.
- `completed` / `Completed`: `yes` or `no` (case-insensitive).
- `notes` / `Notes`: (Optional) Free-text notes.

2. Run the analysis script:

```bash
python agent.py
```

3. After running, the following files will be generated in the same folder:

- `habits.json` — structured per-habit metrics.
- `habits.txt` — readable summary with insights and recommendations.

4. Check the console output for a quick status message. For the above sample CSV, it looks like:

```text
✅ Habit analysis complete.
Tracked habits: 2
```

---

## 🗂 Project Folder Structure

```text
.
├── agent.py        # Main habit analysis script
├── habits.csv      # Input data: user-provided habit log
├── habits.json     # Output: JSON report (generated)
├── habits.txt      # Output: Text summary (generated)
└── README.md       # Project documentation
```

---

## 📡 API Documentation

This project is a **command-line utility** and **does not expose HTTP APIs**.

Key functions inside `agent.py`:

- `parse_date(s: str) -> date`
  - Parses a date string in `YYYY-MM-DD` format.
- `read_habits(path: str = "habits.csv") -> list[dict]`
  - Reads habit records from a CSV file and normalizes them.
- `analyze_habits(records: list[dict]) -> dict`
  - Groups records by habit and calculates:
    - `total_days`
    - `completed_days`
    - `consistency_percent`
    - `current_streak`
    - `missed_days`
    - `insight`
    - `recommendation`
- `main()`
  - Orchestrates reading input, analyzing habits, and writing outputs.

You can also import `agent.py` as a module in another Python script and call `read_habits` / `analyze_habits` directly.

---

## 📊 Dataset Information

- **Input File:** `habits.csv`
- **Format:** CSV with the following columns:
  - `habit` / `Habit` — string, required.
  - `date` / `Date` — string, `YYYY-MM-DD`, required.
  - `completed` / `Completed` — string (`Yes`/`No`), required.
  - `notes` / `Notes` — string, optional.
- **Storage:** Local file only; no data is sent to external services.
- **Privacy:** All data remains on the user's machine.

Sample rows:

```csv
habit,date,completed,notes
Meditation,2026-03-01,Yes,Evening session
Meditation,2026-03-02,No,Busy day
Sleep before 11 PM,2026-03-01,Yes,
```

---

## 🚀 Future Enhancements

- 📈 Visual dashboards (charts for streaks and consistency over time).
- 📅 Support for multiple CSV files or date ranges.
- 🕒 Configurable habit difficulty levels and weighting.
- 🌐 Web or desktop UI for non-technical users.
- ⚙️ Command-line options (custom input/output file paths, filters, etc.).
- 🔔 Reminders or notifications based on low-consistency habits.

---

## 🤝 Contribution Guidelines

Contributions are welcome! 🎉

1. Fork the repository.
2. Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and ensure the script still runs correctly.
4. Commit your changes with a clear message:

```bash
git commit -m "Add feature: description"
```

5. Push your branch and open a Pull Request.

Please keep the code clean, readable, and consistent with the existing style.

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project, subject to the terms of the MIT license.

---

## 👩‍💻 Author

**Anya Sree**  
- GitHub: [Sree-8639](https://github.com/Sree-8639)  
- Email: [23A81A6193@sves.org.in](mailto:23A81A6193@sves.org.in)

If you find this project helpful, consider giving it a ⭐ on GitHub!