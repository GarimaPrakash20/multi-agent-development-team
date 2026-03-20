from app.services.llm_service import generate

def generate_code(tasks: str):
    prompt = f"""
Write a FastAPI application based on these tasks.

Tasks:
{tasks}

Rules:
- Return ONLY Python code
- No explanation
- No markdown
- No comments outside code

Code:
"""

    return generate(prompt)
