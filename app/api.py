from fastapi import FastAPI
from app.rag import ask_question

app = FastAPI()

@app.get("/chat")
def chat(q: str):
    return ask_question(q)
