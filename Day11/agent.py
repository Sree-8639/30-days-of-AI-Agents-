import json
import os
from datetime import date
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a Blog Post Generator Agent.

Your job:
- Generate a well-structured blog post
- Adapt tone and depth to the target audience
- Use clear section headers
- Keep writing concise and readable
- Avoid fluff and repetition

Return ONLY valid JSON with this schema:

{
  "title": "",
  "sections": [
    {
      "header": "",
      "content": ""
    }
  ],
  "conclusion": ""
}
"""


def read_blog_input(path="blog.txt"):
    """Read blog instructions"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def generate_blog(blog_instructions):
    """Generate blog post using Groq"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": blog_instructions}
        ],
        temperature=0.4
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown JSON formatting if present
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


def save_outputs(blog):
    """Save blog to JSON and TXT"""

    with open("blog.json", "w", encoding="utf-8") as f:
        json.dump(blog, f, indent=2)

    with open("blog_output.txt", "w", encoding="utf-8") as f:
        f.write(f"{blog['title']}\n")
        f.write("=" * len(blog["title"]) + "\n\n")

        for s in blog["sections"]:
            f.write(f"{s['header']}\n")
            f.write("-" * len(s["header"]) + "\n")
            f.write(s["content"] + "\n\n")

        f.write("Conclusion\n")
        f.write("-" * 10 + "\n")
        f.write(blog["conclusion"] + "\n")


def main():

    instructions = read_blog_input()
    blog = generate_blog(instructions)
    save_outputs(blog)

    print("✅ Blog post generated successfully.")
    print("Title:", blog["title"])


if __name__ == "__main__":
    main()