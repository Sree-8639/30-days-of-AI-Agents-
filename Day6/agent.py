import json
import os
import re
import hashlib
import numpy as np
from openai import OpenAI
from datetime import date


def load_env(path=".env"):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


load_env()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in environment or .env file.")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

CHAT_MODEL = "llama-3.3-70b-versatile"
HASH_DIM = 1024


def read_notes(path="notes.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def embed_texts(texts):
    def tokenize(text):
        return re.findall(r"[a-zA-Z0-9_]+", text.lower())

    vectors = []
    for text in texts:
        v = np.zeros(HASH_DIM, dtype=float)
        tokens = tokenize(text)
        for token in tokens:
            h = hashlib.md5(token.encode("utf-8")).hexdigest()
            idx = int(h, 16) % HASH_DIM
            v[idx] += 1.0
        norm = np.linalg.norm(v)
        if norm > 0:
            v = v / norm
        vectors.append(v.tolist())
    return vectors


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def store_knowledge(chunks, embeddings):
    records = []
    for text, emb in zip(chunks, embeddings):
        records.append({
            "text": text,
            "embedding": emb,
            "created": date.today().isoformat()
        })
    with open("knowledge.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)
    return records


def load_knowledge():
    with open("knowledge.json", "r", encoding="utf-8") as f:
        return json.load(f)


def retrieve(query, records, top_k=3):
    query_emb = embed_texts([query])[0]
    scored = []
    for r in records:
        score = cosine_similarity(query_emb, r["embedding"])
        scored.append((score, r["text"]))
    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]


def answer_query(query, contexts):
    prompt = f"""
Answer the following question using ONLY the provided notes.

Notes:
{chr(10).join(contexts)}

Question:
{query}
"""
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content


def main():
    print("Ingesting notes...")
    chunks = read_notes()
    embeddings = embed_texts(chunks)
    records = store_knowledge(chunks, embeddings)

    print("Knowledge base ready.")
    query = input("\nAsk a question: ")
    top_contexts = retrieve(query, records)
    answer = answer_query(query, top_contexts)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
