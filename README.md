🚀 Autonomous Multi-Agent AI Software Development Team

An AI-powered system that simulates a real-world software development team using multiple specialized agents (Planner, Developer, Reviewer, QA, and Documentation).

This project demonstrates how LLMs can collaborate as autonomous agents to transform a feature request into production-ready artifacts — including code, tests, and documentation.

🧠 Overview

Given a simple feature request, the system automatically:

📋 Breaks it into development tasks (Planner Agent)

💻 Generates code (Developer Agent)

🔍 Reviews code for issues (Reviewer Agent)

🧪 Creates test cases (QA Agent)

📚 Generates documentation (Docs Agent)

🏗️ Architecture
User Request
     ↓
Planner Agent → Tasks
     ↓
Developer Agent → Code
     ↓
Reviewer Agent → Issues (JSON)
     ↓
QA Agent → Tests
     ↓
Docs Agent → Documentation
⚙️ Tech Stack

Backend: FastAPI

LLM: Phi-2 (via HuggingFace Transformers)

Language: Python 3.12

Server: Uvicorn

Architecture: Multi-Agent System

📂 Project Structure
app/
├── agents/
│   ├── planner_agent.py
│   ├── developer_agent.py
│   ├── reviewer_agent.py
│   ├── qa_agent.py
│   └── docs_agent.py
│
├── orchestrator/
│   └── agent_controller.py
│
├── routes/
│   └── build_feature.py
│
├── services/
│   └── llm.py
│
├── utils/
│   └── cleaner.py
│
└── main.py
🚀 Getting Started
1. Clone the repository
git clone <your-repo-url>
cd multi-agent-development-team
2. Create virtual environment
python -m venv myvenv
source myvenv/bin/activate   # Mac/Linux
myvenv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the server
uvicorn app.main:app --reload
📡 API Usage
Endpoint
POST /build-feature
Request Body
{
  "request": "Build a FastAPI todo API with CRUD endpoints"
}
Sample Response
{
  "tasks": "1. Define Todo model...\n2. Create FastAPI app...",
  "code": "from fastapi import FastAPI ...",
  "review": {
    "bugs": [],
    "performance_issues": [],
    "security_issues": [],
    "best_practices": []
  },
  "tests": "def test_create_todo(): ...",
  "documentation": "API endpoints:\n- GET /todos\n..."
}
🧩 Key Features

🤖 Multi-agent collaboration (Planner, Developer, Reviewer, QA, Docs)

🧠 LLM-powered reasoning for each development stage

📦 End-to-end automation from idea → code → tests → docs

🔍 Structured code review output (JSON)

⚡ FastAPI-based scalable backend

⚠️ Known Limitations

LLM outputs may occasionally be inconsistent or verbose

Requires prompt tuning for better code quality

No persistent memory between agents (yet)

🔮 Future Enhancements

✅ Add vector memory (RAG) for context awareness

✅ Integrate with GitHub PR automation

✅ Add UI dashboard for agent workflow

✅ Improve code generation reliability

✅ Add execution sandbox for generated code

💡 Why This Project Stands Out

This project showcases:

Real-world AI system design (not just API calls)

Understanding of multi-agent orchestration

Practical use of LLMs in software engineering workflows

Strong backend engineering with FastAPI + modular design

👩‍💻 Author

Garima Singh
AI/Backend Developer | Building AI-powered developer tools

⭐ If you found this useful

Give it a ⭐ on GitHub and share your feedback!
