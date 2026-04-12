# 🧠 Personal Knowledge Base Agent

> **An AI-powered personal knowledge base that ingests your notes, understands them semantically, and answers your questions using Retrieval-Augmented Generation (RAG).**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3.3-70B-blueviolet)
![Groq](https://img.shields.io/badge/Groq-API-orange?logo=groq)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

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
- [Configuration](#%EF%B8%8F-configuration)
- [Future Enhancements](#-future-enhancements)
- [Contribution Guidelines](#-contribution-guidelines)
- [License](#-license)
- [Author](#-author)

---

## 📖 Project Overview

The **Personal Knowledge Base Agent** transforms your plain-text notes into a searchable, AI-powered knowledge base. It reads notes from a text file, generates hash-based vector embeddings, stores them in a local JSON knowledge store, and uses semantic similarity retrieval combined with a large language model (LLaMA 3.3 70B via Groq) to answer natural language questions grounded in your personal notes.

No cloud vector database required — everything runs locally with a lightweight, dependency-minimal design.

---

## 🎯 Problem Statement

We all accumulate a wealth of personal notes — meeting takeaways, learning snippets, ideas, and productivity tips — but retrieving the right piece of information at the right time is difficult. Traditional keyword search fails when you don't remember the exact words you used.

This agent solves that by enabling **semantic Q&A over your personal notes**, so you can ask questions in natural language and get accurate, context-grounded answers.

---

## ✨ Features

| Feature                       | Description                                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------------|
| 📄 **Note Ingestion**         | Reads notes line-by-line from a plain `notes.txt` file                                       |
| 🔢 **Hash-Based Embedding**   | Generates lightweight vector embeddings using MD5 hashing (no external embedding API needed)  |
| 🗃️ **Local Knowledge Store**  | Persists embeddings and metadata in a local `knowledge.json` file                            |
| 🔍 **Semantic Retrieval**     | Retrieves the most relevant notes using cosine similarity                                    |
| 🤖 **RAG-Powered Answers**    | Sends retrieved context to LLaMA 3.3 70B (via Groq) for grounded, accurate answers           |
| ⚡ **Fast Inference**          | Leverages Groq's ultra-fast LPU inference engine                                             |
| 🪶 **Minimal Dependencies**   | Only requires `numpy` and `openai` — no heavy ML frameworks                                 |

---

## 🛠️ Tech Stack

| Category         | Technology                                      |
|------------------|--------------------------------------------------|
| **Language**     | Python 3.9+                                      |
| **LLM**          | LLaMA 3.3 70B Versatile                          |
| **LLM Provider** | Groq API (OpenAI-compatible)                     |
| **Embeddings**   | Custom hash-based vectorization (MD5 + NumPy)    |
| **Storage**      | JSON (local file-based)                          |
| **Libraries**    | `openai`, `numpy`                                |

---

## 🏗️ Architecture / Workflow

```
┌──────────────┐
│  notes.txt   │   ← Your personal notes (one per line)
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│  Note Ingestion   │   ← Reads and cleans each line
└──────┬───────────┘
       │
       ▼
┌──────────────────────┐
│  Hash-Based Embedding │   ← Tokenize → MD5 hash → sparse vector
└──────┬───────────────┘
       │
       ▼
┌──────────────────┐
│  knowledge.json  │   ← Stores text + embedding + timestamp
└──────┬───────────┘
       │
       ▼ (on query)
┌──────────────────────────┐
│  Semantic Retrieval       │   ← Cosine similarity → top-K notes
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  LLaMA 3.3 via Groq API      │   ← Generates answer from context
└──────┬───────────────────────┘
       │
       ▼
┌──────────────┐
│   Answer     │   ← Grounded response to the user
└──────────────┘
```

---

## 📦 Installation Guide

### Prerequisites

- **Python 3.9+** installed
- A **Groq API key** ([get one here](https://console.groq.com))

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/personal-knowledge-base-agent.git
   cd personal-knowledge-base-agent
   ```

2. **Install dependencies**
   ```bash
   pip install numpy openai
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Add your notes**

   Edit `notes.txt` and add your personal notes (one note per line):
   ```text
   AI agents are autonomous systems that can plan, reason, and act toward goals.
   RAG systems combine retrieval with generation to produce grounded responses.
   Daily prioritization improves productivity by focusing on high-impact work.
   ```

---

## 🚀 Usage Guide

### Run the Agent

```bash
python agent.py
```

### Example Session

```
Ingesting notes...
Knowledge base ready.

Ask a question: What are AI agents?

Answer:
AI agents are autonomous systems that can plan, reason, and act toward goals.
```

### How It Works (Step-by-Step)

1. The agent reads all lines from `notes.txt`
2. Each note is converted into a 1024-dimensional hash-based vector
3. Vectors and metadata are saved to `knowledge.json`
4. You type a natural language question
5. The query is embedded and compared against stored vectors via cosine similarity
6. The top 3 most relevant notes are retrieved
7. These notes are sent as context to LLaMA 3.3 70B via the Groq API
8. The model generates a grounded answer using **only** the provided notes

---

## 📂 Project Folder Structure

```
Personal Knowledge Base Agent/
│
├── agent.py            # Main application — ingestion, retrieval, and Q&A logic
├── notes.txt           # Input notes file (one note per line)
├── knowledge.json      # Auto-generated knowledge store with embeddings
├── .env                # Environment variables (GROQ_API_KEY) — not committed
└── README.md           # Project documentation
```

---

## ⚙️ Configuration

| Parameter      | Location         | Default                     | Description                                          |
|----------------|------------------|-----------------------------|------------------------------------------------------|
| `GROQ_API_KEY` | `.env`           | —                           | Your Groq API key (required)                         |
| `CHAT_MODEL`   | `agent.py`       | `llama-3.3-70b-versatile`   | LLM model to use for answer generation               |
| `HASH_DIM`     | `agent.py`       | `1024`                      | Dimensionality of the hash-based embedding vectors   |
| `top_k`        | `retrieve()`     | `3`                         | Number of top relevant notes to retrieve per query   |
| `temperature`  | `answer_query()` | `0.2`                       | LLM temperature (lower = more deterministic)         |

---

## 🔮 Future Enhancements

- 🔄 **Incremental ingestion** — Add new notes without re-embedding everything
- 📂 **Multi-file support** — Ingest notes from multiple files or directories
- 🧩 **Chunking strategies** — Split longer documents into overlapping chunks
- 🌐 **Web UI** — Add a Streamlit or Gradio frontend for interactive Q&A
- 🗄️ **Vector database integration** — Support ChromaDB, FAISS, or Pinecone for scalable storage
- 🔐 **Transformer embeddings** — Optionally use sentence-transformers for higher-quality embeddings
- 💬 **Conversational memory** — Support multi-turn conversations with chat history
- 🏷️ **Tagging & categorization** — Auto-tag notes by topic for filtered retrieval

---

## 🤝 Contribution Guidelines

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes with clear messages
   ```bash
   git commit -m "feat: add multi-file ingestion support"
   ```
4. **Push** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** with a description of your changes

### Guidelines

- Follow PEP 8 style conventions
- Add docstrings for new functions
- Test your changes before submitting
- Keep PRs focused and atomic

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025

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
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**Your Name**

- 🔗 GitHub: [github.com/your-username](https://github.com/your-username)

---

<p align="center">
  Made with ❤️ and 🤖 AI
</p>
