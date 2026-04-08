# Note-to-Action Item Agent 📝➡️✅

> Turn unstructured meeting notes into clear, trackable action items.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📚 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Features](#-features)
4. [Tech Stack](#-tech-stack)
5. [Architecture / Workflow](#-architecture--workflow)
6. [Installation Guide](#-installation-guide)
7. [Usage Guide](#-usage-guide)
8. [Project Folder Structure](#-project-folder-structure)
9. [API Documentation](#-api-documentation)
10. [Future Enhancements](#-future-enhancements)
11. [Contribution Guidelines](#-contribution-guidelines)
12. [License](#-license)
13. [Author](#-author)

---

## 🧾 Project Overview

The **Note-to-Action Item Agent** is a lightweight Python tool that reads raw meeting notes and automatically extracts well-structured action items using the Groq LLM API.

It:
- Parses unstructured notes from `notes.txt`
- Sends them to a language model with a strict system prompt
- Produces a structured list of actions as both `actions.json` and a human-readable `actions.txt`

This makes it easy to go from messy notes to a clear, shareable action list in seconds.

---

## ❗ Problem Statement

Unstructured meeting notes are hard to follow and even harder to turn into concrete follow-ups:

- Important tasks are buried in paragraphs of discussion
- Owners, deadlines, and priorities are often missing or ambiguous
- Teams lose track of who is responsible for what

The **Note-to-Action Item Agent** solves this by automatically extracting only *actionable* items from notes and structuring them into a machine- and human-friendly format.

---

## ✨ Features

- ✅ **Action extraction only** – Ignores opinions, ideas, and non-actionable text
- 👥 **Owner detection** – Resolves the task owner when mentioned, or defaults to `Unassigned`
- ⏰ **Deadline inference** – Suggests a deadline when implied, or uses `Not specified`
- 🚦 **Priority tagging** – Classifies each task as `Low`, `Medium`, or `High`
- 📄 **Dual output formats** – Exports to both `actions.json` and `actions.txt`
- 🔍 **Source context** – Keeps a short snippet of the original context for each action

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **LLM Provider:** [Groq](https://groq.com/) (`llama-3.3-70b-versatile` model)
- **Environment Management:** [python-dotenv](https://github.com/theskumar/python-dotenv)
- **Standard Library:** `json`, `os`, `datetime`

> Make sure you have a valid **GROQ_API_KEY** to use this project.

---

## 🧬 Architecture / Workflow

High-level flow:

1. 📝 User writes or pastes meeting notes into `notes.txt`.
2. ▶️ `agent.py` is executed (`python agent.py`).
3. 📤 The script reads the notes and sends them to the Groq Chat Completions API with a strict JSON-only system prompt.
4. 🧠 The LLM returns a JSON payload matching the schema:

   ```json
   {
     "actions": [
       {
         "action": "",
         "owner": "",
         "deadline": "",
         "priority": "",
         "source_context": ""
       }
     ]
   }
   ```

5. 💾 The response is parsed and saved to:
   - `actions.json` – structured machine-readable output
   - `actions.txt` – formatted, human-friendly summary
6. ✅ The script logs success and prints the JSON to the console.

Core components:

- `read_notes()` – Reads raw notes from `notes.txt`
- `extract_actions()` – Calls the Groq LLM and parses the JSON response
- `save_outputs()` – Persists results to JSON and text files
- `main()` – Orchestrates the flow end-to-end

---

## 📦 Installation Guide

### 1. Prerequisites

- Python **3.10+** installed
- A Groq account and API key
- Git (optional, for cloning)

### 2. Clone the repository

```bash
git clone https://github.com/<your-username>/note-to-action-item-agent.git
cd note-to-action-item-agent
```

### 3. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate
```

### 4. Install dependencies

You can either create a `requirements.txt` or install directly:

```bash
pip install groq python-dotenv
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Never commit your real API keys to version control.

---

## ▶️ Usage Guide

1. **Prepare your notes**
   - Open `notes.txt`
   - Paste your meeting notes, conversation log, or brainstorming content
   - Save the file

2. **Run the agent**

   ```bash
   python agent.py
   ```

3. **Review the outputs**
   - `actions.json` – Structured JSON array of action items
   - `actions.txt` – Readable action list with owner, deadline, priority, and source context

4. **Integrate with your workflow (optional)**
   - Import `actions.json` into a task manager, PM tool, or custom automation
   - Share `actions.txt` in email, Slack, or documentation

---

## 📁 Project Folder Structure

```bash
.
├── agent.py        # Main script: reads notes, calls Groq, saves outputs
├── notes.txt       # Input: raw meeting notes
├── actions.json    # Output: structured action items (JSON)
├── actions.txt     # Output: human-readable action summary
├── .env            # Local environment variables (GROQ_API_KEY)
└── README.md       # Project documentation
```

---

## 📡 API Documentation

This project does **not** expose a public HTTP API. It is a CLI tool that internally uses the **Groq Chat Completions API**.

### Internal LLM Call

- **Model:** `llama-3.3-70b-versatile`
- **Endpoint:** `client.chat.completions.create(...)`
- **System prompt:** Enforces JSON-only output with the `actions` schema
- **User content:** Raw text from `notes.txt`
- **Temperature:** `0.2` for deterministic, task-focused outputs

The expected response is a JSON string matching the schema shown in the [Architecture / Workflow](#-architecture--workflow) section.

If you want to reuse the core logic programmatically, you can import and call `extract_actions(notes_text)` from `agent.py` in your own Python code.

---

## 🔮 Future Enhancements

- [ ] Add support for multiple input files or folders
- [ ] Export actions directly to tools like Jira, Trello, Linear, or Notion
- [ ] Add a simple web UI for uploading notes
- [ ] Support different prompt profiles (e.g., "strict tasks", "risks", "decisions")
- [ ] Add unit tests and CI workflow
- [ ] Containerize the app with Docker for easier deployment

Feel free to extend this list with ideas that fit your workflow.

---

## 🤝 Contribution Guidelines

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** in a clear, focused way
4. **Run tests / manual checks** (if applicable)
5. **Commit with a clear message**
   ```bash
   git commit -m "Add <short-description-of-change>"
   ```
6. **Push and open a Pull Request** describing the motivation and changes

Please keep the coding style consistent and avoid committing secrets.

---

## 📄 License

This project is licensed under the **MIT License**.  
You can update this section if you prefer a different license.

---

## 👤 Author

- **Name:** Sree
- **GitHub:** [https://github.com/Sree-8639](https://github.com/Sree-8639)
- **Email:** 23A81A6193@sves.org.in

If you use or extend this project, a ⭐ on GitHub is always appreciated!
