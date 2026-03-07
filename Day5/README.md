<p align="center">
  <h1 align="center">📋 Meeting Agenda Generator Agent</h1>
  <p align="center">
    <em>An AI-powered agent that transforms unstructured meeting details into clear, time-boxed, professional agendas — in seconds.</em>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LLM-LLaMA%203.1-orange?style=for-the-badge&logo=meta&logoColor=white" alt="LLaMA 3.1">
  <img src="https://img.shields.io/badge/API-Groq-green?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture / Workflow](#-architecture--workflow)
- [Installation Guide](#-installation-guide)
- [Usage Guide](#-usage-guide)
- [Project Folder Structure](#-project-folder-structure)
- [Sample Output](#-sample-output)
- [Future Enhancements](#-future-enhancements)
- [Contribution Guidelines](#-contribution-guidelines)
- [License](#-license)
- [Author](#-author)

---

## 🔍 Project Overview

**Meeting Agenda Generator Agent** is an AI-powered command-line tool that reads unstructured meeting details (title, objective, duration, participants, constraints) from a plain text file and produces a well-structured, time-boxed meeting agenda using a Large Language Model (LLM).

The agent outputs the agenda in two formats:
- **JSON** – machine-readable, easy to integrate with calendars or project management tools.
- **Plain Text** – human-readable, ready to share via email or messaging apps.

---

## ❗ Problem Statement

Meetings are one of the biggest drains on workplace productivity. Poorly planned meetings lack structure, run over time, and fail to reach actionable decisions.

**Common pain points:**
- ⏳ Spending too long manually drafting agendas
- 🎯 Missing clear objectives and time allocations
- 🤷 No defined owners or expected outcomes per agenda item
- 📉 Meetings that end without decisions or action items

This agent solves these problems by **automatically generating structured, time-boxed agendas** with clear ownership and expected outcomes — in seconds.

---

## ✨ Features

| Feature                          | Description                                                               |
|----------------------------------|---------------------------------------------------------------------------|
| 🤖 **AI-Powered Generation**     | Uses LLaMA 3.1 (via Groq API) to intelligently create agendas            |
| ⏱️ **Time-Boxed Scheduling**     | Automatically allocates time to each agenda item within the total duration |
| 👤 **Owner Assignment**          | Assigns topic owners based on participants and context                    |
| 🎯 **Outcome-Driven**            | Each agenda item includes an expected outcome                             |
| 🔀 **Dual Output Formats**       | Generates both JSON and human-readable text files                         |
| ✅ **Decision Point Detection**  | Identifies and flags agenda items that require decisions                   |
| 📝 **Simple Text Input**         | Just describe your meeting in plain text — the agent does the rest        |

---

## 🛠️ Tech Stack

| Technology               | Purpose                                    |
|--------------------------|--------------------------------------------|
| **Python 3.8+**          | Core programming language                  |
| **Groq SDK**             | API client for LLM inference               |
| **LLaMA 3.1 8B Instant** | Large Language Model for agenda generation |
| **python-dotenv**        | Environment variable management            |
| **JSON**                 | Structured output format                   |

---

## 🏗️ Architecture / Workflow

```
┌─────────────────┐
│   meeting.txt   │  ← Plain-text meeting details (input)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    agent.py     │  ← Reads input, calls LLM, parses response
│                 │
│  ┌───────────┐  │
│  │ Groq API  │  │  ← LLaMA 3.1 8B Instant model
│  │ (LLM)     │  │
│  └───────────┘  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  agenda.json    │  ← Structured JSON output
│  agenda.txt     │  ← Human-readable text output
└─────────────────┘
```

**Workflow Steps:**
1. User writes meeting details in `meeting.txt`
2. `agent.py` reads the input file
3. The meeting details are sent to **LLaMA 3.1** via the **Groq API** with a structured system prompt
4. The LLM returns a JSON agenda with time allocations, owners, and outcomes
5. The agent parses and saves the output as both `agenda.json` and `agenda.txt`

---

## 📦 Installation Guide

### Prerequisites

- Python 3.8 or higher
- A [Groq API Key](https://console.groq.com/) (free tier available)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/meeting-agenda-generator-agent.git
   cd meeting-agenda-generator-agent
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install groq python-dotenv
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🚀 Usage Guide

### 1. Define your meeting

Edit `meeting.txt` with your meeting details:

```text
Meeting Title: Q1 Product Planning
Objective: Decide priorities for Q1 roadmap and align teams
Duration: 60 minutes
Meeting Type: decision
Participants: Product, Engineering, Marketing
Constraints: Must decide top 3 features
```

### 2. Run the agent

```bash
python agent.py
```

### 3. View the output

The agent generates two files:

- **`agenda.json`** — Structured JSON agenda
- **`agenda.txt`** — Human-readable formatted agenda

**Example console output:**
```
Meeting agenda generated successfully.
```

---

## 📂 Project Folder Structure

```
Meeting Agenda Generator Agent/
│
├── agent.py           # Main agent script — reads input, calls LLM, saves output
├── meeting.txt        # Input file — meeting details in plain text
├── agenda.json        # Output — structured JSON agenda
├── agenda.txt         # Output — human-readable text agenda
├── .env               # Environment variables (Groq API key) — not committed
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (optional)
```

---

## 📸 Sample Output

### Input (`meeting.txt`)
```text
Meeting Title: Q1 Product Planning
Objective: Decide priorities for Q1 roadmap and align teams
Duration: 60 minutes
Meeting Type: decision
Participants: Product, Engineering, Marketing
Constraints: Must decide top 3 features
```

### Output (`agenda.txt`)
```
Meeting Agenda (2026-03-07)
=============================================

Title: Q1 Product Planning
Objective: Decide priorities for Q1 roadmap and align teams
Duration: 60 minutes

1. Review Current Roadmap and Gather Feedback (10 min)
   Owner: Product
   Outcome: Understand current team perspectives on Q1 roadmap

2. Marketing Input and Customer Feedback (15 min)
   Owner: Marketing
   Outcome: Understand customer needs and market trends

3. Engineering Input and Technical Feasibility (15 min)
   Owner: Engineering
   Outcome: Assess technical feasibility of proposed features

4. Prioritization and Decision-Making (10 min)
   Owner: Product
   Outcome: Decide top 3 features for Q1 roadmap

5. Next Steps and Action Items (10 min)
   Owner: Product
   Outcome: Assign action items and set deadlines
```

---

## 🔮 Future Enhancements

- [ ] 🌐 **Web UI** — Add a Streamlit / Gradio front-end for non-technical users
- [ ] 📧 **Email Integration** — Auto-send generated agendas to participants
- [ ] 📅 **Calendar Sync** — Export agendas to Google Calendar / Outlook
- [ ] 🧠 **Multi-Model Support** — Allow switching between different LLMs (GPT-4, Claude, Gemini)
- [ ] 📎 **Template Library** — Pre-built templates for standups, sprint planning, 1:1s, etc.
- [ ] 🔄 **Follow-Up Agent** — Generate post-meeting summaries and action item trackers
- [ ] 📊 **Analytics Dashboard** — Track meeting efficiency over time

---

## 🤝 Contribution Guidelines

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** with a clear description of your changes

### Guidelines
- Follow PEP 8 style guidelines for Python code
- Write clear, descriptive commit messages
- Test your changes before submitting a PR
- Update documentation if your changes affect usage

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 👤 Author

**Your Name**

- GitHub: [github.com/your-username](https://github.com/your-username)

---

<p align="center">
  <em>⭐ If you found this project useful, please give it a star!</em>
</p>
