# agentic_pipeline.py

from agents.ai_writer import ai_writer, ai_reviewer
from versions.version_store import store_version
import json

class AIWriterAgent:
    def process(self, text):
        print("🧠 AI Writer processing using simulated LLM...")
        output = ai_writer(text)
        store_version("chapter_1_writer", output, step="writer")
        return output

class AIReviewerAgent:
    def process(self, text):
        print("🧠 AI Reviewer analyzing and adding feedback...")
        output = ai_reviewer(text)
        store_version("chapter_1_reviewer", output, step="reviewer")
        return output

class HumanEditorAgent:
    def process(self, text):
        print("🧑 Human Editor applying final manual edits...")
        with open("human_edits/chapter_1_edited_by_human.md", "r", encoding="utf-8") as f:
            final_output = f.read()

        store_version("chapter_1_final", final_output, step="human_editor")

        # Optional: print feedback summary
        try:
            with open("human_edits/chapter_1_feedback.json", "r", encoding="utf-8") as f:
                feedback = json.load(f)
                print(f"📝 Feedback loaded ({len(feedback['feedback'])} notes):")
                for note in feedback["feedback"]:
                    print("   -", note)
        except FileNotFoundError:
            print("⚠️  Feedback file not found. Skipping RL notes.")

        return final_output

def run_pipeline():
    with open("chapter_1.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    writer = AIWriterAgent()
    
    reviewer = AIReviewerAgent()
    editor = HumanEditorAgent()

    x = writer.process(raw_text)
    y = reviewer.process(x)
    z = editor.process(y)

    print("✅ Agentic pipeline complete.")

if __name__ == "__main__":
    run_pipeline()
