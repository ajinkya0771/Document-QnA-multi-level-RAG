from fastapi import FastAPI
from pydantic import BaseModel
from rag.query_engine import get_rag_answer

app = FastAPI(title="Enterprise RAG API")

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(payload: QueryRequest):
    answer, sources = get_rag_answer(payload.question)
    return {
        "question": payload.question,
        "answer": answer,
        "sources": sources
    }
