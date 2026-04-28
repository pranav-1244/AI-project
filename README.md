# 🚀 AI DevOps Agent (Local LLM Powered)

An AI-powered web application that analyzes system/application logs and provides intelligent insights such as root cause, fixes, and severity — built using FastAPI and a local LLM via Ollama.

---

## 🧠 Overview

This project demonstrates how to build a real-world AI-powered DevOps assistant using:

* Local LLM (no API cost)
* Backend API (FastAPI)
* Separate frontend (HTML + JavaScript)
* GitHub-based workflow (branching, PR, merge)

---

## 🏗️ Architecture

```
Frontend (HTML + JS)
        ↓
FastAPI Backend (API)
        ↓
Ollama (Local AI Model)
```

---

## ⚙️ Tech Stack

* **Backend**: Python (FastAPI)
* **Frontend**: HTML, CSS, JavaScript
* **AI Model**: Ollama (Mistral / Phi)
* **Environment**: WSL (Ubuntu)
* **Version Control**: Git + GitHub

---

## 📂 Project Structure

```
AI-project/
│
├── app.py                # FastAPI backend
├── frontend/
│   └── index.html       # Frontend UI
├── venv/                # Virtual environment (ignored)
├── .gitignore
└── README.md
```

---

## 🔧 Requirements

Make sure you have the following installed:

* Python 3.10+
* pip
* Git
* WSL (Ubuntu recommended)
* Ollama

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/pranav-1244/AI-project.git
cd AI-project
```

---

### 2️⃣ Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn ollama pydantic
```

---

### 4️⃣ Install and run Ollama

Install Ollama:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Pull a model (recommended: fast model):

```
ollama pull phi
```

Start Ollama service:

```
ollama serve
```

---

### 5️⃣ Run backend server

```
uvicorn app:app --reload
```

---

### 6️⃣ Run frontend

Open in browser:

```
frontend/index.html
```

---

## 🚀 Usage

1. Paste logs into the input box
2. Click **Analyze**
3. View AI-generated insights

---

## 🧪 Sample Logs

```
ERROR: Failed to connect to database
Timeout after 30 seconds
```

---

## ⚡ Features

* AI-powered log analysis
* Local LLM (no external API)
* FastAPI backend
* Separate frontend (API-based)
* Improved UI with loading state
* GitHub workflow (branch → PR → merge)

---

## 🔥 Future Improvements

* Chat-style UI (like ChatGPT)
* File upload support
* Streaming responses
* React frontend
* AWS deployment
* Multi-agent system

---

## 🧠 Learning Outcomes

* Building AI-powered applications
* Backend API design (FastAPI)
* Frontend-backend separation
* Local LLM integration
* GitHub workflow (branches, PRs)
* Debugging real-world issues

---

## 👨‍💻 Author

**Pranav**

---

## 📜 License

This project is for learning and educational purposes.
