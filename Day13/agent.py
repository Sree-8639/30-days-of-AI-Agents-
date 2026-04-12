import json
import os
from datetime import date
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a Resume Optimization Agent.

Your goals:
- Rewrite resume bullets to emphasize measurable impact
- Align content with the target role
- Preserve factual accuracy (do not invent experience)
- Keep language ATS-friendly and concise

Return ONLY valid JSON with this schema:

{
  "optimized_experience": [],
  "optimized_skills": [],
  "summary_suggestion": ""
}
"""

def read_file(path):
    """Read text from file"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def optimize_resume(resume_text, job_text):
    """Send resume and job description to Groq model"""

    prompt = f"""
RESUME:
{resume_text}

TARGET ROLE:
{job_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown JSON formatting if returned
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)


def save_outputs(data):
    """Save optimized resume results"""

    with open("resume_optimized.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open("resume_optimized.txt", "w", encoding="utf-8") as f:
        f.write(f"Optimized Resume Output ({date.today()})\n")
        f.write("=" * 45 + "\n\n")

        f.write("Optimized Experience:\n")
        for bullet in data["optimized_experience"]:
            f.write(f"- {bullet}\n")

        f.write("\nOptimized Skills:\n")
        for skill in data["optimized_skills"]:
            f.write(f"- {skill}\n")

        f.write("\nSummary Suggestion:\n")
        f.write(data["summary_suggestion"] + "\n")


def main():

    resume_text = read_file("resume.txt")
    job_text = read_file("job.txt")

    optimized = optimize_resume(resume_text, job_text)
    save_outputs(optimized)

    print("✅ Resume optimization complete.")


if __name__ == "__main__":
    main()