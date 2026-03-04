
# 📅 Calendar Conflict Detection Agent

## Overview
This project analyzes a calendar schedule and automatically detects **conflicts between events** such as:
- Overlapping meetings
- Events scheduled without sufficient buffer time

It then generates structured reports suggesting possible resolutions.

The system reads events from a CSV calendar file and outputs the detected conflicts in both **JSON** and **text report** formats.

---

# 📂 Project Structure

```
project/
│
├── agent.py           # Main program for conflict detection
├── calendar.csv       # Input calendar events
│
├── conflicts.json     # Structured machine‑readable conflict report
└── conflicts.txt      # Human‑readable conflict report
```

---

# ⚙️ Requirements

- Python 3.8+
- No external libraries required (uses standard Python libraries)

Used modules:

- csv
- json
- datetime
- dataclasses
- typing

---

# 📥 Input File

## calendar.csv

Contains calendar events with metadata.

Example structure:

```
title,start_time,end_time,priority,type,flexible
Team Sync,2026-03-01 09:00,2026-03-01 10:00,high,meeting,no
Client Call,2026-03-01 09:30,2026-03-01 10:30,high,call,no
Code Review,2026-03-01 10:30,2026-03-01 11:30,medium,work,yes
```

### Field Description

| Field | Description |
|------|-------------| title | Name of the event |
| start_time | Start datetime (YYYY-MM-DD HH:MM) |
| end_time | End datetime |
| priority | low / medium / high |
| type | Event category |
| flexible | yes / no (whether event can be moved) |

---

# 🧠 Conflict Detection Logic

The agent checks events sequentially and identifies two types of conflicts:

### 1️⃣ Overlap Conflict
Occurs when one event starts **before the previous event ends**.

Example:

```
Event A: 09:00 - 10:00
Event B: 09:30 - 10:30
```

### 2️⃣ No Buffer Conflict
Occurs when there is **less than 10 minutes gap** between two events.

Example:

```
Event A: 10:00 - 11:00
Event B: 11:05 - 12:00
```

Buffer required:

```
BUFFER_MINUTES = 10
```

---

# ⚠️ Conflict Severity

Severity is determined based on event priority.

| Priority | Severity |
|--------|----------| High priority involved | high |
| Otherwise | medium |

Priority mapping used in the code:

```
PRIORITY_MAP = {
    "low": 1,
    "medium": 2,
    "high": 3
}
```

---

# 💡 Resolution Suggestions

The system suggests actions automatically:

| Situation | Suggestion |
|----------|------------| Higher priority event exists | Reschedule lower priority event |
| Both events flexible | Shorten or reschedule one |
| Both fixed events | Requires human decision |

---

# 📤 Output Files

## conflicts.json

Machine‑readable structured output.

Example:

```
[
  {
    "event_a": "Team Sync",
    "event_b": "Client Call",
    "type": "overlap",
    "severity": "high",
    "suggestion": "Requires human decision"
  }
]
```

---

## conflicts.txt

Human‑readable report.

Example:

```
Calendar Conflict Report
========================================

- Conflict between Team Sync and Client Call
  Type: overlap, Severity: high
  Suggested Action: Requires human decision
```

---

# ▶️ How to Run

1️⃣ Place your calendar file in the same folder.

```
calendar.csv
```

2️⃣ Run the program:

```
python agent.py
```

3️⃣ The script will generate:

```
conflicts.json
conflicts.txt
```

Console output:

```
Conflict analysis complete.
Detected X conflicts.
```

---

# 🧩 Key Components in agent.py

## Event Dataclass

Represents a calendar event.

```
@dataclass
class Event:
    title: str
    start: datetime
    end: datetime
    priority: int
    event_type: str
    flexible: bool
```

---

## Main Functions

### read_calendar()
Reads events from CSV and converts them into Event objects.

### detect_conflicts()
Detects overlapping or no‑buffer events.

### suggest_resolution()
Provides automated resolution suggestions.

### main()
Coordinates the full workflow:
- Read events
- Detect conflicts
- Generate reports

---

# 📊 Example Conflicts Detected

- Team Sync ↔ Client Call → Overlap
- Client Call ↔ Code Review → No buffer
- Deep Work Block ↔ Lunch → Overlap

---

# 🚀 Possible Improvements

Future enhancements could include:

- Google Calendar integration
- Automatic rescheduling suggestions
- Visualization of schedules
- Email or Slack alerts
- Machine learning prioritization

---

# 👨‍💻 Author

Calendar Conflict Detection Agent  
Python automation project for schedule analysis.
