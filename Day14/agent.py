import json
import os
from datetime import date
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a Grammar Correction Agent.

Rules:
- Correct grammar, spelling, and punctuation
- Improve clarity while preserving original meaning
- Do NOT rewrite content or change tone
- Do NOT add new information
- Keep edits minimal

Return ONLY valid JSON with this schema:

{
  "corrected_text": "",
  "notes": []
}
"""

def read_input(path="input.txt"):
    """Read text from input file"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def correct_text(raw_text):
    """Send text to Groq model for grammar correction"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": raw_text}
        ],
        temperature=0.1
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown JSON formatting if model returns it
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


def save_outputs(data):
    """Save results to JSON and TXT"""

    with open("corrected.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open("corrected.txt", "w", encoding="utf-8") as f:
        f.write(f"Corrected Text ({date.today()})\n")
        f.write("=" * 45 + "\n\n")
        f.write(data["corrected_text"] + "\n")


def main():

    raw_text = read_input()
    corrected = correct_text(raw_text)
    save_outputs(corrected)

    print("✅ Grammar correction complete.\n")
    print(corrected["corrected_text"])


if __name__ == "__main__":
    main()