# Blog Post Generator Agent 📝🤖  
*AI-powered blog writer that turns simple ideas into structured, publication-ready articles.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3%2070B-ff6f00.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#-license)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contribution-guidelines)

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

## 🧾 Project Overview

The **Blog Post Generator Agent** is a lightweight Python-based AI agent that generates well-structured blog posts from a simple text prompt.  
It uses the Groq LLaMA 3.3 70B model to create a JSON-structured article and a clean, human-readable text version ready for publishing.

You provide high-level instructions (topic, audience, tone, length), and the agent returns a complete blog post with sections, headings, and a conclusion.

---

## 💡 Problem Statement

Writing high-quality blog posts is time-consuming and often blocked by:

- Writer’s block and blank-page anxiety.
- Inconsistent structure and tone across articles.
- Repetitive formatting work (headings, sections, conclusions).

This project automates the **first draft** creation so writers, founders, and content creators can focus on reviewing, editing, and publishing instead of starting from scratch.

---

## ✨ Key Features

- 🧠 **AI-Powered Drafting** – Uses Groq’s LLaMA 3.3 70B model to generate complete blog posts.
- 📑 **Structured JSON Output** – Returns blog content in a clean JSON schema (`title`, `sections`, `conclusion`).
- 📰 **Readable Text Export** – Automatically formats and saves a human-friendly `.txt` version.
- 🎯 **Audience-Aware Writing** – Adapts tone and depth based on your instructions.
- 🔁 **Deterministic-ish Output** – Tuned temperature (`0.4`) for balanced creativity and consistency.
- 🖥️ **Simple CLI Workflow** – Run a single Python script to generate a blog post.
- 🔐 **Secure API Key Handling** – Uses `.env` file to store your `GROQ_API_KEY`.

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **LLM Provider:** Groq (LLaMA 3.3 70B – `llama-3.3-70b-versatile`)
- **Libraries:**
  - `groq` – official Groq Python client
  - `python-dotenv` – environment variable management
  - Standard library: `json`, `os`, `datetime`
- **Environment:** Local CLI script (no server required)

---

## 🔄 System Architecture / Workflow

High-level workflow:

1. **User Input**  
   - You write blog instructions (topic, style, audience, length, etc.) in `blog.txt`.

2. **Agent Initialization**  
   - `agent.py` loads `GROQ_API_KEY` from `.env` using `python-dotenv`.
   - A `Groq` client is instantiated.

3. **Prompt Construction**  
   - A system prompt (`SYSTEM_PROMPT`) instructs the model to:
     - Generate a structured blog.
     - Use a specific JSON schema.
     - Avoid fluff and stay concise.

4. **LLM Call**  
   - The script calls `client.chat.completions.create(...)` with:
     - `model="llama-3.3-70b-versatile"`
     - System + user messages.
     - **Temperature:** `0.4`.

5. **Post-Processing**  
   - Any Markdown code-fence wrappers around JSON are stripped.
   - The JSON string is parsed into a Python dict.

6. **Output Generation**  
   - `blog.json` – full JSON response (machine-readable).
   - `blog_output.txt` – formatted article:
     - Title
     - Section headers + content
     - Conclusion

7. **CLI Feedback**  
   - The script prints a success message and the generated blog title.

Simple diagram:

```text
blog.txt  ──▶ agent.py ──▶ Groq LLM ──▶ JSON response
   ▲                                  │
   │                                  ▼
   └──────── blog_output.txt ◀── blog.json
```

---

## 📥 Installation Guide

### 1. Prerequisites

- Python **3.10+**
- A **Groq API key** – sign up at https://groq.com/  
- Git (optional, if cloning from GitHub)

### 2. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 3. Create and Activate Virtual Environment (Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install groq python-dotenv
```

*(Optionally, add a `requirements.txt` with these packages for easier setup.)*

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Usage Guide

1. **Define Blog Instructions**

Edit `blog.txt` and describe what you want:

```text
Topic: Why AI agents will redefine productivity in 2026
Audience: Founders and tech professionals
Tone: Professional but friendly
Length: 1200–1500 words
Focus: Practical benefits, daily usage, and future impact
```

2. **Run the Agent**

```bash
python agent.py
```

3. **View Outputs**

- `blog.json` – structured content:
  - `title`
  - `sections` (array of `{ "header", "content" }`)
  - `conclusion`
- `blog_output.txt` – formatted blog ready for quick review or publishing.

4. **Iterate**

- Adjust instructions in `blog.txt`.
- Rerun `python agent.py` until you’re happy with the result.

---

## 📂 Project Folder Structure

```text
.
├── agent.py          # Main blog generator script
├── blog.txt          # User-provided instructions / prompt for the blog
├── blog.json         # Generated blog in JSON format (output)
├── blog_output.txt   # Generated blog in human-readable text format (output)
├── .env              # Environment variables (GROQ_API_KEY) - not committed
└── README.md         # Project documentation
```

---

## 📡 API Documentation

This project is a **CLI agent**, not a web API, but it does interact with the Groq Chat Completions API via the Python client.

### Internal LLM Call

Function: `generate_blog(blog_instructions: str) -> dict`

- **Request:**
  - **Model:** `llama-3.3-70b-versatile`
  - **Messages:**
    - `system`: Detailed instructions plus JSON schema.
    - `user`: Raw text from `blog.txt`.
  - **Temperature:** `0.4`

- **Response (Expected JSON Schema):

```json
{
  "title": "string",
  "sections": [
    {
      "header": "string",
      "content": "string"
    }
  ],
  "conclusion": "string"
}
```

If the model returns Markdown-wrapped JSON (e.g., ```json ... ```), the script strips the fences before parsing.

---

## 📊 Dataset Information

This is **not** an ML training project and does **not** use or bundle any datasets.

- No datasets are stored or processed beyond the plain-text instructions you provide in `blog.txt`.
- All intelligence comes from the Groq-hosted LLM.

---

## 🔮 Future Enhancements

Potential improvements:

- 🌐 Web UI for non-technical users (FastAPI / Streamlit).
- ⚙️ Configurable system prompts (per-audience / per-brand tone).
- 📂 Multiple post generation in a single run.
- 🌍 Multi-language blog support.
- 🧪 Unit tests and validation for JSON schema.
- 💾 Automatic export to Markdown / HTML.

---

## 🤝 Contribution Guidelines

Contributions are welcome! 🎉

1. **Fork** the repository.
2. **Create a branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/my-awesome-feature
   ```
3. Make your changes, keeping code clean and well-documented.
4. **Test** your changes locally.
5. **Open a Pull Request** with:
   - Clear description of the change.
   - Screenshots or examples if relevant.

Please keep commits focused and avoid bundling unrelated changes.

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.

---

## 👩‍💻 Author

**Anya Sree**

- 🌐 GitHub: [Sree-8639](https://github.com/Sree-8639)
- 📧 Email: [23A81A6193@sves.org.in](mailto:23A81A6193@sves.org.in)

If you use this agent in your workflow or extend it, feel free to reach out or open an issue/PR. 💬
