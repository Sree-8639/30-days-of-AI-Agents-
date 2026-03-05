# 🧠 Smart Reminder Agent

A Python-based intelligent agent that reads tasks from a CSV file and automatically generates smart, priority-based reminder schedules — exported as both JSON and human-readable text.

---

## 📖 Project Description

The **Smart Reminder Agent** is a lightweight command-line tool designed to help users stay on top of their tasks and deadlines. Given a list of tasks with deadlines, priorities, and context, the agent intelligently determines *when* to send reminders based on the urgency of each task.

- **High-priority** tasks trigger reminders at **7, 3, 1, and 0 days** before the deadline.
- **Medium-priority** tasks trigger reminders at **3 and 1 day(s)** before the deadline.
- **Low-priority** tasks trigger a reminder **1 day** before the deadline.

Only future or current-day reminders are generated, ensuring you never see stale notifications.

---

## ✨ Features

- **Priority-Based Scheduling** — Automatically determines reminder frequency based on task priority (`high`, `medium`, `low`).
- **CSV Task Input** — Reads tasks from a simple, easy-to-edit `tasks.csv` file.
- **Dual Output Formats** — Generates reminders in both structured **JSON** (`reminders.json`) and human-readable **plain text** (`reminders.txt`).
- **Smart Date Filtering** — Only produces reminders for today or future dates; past reminders are automatically excluded.
- **Sorted Reminder Timeline** — All reminders are sorted chronologically for a clear, actionable schedule.
- **Context Tagging** — Each task supports a `context` field (e.g., `work`, `personal`) for easy categorization.

---

## 🛠️ Technology Stack

| Technology | Purpose                          |
|------------|----------------------------------|
| Python 3   | Core programming language        |
| `csv`      | Parsing task input from CSV      |
| `json`     | Exporting reminders to JSON      |
| `datetime` | Date parsing, arithmetic & filtering |

> No external dependencies required — runs entirely on the Python standard library.

---

## 📁 Project Structure

```
Smart Reminder Agent/
│
├── agent.py           # Main script — reads tasks, generates & exports reminders
├── tasks.csv          # Input file — list of tasks with deadlines and priorities
├── reminders.json     # Output — generated reminders in JSON format
├── reminders.txt      # Output — generated reminders in plain text format
└── README.md          # Project documentation
```

---

## ⚙️ Installation / Setup Instructions

### Prerequisites

- **Python 3.7+** installed on your system.

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/smart-reminder-agent.git
   cd smart-reminder-agent
   ```

2. **No additional packages to install** — the project uses only Python's standard library.

3. **Prepare your tasks** — Edit `tasks.csv` with your own tasks (see format below).

---

## 🚀 Usage / How to Run the Project

1. **Add your tasks** to `tasks.csv` in the following format:

   ```csv
   task,deadline,priority,context
   Submit tax documents,2025-04-15,high,personal
   Prepare quarterly report,2025-03-25,high,work
   Book car service,2025-03-30,medium,personal
   Buy birthday gift,2025-03-28,low,personal
   Follow up with vendor,2025-03-22,medium,work
   ```

   | Column     | Description                                      |
   |------------|--------------------------------------------------|
   | `task`     | Name/description of the task                     |
   | `deadline` | Due date in `YYYY-MM-DD` format                  |
   | `priority` | `high`, `medium`, or `low`                       |
   | `context`  | Optional tag (e.g., `work`, `personal`)          |

2. **Run the agent:**

   ```bash
   python agent.py
   ```

3. **Check the output files:**
   - `reminders.json` — structured reminder data
   - `reminders.txt` — human-readable reminder schedule

---

## 📋 Example Output

### Console

```
Smart reminders generated.
Total reminders: 12
```

### reminders.txt

```
Smart Reminder Schedule
========================================

2025-03-21 → Reminder: 'Follow up with vendor' is due on 2025-03-22.
2025-03-25 → Reminder: 'Prepare quarterly report' is due on 2025-03-25.
2025-03-27 → Reminder: 'Buy birthday gift' is due on 2025-03-28.
2025-03-27 → Reminder: 'Book car service' is due on 2025-03-30.
2025-03-29 → Reminder: 'Book car service' is due on 2025-03-30.
2025-04-08 → Reminder: 'Submit tax documents' is due on 2025-04-15.
2025-04-12 → Reminder: 'Submit tax documents' is due on 2025-04-15.
2025-04-14 → Reminder: 'Submit tax documents' is due on 2025-04-15.
2025-04-15 → Reminder: 'Submit tax documents' is due on 2025-04-15.
```

### reminders.json (excerpt)

```json
[
  {
    "task": "Submit tax documents",
    "context": "personal",
    "priority": "high",
    "deadline": "2025-04-15",
    "remind_on": "2025-04-08",
    "message": "Reminder: 'Submit tax documents' is due on 2025-04-15."
  }
]
```

---

## 🔮 Future Improvements

- [ ] **Email / SMS Notifications** — Integrate with email or SMS APIs to send real-time reminders.
- [ ] **Recurring Tasks** — Support tasks that repeat daily, weekly, or monthly.
- [ ] **GUI / Web Dashboard** — Build a visual interface to manage tasks and view upcoming reminders.
- [ ] **Database Backend** — Replace CSV with SQLite or another database for scalable task storage.
- [ ] **Natural Language Input** — Allow users to add tasks using plain English (e.g., *"Remind me to submit taxes by April 15"*).
- [ ] **Calendar Integration** — Sync reminders with Google Calendar, Outlook, or iCal.
- [ ] **Custom Reminder Rules** — Let users define their own reminder intervals per priority level.

---

## 🤝 Contributing Guidelines

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push to your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** with a clear description of your changes.

### Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style conventions.
- Write clear, descriptive commit messages.
- Test your changes before submitting a PR.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

You are free to use, modify, and distribute this project with attribution.

---

## 👤 Author

**Sree-8639**

- GitHub: [@Sree-8639](https://github.com/Sree-8639)

---

> *Stay productive. Never miss a deadline.* ⏰
