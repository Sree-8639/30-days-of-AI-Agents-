import json
import os
from datetime import date
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a LinkedIn Post Ideation Agent.

Your job:
- Generate 5 distinct LinkedIn post ideas
- Each idea must be skimmable and hook-driven
- Optimize for professional audiences
- Avoid generic motivational content
- Suggest a discussion-oriented CTA

Return ONLY valid JSON with this schema:

{
  "ideas": [
    {
      "title": "",
      "hook": "",
      "core_message": "",
      "cta": "",
      "hashtags": []
    }
  ]
}
"""

def read_input(path="input.txt"):
    """Read topic input"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def generate_ideas(prompt_text):
    """Generate LinkedIn post ideas using Groq"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.5
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown formatting if present
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


def save_outputs(data):
    """Save generated ideas"""

    with open("ideas.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open("ideas.txt", "w", encoding="utf-8") as f:
        f.write(f"LinkedIn Post Ideas ({date.today()})\n")
        f.write("=" * 45 + "\n\n")

        for i, idea in enumerate(data["ideas"], 1):
            f.write(f"{i}. {idea['title']}\n")
            f.write(f"   Hook: {idea['hook']}\n")
            f.write(f"   Core Message: {idea['core_message']}\n")
            f.write(f"   CTA: {idea['cta']}\n")

            if idea["hashtags"]:
                f.write(f"   Hashtags: {' '.join(idea['hashtags'])}\n")

            f.write("\n")


def main():

    prompt_text = read_input()
    ideas = generate_ideas(prompt_text)
    save_outputs(ideas)

    print("✅ LinkedIn post ideas generated successfully.")
    print(f"Ideas generated: {len(ideas['ideas'])}")


if __name__ == "__main__":
    main()