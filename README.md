# RAG-based AI Chatbot (Agentic AI eBook)

## Overview
This project is a Retrieval-Augmented Generation (RAG) based AI chatbot that answers questions strictly using the Agentic AI eBook as its knowledge source.

---

## Tech Stack
- Python
- LangChain
- LangGraph
- FAISS
- HuggingFace Sentence Transformers
- FastAPI

---

## Architecture
1. Load and parse the Agentic AI PDF
2. Split text into chunks
3. Generate embeddings
4. Store embeddings in FAISS
5. Retrieve relevant chunks for a query
6. Generate answers strictly from retrieved context
7. Expose chatbot via FastAPI

---

## Setup Instructions

### Install dependencies
```bash
pip install -r requirements.txt
2. Ingest the PDF.
python app/ingest.py

3. Run the chatbot API
uvicorn app.api:app --reload

Usage

Open your browser and visit:

http://127.0.0.1:8000/chat?q=What is Agentic AI?

Sample Queries

What is Agentic AI?

How does Agentic AI differ from traditional AI?

What role do agents play in AI systems?

What are the limitations of Agentic AI?

How is Agentic AI used in real-world applications?

Notes

Answers are strictly grounded in the Agentic AI eBook

If the answer is not found, the system responds with "I don't know"

Free embeddings are used to avoid paid APIs
