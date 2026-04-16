from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
import ollama

app = FastAPI()

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

# IMPORTANT: correct initialization
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(request: Request, log_input: str = Form(...)):
    ai_result = analyze_logs_with_ai(log_input)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": ai_result,
            "log_input": log_input
        }
    )