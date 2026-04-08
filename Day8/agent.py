import json
import os
from datetime import date
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Initialize Groq client using API key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a Note-to-Action Item Agent.

Your job:
- Extract ONLY actionable tasks from the notes
- Ignore ideas, opinions, or decisions without actions
- Identify owner if mentioned; otherwise use "Unassigned"
- Suggest a deadline if implied; otherwise "Not specified"
- Assign priority: Low, Medium, or High

Return ONLY valid JSON with this schema:

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
"""

def read_notes(path="notes.txt"):
    """Read meeting notes from file"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_actions(notes_text):
    """Call Groq LLM to extract action items"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": notes_text}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown json formatting if present
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


def save_outputs(data):
    """Save results to JSON and TXT files"""

    with open("actions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open("actions.txt", "w", encoding="utf-8") as f:
        f.write(f"Extracted Action Items ({date.today()})\n")
        f.write("=" * 45 + "\n\n")

        for i, a in enumerate(data["actions"], 1):
            f.write(f"{i}. {a['action']}\n")
            f.write(f"   Owner: {a['owner']}\n")
            f.write(f"   Deadline: {a['deadline']}\n")
            f.write(f"   Priority: {a['priority']}\n")
            f.write(f"   Source: {a['source_context']}\n\n")


def main():
    """Main program"""

    notes_text = read_notes()
    actions = extract_actions(notes_text)
    save_outputs(actions)

    print("✅ Action items extracted successfully.\n")
    print(json.dumps(actions, indent=2))


if __name__ == "__main__":
    main()