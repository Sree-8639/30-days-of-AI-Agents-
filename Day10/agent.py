import csv
import json
from datetime import datetime
from collections import defaultdict


def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def read_habits(path="habits.csv"):
    records = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            # handle different column name styles safely
            habit = row.get("habit") or row.get("Habit")
            date_val = row.get("date") or row.get("Date")
            completed = row.get("completed") or row.get("Completed")
            notes = row.get("notes") or row.get("Notes") or ""

            records.append({
                "habit": habit,
                "date": parse_date(date_val),
                "completed": completed.lower() == "yes",
                "notes": notes
            })

    return records


def analyze_habits(records):

    habits = defaultdict(list)

    for r in records:
        habits[r["habit"]].append(r)

    analysis = {}

    for habit, entries in habits.items():

        entries.sort(key=lambda x: x["date"])

        total = len(entries)
        completed = sum(1 for e in entries if e["completed"])

        consistency = round((completed / total) * 100, 1)

        # calculate current streak
        streak = 0
        for e in reversed(entries):
            if e["completed"]:
                streak += 1
            else:
                break

        missed_days = [
            e["date"].isoformat() for e in entries if not e["completed"]
        ]

        insight = (
            "Strong habit consistency."
            if consistency >= 75
            else "Habit needs reinforcement."
        )

        recommendation = (
            "Keep the habit as-is."
            if consistency >= 75
            else "Reduce difficulty or change timing."
        )

        analysis[habit] = {
            "total_days": total,
            "completed_days": completed,
            "consistency_percent": consistency,
            "current_streak": streak,
            "missed_days": missed_days,
            "insight": insight,
            "recommendation": recommendation
        }

    return analysis


def main():

    records = read_habits()
    results = analyze_habits(records)

    # Save JSON
    with open("habits.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Save TXT summary
    with open("habits.txt", "w", encoding="utf-8") as f:
        f.write("Habit Tracking Summary\n")
        f.write("=" * 40 + "\n\n")

        for habit, r in results.items():

            f.write(f"Habit: {habit}\n")
            f.write(f"Consistency: {r['consistency_percent']}%\n")
            f.write(f"Current Streak: {r['current_streak']} days\n")

            missed = ", ".join(r["missed_days"]) if r["missed_days"] else "None"

            f.write(f"Missed Days: {missed}\n")
            f.write(f"Insight: {r['insight']}\n")
            f.write(f"Recommendation: {r['recommendation']}\n\n")

    print("✅ Habit analysis complete.")
    print(f"Tracked habits: {len(results)}")


if __name__ == "__main__":
    main()