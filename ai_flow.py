# ai_flow.py

from agents.ai_writer import ai_writer, ai_reviewer
from versions.version_store import store_version, search_versions, rank_with_rl_stub

def run_ai_pipeline():
    print("📖 Loading original chapter...")
    with open("chapter_1.txt", "r", encoding="utf-8") as f:
        original = f.read()

    # Step 1: Simulated AI Writer (LLM)
    print("🧠 Running AI Writer (simulated Gemini)...")
    writer_output = ai_writer(original)
    with open("chapter_1_writer.md", "w", encoding="utf-8") as f:
        f.write(writer_output)

    # Step 2: AI Reviewer
    print("🧠 Running AI Reviewer (text analysis)...")
    reviewer_output = ai_reviewer(writer_output)
    with open("chapter_1_reviewer.md", "w", encoding="utf-8") as f:
        f.write(reviewer_output)

    print("✅ AI writing and review complete!")

    # Step 3: Store both versions in ChromaDB
    store_version("chapter_1_writer", writer_output, step="writer")
    store_version("chapter_1_reviewer", reviewer_output, step="reviewer")

    # Step 4: Semantic Search
    print("\n🔍 Semantic search for keyword: 'sentence'")
    results = search_versions("sentence")

    docs = results['documents'][0]
    ranked = rank_with_rl_stub("sentence", docs)

    for i, doc in enumerate(ranked, 1):
        print(f"\n🔎 Top {i} result:\n", doc[:120], "...")


if __name__ == "__main__":
    run_ai_pipeline()
