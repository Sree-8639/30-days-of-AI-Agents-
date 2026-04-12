# Resume Optimization Agent 
> AI-powered CLI tool that rewrites resume content to better match a target job description.

A lightweight, prompt-engineered agent that takes a resume and a job description as input, then uses the Groq LLM API to generate optimized bullet points, skills, and a summary tailored to the role.

---

## 🏷️ Badges

> Update the repository/branch names as needed.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-None-lightgrey.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

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
- [Dataset Information](#-dataset-information-if-ml-project)
- [Screenshots / Demo](#-screenshots--demo)
- [Future Enhancements](#-future-enhancements)
- [Contribution Guidelines](#-contribution-guidelines)
- [License](#-license)
- [Author](#-author)

---

## 🧩 Project Overview

The **Resume Optimization Agent** is a command-line tool that helps job seekers tailor their resumes to specific job descriptions.

Given:

- a raw resume (`resume.txt`)
- a target job description (`job.txt`)

The agent sends both to a Groq LLM model, which returns:

- optimized experience bullet points
- an updated skill list
- a concise, ATS-friendly summary suggestion

Outputs are written to:

- `resume_optimized.json` — structured JSON output
- `resume_optimized.txt` — human-readable text version

---

## ❓ Problem Statement

Job seekers often struggle to:

- rewrite their resumes for each application
- highlight measurable impact and relevant experience
- keep wording clear, concise, and ATS-friendly

Manually tailoring resumes to every role is time-consuming and error-prone.

The **Resume Optimization Agent** automates the heavy lifting by:

- aligning resume content with the target job description
- emphasizing quantifiable achievements
- preserving factual accuracy while improving clarity and focus

---

## 🌟 Key Features

- ✨ **Role-aware optimization** – Adjusts resume bullets and skills to match the target job description.
- 🚀 **Impact-focused rewriting** – Emphasizes measurable results and clear outcomes in experience bullets.
- 💡 **ATS-friendly suggestions** – Produces concise, keyword-rich content suitable for resume screening systems.
- 📦 **Structured outputs** – Saves both JSON and plain-text outputs for easy review and integration.

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **LLM Provider:** Groq API (`llama-3.3-70b-versatile` model)
- **Environment Management:** `python-dotenv` for loading `.env` variables
- **Standard Library:** `json`, `os`, `datetime`

> No database is required; all inputs/outputs are file-based.

---

## 🧬 System Architecture / Workflow

High-level workflow:

1. 🔐 Load the Groq API key from `.env` via `python-dotenv`.
2. 📄 Read user-provided `resume.txt` and `job.txt` from the project root.
3. 🧠 Send a structured system prompt and combined input to the `llama-3.3-70b-versatile` model via Groq's Chat Completions API.
4. 🧾 Parse the returned JSON (validated/cleaned if wrapped in Markdown code fences).
5. 💾 Save the optimized content to:
   - `resume_optimized.json`
   - `resume_optimized.txt` (human-readable, dated output)
6. ✅ Print a confirmation message in the terminal.

Simple conceptual diagram:

```text
[resume.txt]        [job.txt]
     \                 /
      \               /
       --> Resume Optimization Agent (agent.py)
                  |
                  v
   [Groq LLM API: llama-3.3-70b-versatile]
                  |
                  v
[resume_optimized.json]   [resume_optimized.txt]
```

---

## 📥 Installation Guide

### 1. Prerequisites

- Python **3.10+** installed
- A **Groq API key** (sign up at Groq and create an API token)
- Git (optional but recommended)

### 2. Clone the repository

```bash
git clone https://github.com/your-username/resume-optimization-agent.git
cd "resume optimization agent"
```

> Adjust the path/name above if your repository name is different.

### 3. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install groq python-dotenv
```

> If you add a `requirements.txt` later, you can instead run:
>
> ```bash
> pip install -r requirements.txt
> ```

### 5. Configure environment variables

Create a `.env` file in the project root with your Groq key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Keep this file private and **never** commit real keys to Git.

---

## ▶️ Usage Guide

1. Prepare your input files in the project root:
   - `resume.txt` – plain-text version of your resume
   - `job.txt` – plain-text job description / target role

2. Run the agent:

```bash
python agent.py
```

3. After completion, check the outputs:

- `resume_optimized.json` – machine-readable JSON with fields:
  - `optimized_experience`: list of bullet strings
  - `optimized_skills`: list of skill strings
  - `summary_suggestion`: a single summary paragraph
- `resume_optimized.txt` – formatted text with sections for experience, skills, and summary

4. Copy the improved bullets, skills, and summary into your resume document (Word, Google Docs, LaTeX, etc.).

> Tip: Re-run with different job descriptions to generate tailored versions for multiple roles.

---

## 📁 Project Folder Structure

Current minimal structure:

```text
.
├─ agent.py              # Main script that orchestrates reading inputs, calling Groq, and saving outputs
├─ job.txt               # Input file containing the target job description / role
├─ resume.txt            # Input file containing the candidate's resume in plain text
├─ .env                  # Local environment file storing GROQ_API_KEY (not committed)
└─ README.md             # Project documentation (this file)
```

Generated at runtime:

```text
resume_optimized.json     # JSON output with optimized experience, skills, and summary
resume_optimized.txt      # Human-readable, dated text output
```

You can extend the structure with additional modules (e.g., `utils/`, `tests/`) as the project grows.

---

## 📡 API Documentation

This project does **not** expose a public HTTP API. Instead, it uses the **Groq Chat Completions API** internally.

### Internal LLM Call

- **Model:** `llama-3.3-70b-versatile`
- **Endpoint Type:** Chat completion via Groq Python client
- **Messages:**
  - `system`: Instructions defining the Resume Optimization Agent behavior and JSON schema
  - `user`: Concatenated `RESUME` and `TARGET ROLE` text
- **Response:**

```json
{
  "optimized_experience": ["..."],
  "optimized_skills": ["..."],
  "summary_suggestion": "..."
}
```

If the model wraps JSON in Markdown code fences, the script strips them before parsing.

---

## 📊 Dataset Information (if ML project)

This project **does not train a model** and does not ship with a dataset.

- The LLM is accessed as a managed API (Groq).
- User resumes and job descriptions are provided ad hoc via `resume.txt` and `job.txt`.

If you later add local training or fine-tuning, document your datasets and preprocessing steps here.

---

## 🚧 Future Enhancements

Potential improvements and next steps:

- Support multiple input formats (PDF/DOCX parsing instead of plain text)
- Add a simple GUI or web frontend for non-technical users
- Allow configuration of tone (formal, casual, leadership-focused, etc.)
- Multi-language support for non-English resumes
- Batch processing for multiple job descriptions or resumes
- Integration with LinkedIn profile export / import

---

## 🤝 Contribution Guidelines

Contributions are welcome! 🎉

1. **Fork** the repository.
2. **Create** a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make changes** with clear, descriptive commit messages:

   ```bash
   git commit -m "Add: short description of your change"
   ```

4. **Push** your branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request** describing:
   - What you changed
   - Why it improves the project
   - Any related issues or limitations

Please ensure:

- Code is readable and follows Python best practices.
- Secrets (like API keys) are never committed.
- Existing functionality still works (run a quick manual test).

---

## 📜 License

Currently, this project does **not specify a formal license** ("None").

> If you intend to make this open source, consider adding a `LICENSE` file (e.g., MIT or Apache-2.0) and updating this section and the badge at the top accordingly.

---

## 👤 Author

**Anya Sree**

- 🌐 GitHub: [Sree-8639](https://github.com/Sree-8639)
- 📧 Email: [23A81A6193@sves.org.in](mailto:23A81A6193@sves.org.in)

If you find this project helpful, please consider giving it a ⭐ on GitHub!
