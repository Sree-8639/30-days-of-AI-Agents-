# Grammar Correction Agent ✍️✨

An automated grammar correction agent powered by Groq's LLM, designed to clean up grammar, spelling, and punctuation in plain-text files while preserving the original tone and intent.

---

## 🔖 Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Groq](https://img.shields.io/badge/LLM-Groq-yellowgreen)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture / Workflow](#-system-architecture--workflow)
- [Installation Guide](#-installation-guide)
- [Usage Guide](#-usage-guide)
- [Project Folder Structure](#-project-folder-structure)
- [API Documentation](#-api-documentation)
- [Dataset Information](#-dataset-information)
- [Screenshots / Demo](#-screenshots--demo)
- [Future Enhancements](#-future-enhancements)
- [Contribution Guidelines](#-contribution-guidelines)
- [License](#-license)
- [Author](#-author)

---

## 📌 Project Overview

**Project Name:** Grammar Correction Agent  
**Description:** A simple command-line tool that reads raw text from a file, sends it to a Groq LLM for grammar correction, and saves both JSON and human-readable outputs.

This agent is built to be minimal, reliable, and easy to integrate into larger workflows or automation pipelines.

---

## 🧩 Problem Statement

Writing error-free English is challenging, especially in fast-paced environments such as:

- Drafting emails, reports, or documentation under time pressure
- Preparing text for publications, blogs, or academic submissions
- Cleaning up content generated from speech-to-text or OCR tools

This project provides a small, scriptable utility that:

- Automatically corrects grammar, spelling, and punctuation
- Improves clarity while preserving meaning and tone
- Produces both machine-friendly (JSON) and human-friendly (TXT) outputs

---

## ⭐ Key Features

- ✅ **Grammar, spelling, and punctuation correction** using a Groq LLM
- ✅ **Minimal changes** – preserves tone and intent; no rewriting
- ✅ **JSON output** with corrected text and notes
- ✅ **Readable text output** with timestamped header
- ✅ **Simple file-based workflow** using `input.txt` and generated outputs

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **LLM Provider:** Groq (via `groq` Python client)
- **Environment Management:** `python-dotenv`
- **Core Dependencies:**
  - `groq`
  - `python-dotenv`

> Note: Install exact versions as needed in your environment or requirements file.

---

## 🧠 System Architecture / Workflow

High-level workflow:

1. User writes or pastes raw text into `input.txt`.
2. The script loads the Groq API key from the `.env` file.
3. The agent sends the raw text and a system prompt to the Groq chat completion API.
4. The model returns JSON with the corrected text and optional notes.
5. The script saves:
   - `corrected.json` – structured JSON with `corrected_text` and `notes`.
   - `corrected.txt` – human-readable corrected text with date header.
6. The corrected text is printed to the console.

---

## 📦 Installation Guide

### 1️⃣ Prerequisites

- Python 3.10 or higher installed
- A Groq API key
- Basic command-line access (Windows, macOS, or Linux)

### 2️⃣ Clone or Download the Project

```bash
# Using git
git clone <YOUR_REPO_URL>
cd 14.Grammar\ correction\ agent
```

Or download the folder and open it in your editor / terminal.

### 3️⃣ Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

Create a `requirements.txt` (if not already provided) or install directly:

```bash
pip install groq python-dotenv
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ Never commit your real API keys to version control.

---

## 🚀 Usage Guide

1. **Add your text** to `input.txt` in the project root.
2. **Run the agent**:

```bash
python agent.py
```

3. On success, you will see:

- `corrected.json` – JSON result from the model
- `corrected.txt` – formatted corrected text with date
- Corrected text printed in the terminal

### Example

`input.txt`:

```text
This is an example sentence with bad gramar and punctuations it should be fixed.
```

After running `python agent.py`, `corrected.txt` might look like:

```text
Corrected Text (2026-03-15)
=============================================

This is an example sentence with bad grammar and punctuation that should be fixed.
```

---

## 📁 Project Folder Structure

```bash
14.Grammar correction agent/
├── agent.py          # Main grammar correction script
├── input.txt         # Input text file to be corrected
├── corrected.json    # JSON output (generated)
├── corrected.txt     # Human-readable corrected text (generated)
├── .env              # Environment variables (Groq API key)
└── README.md         # Project documentation
```

---

## 📡 API Documentation

This project does **not** expose a public HTTP API; instead, it acts as a **client** of the Groq chat completion API.

### Groq Chat Completion Usage (Simplified)

The core call in `agent.py` looks like:

```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": raw_text}
    ],
    temperature=0.1
)
```

The model is instructed to return **only valid JSON** of the form:

```json
{
  "corrected_text": "...",
  "notes": []
}
```

The script then parses this JSON and writes it to `corrected.json` and `corrected.txt`.

---

## 📊 Dataset Information

This project does **not** ship with a dataset. It operates on **user-provided free-form text** in `input.txt`.

If you adapt this for ML workflows (e.g., benchmarking corrections), you can:

- Feed sentences or documents from a dataset into `input.txt` programmatically.
- Capture and store the model's corrections from `corrected.json` for analysis.

---

## 🖼 Screenshots / Demo

You can enhance this section with your own assets. For now, suggested placeholders:

- Terminal usage screenshot
- Before/after comparison screenshot

Example structure:

```markdown
![CLI Demo](docs/images/cli-demo.png)
![Before vs After](docs/images/before-after.png)
```

---

## 🔮 Future Enhancements

Planned or potential improvements:

- 🧪 Add unit tests for file I/O and JSON validation
- 🌐 Wrap the agent in a simple web UI or REST API
- 📂 Support batch processing of multiple files
- 🌍 Multi-language grammar correction (if supported by the model)
- 📝 Option to output change annotations (diff-style)

---

## 🤝 Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes with clear commit messages
4. Open a Pull Request with a descriptive title and summary

Please ensure your changes are:

- Consistent with the existing coding style
- Free of secrets/API keys
- Documented where necessary

---

## 📄 License

This project is licensed under the **MIT License**. You may modify and distribute it as permitted by the license terms.

---

## 👩‍💻 Author

**Name:** Anya Sree  
**GitHub:** [@Sree-8639](https://github.com/Sree-8639)  
**Email:** [23A81A6193@sves.org.in](mailto:23A81A6193@sves.org.in)

If you find this project useful, consider giving it a ⭐ on GitHub!