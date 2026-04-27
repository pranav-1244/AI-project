from fastapi import FastAPI
from pydantic import BaseModel
import ollama
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LogRequest(BaseModel):
    log_input: str


def analyze_logs_with_ai(log_data: str):
    prompt = f"""
You are a senior DevOps engineer.

Analyze the following logs:
{log_data}

Give:
1. Issue
2. Root cause
3. Fix
4. Severity
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


@app.post("/analyze")
async def analyze(request: LogRequest):
    result = analyze_logs_with_ai(request.log_input)
    return {"result": result}




@app.get("/")
async def home():
    return FileResponse("frontend/index.html")