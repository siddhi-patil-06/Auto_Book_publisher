# agents/ai_writer.py
import requests

MODEL_NAME = "gemma:2b"

def call_llm(prompt: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
        )
        return response.json()["response"]
    except Exception as e:
        print(f"❌ gemma:2b call failed: {e}")
        return f"[Fallback LLM]: {prompt[:500].upper()}"

def ai_writer(text: str) -> str:
    prompt = (
        "You're a skilled writer. Rewrite this chapter in fluent, modern, and engaging style:\n\n" + text
    )
    return "# AI Writer Output\n\n" + call_llm(prompt)

def ai_reviewer(text: str) -> str:
    prompt = (
        "You're an expert reviewer. Provide suggestions to improve this chapter. List in bullet points:\n\n" + text
    )
    return "# AI Reviewer Feedback\n\n" + call_llm(prompt)
