# 📚 Auto Book Publisher — Agentic AI Writing Pipeline

## Overview
An AI-powered book editing pipeline that:
- Scrapes public domain chapters 
- Rewrites content using local LLMs (Ollama + Gemma)
- Provides AI-powered review feedback
- Stores versions semantically (ChromaDB)
- Enables semantic search across versions

> ✅ **Internship Round-1 Submission Ready**  
> ✅ **100% Local Execution** (No API dependencies)  
> ✅ **Modular Agent Architecture**

---

## 🛠️ Technical Implementation

### Core Components
1. **Chapter Scraping**
   - Source: `https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1`
   - Tools: Playwright + BeautifulSoup
   - Outputs: 
     - `chapter_1.txt` (raw text)
     - `chapter_1.png` (screenshot)

2. **AI Writer Agent**
   - Model: `gemma:2b` via Ollama
   - Output: `chapter_1_writer.md` (modernized text)

3. **AI Reviewer Agent** 
   - Output: `chapter_1_reviewer.md` (improvement suggestions)

4. **Version Control**
   - ChromaDB storage with semantic search
   - Metadata tagging for all versions

---

## 📂 File Structure
auto_book_pub/
├── main.py # Scraping entry point
├── ai_flow.py # Full AI pipeline
├── agentic_pipeline.py # Agent-based workflow
├── scraper.py # Web scraping logic
├── agents/
│ └── ai_writer.py # LLM interaction logic
├── versions/
│ └── version_store.py # ChromaDB operations
├── human_edits/ # Optional human inputs
├── chapter_1.* # Generated files
└── requirements.txt # Dependencies

---

## 🚀 Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Initialize Ollama
ollama pull gemma:2b

# Run pipeline
python main.py         # Scrape chapter
python ai_flow.py      # Execute full AI workflow
python agentic_pipeline.py

## 🎯 Assignment Requirements Coverage
| Requirement | Implementation File | Status |
|-------------|---------------------|--------|
| Web Scraping | scraper.py | ✅ Fully Implemented |
| AI Writing | agents/ai_writer.py | ✅ Gemma 2B Integration |
| Human-in-the-Loop | agentic_pipeline.py | ✅ Editor Agent |
| Versioning | versions/version_store.py | ✅ ChromaDB Integration |