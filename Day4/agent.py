import json
from datetime import date
import re
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(api_key=api_key)

# System Prompt
SYSTEM_PROMPT = """
You are an Email Summarization Agent.

Tasks:
1. Summarize the email in 2–3 sentences.
2. Extract all key points.
3. Extract action items (who should do what).
4. Extract ALL deadlines, meetings, and time references.
5. Classify urgency:
   - High → urgent deadlines, schedule changes, immediate tasks
   - Medium → normal project updates
   - Low → informational emails.

Return ONLY valid JSON with this schema:

{
  "summary": "",
  "key_points": [],
  "action_items": [],
  "deadlines": [],
  "urgency": ""
}
"""

# Read Email File
def read_email(path="email.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Summarize Email using Groq
def summarize_email(email_text):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": email_text}
        ],
        temperature=0.2
    )

    text = response.choices[0].message.content.strip()

    # Extract JSON safely
    json_match = re.search(r"\{.*\}", text, re.S)

    if json_match:
        return json.loads(json_match.group())

    raise ValueError("No valid JSON found in model response")

# Save outputs
def save_outputs(data):

    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open("summary.txt", "w", encoding="utf-8") as f:

        f.write(f"Email Summary ({date.today()})\n")
        f.write("=" * 40 + "\n\n")

        f.write("SUMMARY:\n")
        f.write(data["summary"] + "\n\n")

        f.write("KEY POINTS:\n")
        for p in data["key_points"]:
            f.write(f"- {p}\n")

        f.write("\nACTION ITEMS:\n")
        for a in data["action_items"]:
            f.write(f"- {a}\n")

        f.write("\nDEADLINES:\n")
        for d in data["deadlines"]:
            f.write(f"- {d}\n")

        f.write(f"\nURGENCY: {data['urgency']}\n")

# Main function
def main():

    email_text = read_email()

    result = summarize_email(email_text)

    save_outputs(result)

    print("✅ Email summarized successfully\n")
    print(json.dumps(result, indent=2))

# Run Script
if __name__ == "__main__":
    main()
