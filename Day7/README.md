# 🤖 Daily Goal Reflection Agent

AI-powered Python agent that turns your daily goal log into structured reflections, insights, and actionable next-day suggestions.

## 📚 Table of Contents
- [🔍 Overview](#overview)
- [✨ Features](#features)
- [📁 Project Structure](#project-structure)
- [✅ Prerequisites](#prerequisites)
- [⚙️ Installation](#installation)
- [🔐 Configuration](#configuration)
- [▶️ Usage](#usage)
- [📝 Input Format](#input-format)
- [📤 Output Format](#output-format)
- [🔄 End-to-End Example](#end-to-end-example)
- [🧰 Tech Stack](#tech-stack)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

## 🔍 Overview
The Daily Goal Reflection Agent is a Python-based CLI assistant for end-of-day review. It reads your planned goals and actual outcomes, sends the context to Groq for analysis, and generates both machine-readable and human-readable reflections.

The workflow is simple: provide your day summary in a text file, run the agent, and receive structured outputs that highlight completed goals, missed goals, key insights, lessons learned, and suggestions for tomorrow.

### Project Screenshots
![Terminal Run Output](images/terminal-output.png)

![Workspace and Files](images/project-explorer.png)

![Generated reflection.json](images/reflection-json-output.png)

![Generated reflection.txt](images/reflection-text-output.png)

## ✨ Features
- 🎯 Compares planned goals against actual outcomes
- ✅ Identifies completed and missed goals automatically
- 🧠 Extracts insights and lessons learned from your notes
- 📅 Suggests practical actions for the next day
- 🧾 Produces clean JSON output for automation workflows
- 📄 Produces readable TXT output for quick review and journaling

## 📁 Project Structure
```text
7.Daily Goal Reflection Agent/
├── .env
├── agent.py
├── day.txt
├── reflection.json
├── reflection.txt
└── README.md
```

## ✅ Prerequisites
- Python 3.10 or newer
- A Groq API key
- Internet access for LLM API calls

## ⚙️ Installation
1. Clone the repository.

```bash
git clone https://github.com/shanm/daily-goal-reflection-agent.git
cd daily-goal-reflection-agent
```

2. Create and activate a virtual environment.

```bash
python -m venv .venv
```

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):
```bat
.\.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
source .venv/bin/activate
```

3. Install dependencies.

```bash
pip install groq python-dotenv
```

## 🔐 Configuration
Create a `.env` file in the project root with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

How setup works:
- `agent.py` loads environment variables using `python-dotenv`
- The Groq client is initialized with `GROQ_API_KEY`

## ▶️ Usage
1. Update `day.txt` with your daily plan and outcomes.
2. Run the agent.

```bash
python agent.py
```

3. Review generated files:
- `reflection.json`
- `reflection.txt`

## 📝 Input Format
The input is a plain text daily report in `day.txt`.

Example:

```text
Planned Goals:
- Finish client proposal
- Review PRs
- Go for a 30-minute walk

Actual Outcomes:
- Finished client proposal
- Reviewed only 1 PR
- Skipped walk

Notes:
Unexpected production issue took 2 hours.
Energy level was low in the afternoon.
```

## 📤 Output Format
The project generates two outputs:

1. `reflection.json` (structured data)

```json
{
  "summary": "Today's goals were partially achieved due to unexpected production issues and low energy levels in the afternoon.",
  "completed_goals": [
    "Finished client proposal"
  ],
  "missed_goals": [
    "Review all PRs",
    "Go for a 30-minute walk"
  ],
  "insights": [
    "Unexpected production issues can significantly impact daily goals",
    "Low energy levels in the afternoon can hinder productivity"
  ],
  "lessons_learned": [
    "Prioritize tasks based on urgency and importance",
    "Schedule critical tasks during high-energy periods"
  ],
  "tomorrow_suggestions": [
    "Review remaining PRs as a priority task",
    "Schedule a 30-minute walk in the morning to boost energy levels",
    "Leave a buffer for unexpected issues and adjust the schedule accordingly"
  ]
}
```

2. `reflection.txt` (human-readable report)

```text
Daily Reflection (2026-03-29)
=============================================

SUMMARY:
Today's goals were partially achieved due to unexpected production issues and low energy levels in the afternoon.

COMPLETED GOALS:
- Finished client proposal

MISSED GOALS:
- Review all PRs
- Go for a 30-minute walk
```

## 🔄 End-to-End Example
```bash
# 1) Add your daily data to day.txt
# 2) Run the agent
python agent.py

# 3) Open outputs
type reflection.json
```

Expected result:
- `reflection.json` contains structured reflection fields
- `reflection.txt` contains a clean daily summary report

## 🧰 Tech Stack
| Layer | Technology |
|------|------------|
| Language | Python |
| Project Type | CLI Agent |
| LLM Provider | Groq |
| Model | llama-3.3-70b-versatile |
| Environment Config | python-dotenv |
| Data Format | JSON + Plain Text |

## 🤝 Contributing
1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/improve-reflection-agent
```

3. Make your changes and test locally.
4. Commit with a clear message.

```bash
git add .
git commit -m "Improve reflection parsing and output formatting"
```

5. Push your branch.

```bash
git push origin feature/improve-reflection-agent
```

6. Open a Pull Request with a concise description of your changes.

## 📄 License
No license file is currently defined for this project.