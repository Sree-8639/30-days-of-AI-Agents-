import json
import os
from datetime import date
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a Tone Rewriting Agent.

Rules:
- Rewrite the text to match the requested tone
- Preserve original meaning exactly
- Do NOT add or remove information
- Do NOT exaggerate emotion
- Keep output natural and professional

Return ONLY valid JSON with this schema:

{
  "rewritten_text": "",
  "tone_applied": ""
}
"""

def read_input(path="input.txt"):
    """Read input text file"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def rewrite_text(text):
    """Call Groq model to rewrite tone"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0.25
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown JSON formatting if present
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


def save_outputs(data):
    """Save results to files"""

    with open("rewritten.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open("rewritten.txt", "w", encoding="utf-8") as f:
        f.write(f"Tone-Rewritten Text ({date.today()})\n")
        f.write("=" * 45 + "\n\n")
        f.write(data["rewritten_text"] + "\n")


def main():

    raw = read_input()
    rewritten = rewrite_text(raw)
    save_outputs(rewritten)

    print("✅ Tone rewriting complete.\n")
    print(rewritten["rewritten_text"])


if __name__ == "__main__":
    main()