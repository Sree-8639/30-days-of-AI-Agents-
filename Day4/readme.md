# 📧 Email Summarization Agent

An AI-powered agent that automatically reads, analyzes, and summarizes emails — extracting key points, action items, deadlines, and urgency levels using the Groq LLM API.

---

## 📌 Problem Statement

Professionals receive a high volume of emails daily, making it time-consuming to identify critical information, deadlines, and action items buried within lengthy threads. Manually parsing each email leads to missed tasks and delayed responses.

The **Email Summarization Agent** solves this by leveraging AI to instantly distill emails into structured, actionable summaries — saving time and ensuring nothing important is overlooked.

---

## ✨ Features

- **Concise Summaries** — Generates a 2–3 sentence summary of any email.
- **Key Point Extraction** — Identifies and lists the most important points.
- **Action Item Detection** — Extracts who needs to do what.
- **Deadline & Meeting Tracking** — Pulls out all dates, deadlines, and scheduled events.
- **Urgency Classification** — Classifies emails as **High**, **Medium**, or **Low** urgency.
- **Dual Output Formats** — Saves results as both structured JSON and human-readable TXT.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Groq API** | LLM inference (LLaMA 3.3 70B) |
| **python-dotenv** | Environment variable management |
| **JSON / Regex** | Output parsing and formatting |

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- A [Groq API key](https://console.groq.com/)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Sree-8639/30-days-of-AI-Agents-.git
   cd 30-days-of-AI-Agents-/Day\ 4
   ```

2. **Install dependencies**

   ```bash
   pip install groq python-dotenv
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Add your email**

   Paste the email content you want to summarize into `email.txt`.

5. **Run the agent**

   ```bash
   python agent.py
   ```

---

## 🚀 Usage

1. Place the raw email text inside `email.txt`.
2. Run `python agent.py`.
3. The agent will:
   - Read the email from `email.txt`
   - Send it to the Groq LLM for analysis
   - Save the structured summary to `summary.json`
   - Save a human-readable summary to `summary.txt`
   - Print the result to the console

### Example Output (JSON)

```json
{
  "summary": "The Q1 project timeline has been updated with a new deadline...",
  "key_points": [
    "Updated project timeline",
    "New prototype delivery deadline: March 10"
  ],
  "action_items": [
    "Design team: finalize assets by March 5",
    "Engineering team: prioritize API integration this week"
  ],
  "deadlines": [
    "March 5: design assets deadline",
    "March 10: initial prototype delivery"
  ],
  "urgency": "High"
}
```

---

## 📁 Project Structure

```
Email-Summarization-Agent/
├── agent.py          # Main agent script (reads email, calls LLM, saves output)
├── email.txt         # Input file — paste your email content here
├── summary.json      # Output — structured JSON summary
├── summary.txt       # Output — human-readable text summary
├── .env              # Environment variables (GROQ_API_KEY) — not tracked by Git
└── readme.md         # Project documentation
```

---

## 🔮 Future Enhancements

- [ ] Batch processing — summarize multiple emails from a folder
- [ ] Gmail / Outlook API integration for direct inbox access
- [ ] Web-based UI dashboard for viewing summaries
- [ ] Email categorization (e.g., Finance, HR, Engineering)
- [ ] Sentiment analysis on email tone
- [ ] Automated email reply drafting based on extracted action items
- [ ] Support for email attachments and inline content parsing

---

## 👤 Author

**Sree-8639**

- GitHub: [github.com/Sree-8639](https://github.com/Sree-8639)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Built with ❤️ using Python and Groq AI
