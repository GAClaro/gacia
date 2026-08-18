from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .agent import ask_agent


app = FastAPI(
    title="GACIA",
    description="Agente de IA baseado em documentos",
    version="0.1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/ask")
def ask(question: Question):
    answer = ask_agent(question.question)

    return {
        "question": question.question,
        "answer": answer
    }