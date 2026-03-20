# 🚀 Autonomous Multi-Agent AI Software Development Team

An AI-powered system that simulates a **real-world software development team** using multiple specialized agents (Planner, Developer, Reviewer, QA, and Documentation).

This project demonstrates how **LLMs can collaborate as autonomous agents** to transform a feature request into production-ready artifacts — including code, tests, and documentation.

---

## 🧠 Overview

Given a simple feature request, the system automatically:

1. 📋 Breaks it into development tasks (Planner Agent)  
2. 💻 Generates code (Developer Agent)  
3. 🔍 Reviews code for issues (Reviewer Agent)  
4. 🧪 Creates test cases (QA Agent)  
5. 📚 Generates documentation (Docs Agent)  

---

## 🏗️ Architecture

User Request → Planner → Developer → Reviewer → QA → Docs

---

## ⚙️ Tech Stack

- Backend: FastAPI  
- LLM: Phi-2 (via HuggingFace Transformers)  
- Language: Python 3.12  
- Server: Uvicorn  
- Architecture: Multi-Agent System  

---

## 📂 Project Structure

app/
├── agents/
├── orchestrator/
├── routes/
├── services/
├── utils/
└── main.py

---

## 🚀 Getting Started

### 1. Clone the repository

git clone <your-repo-url>
cd multi-agent-development-team

### 2. Create virtual environment

python -m venv myvenv
source myvenv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the server

uvicorn app.main:app --reload

---

## 📡 API Usage

POST /build-feature

Request:
{
  "request": "Build a FastAPI todo API with CRUD endpoints"
}

---

## 🧩 Features

- Multi-agent collaboration  
- LLM-powered reasoning  
- End-to-end automation  
- Structured code reviews  

---

## 👩‍💻 Author

Garima Singh
