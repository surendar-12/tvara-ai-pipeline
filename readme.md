# Mock AI Pipeline

This repo contains a minimal demo for two tasks:
- A mock GPT-5-Nano + moderation pipeline
- A small RAG pipeline using Docling and FAISS

The focus is on clean structure and correct flow, with mocked components as instructed.

## Approach
- Task 1 reads text from a PDF, runs a mock moderation check, and passes it to a mock GPT module.
- Task 2 parses a PDF using Docling, chunks the text, embeds it using e5-small-v2, and retrieves relevant chunks from FAISS.

## Setup
```bash
pip install -r requirements.txt
python src/app.py <pdf_path>
python src/rag_demo.py
