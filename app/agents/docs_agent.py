from app.services.llm_service import generate

def generate_docs(code: str):
    prompt = f"""
Write API documentation.

Include:
- Endpoints
- Example requests

Be concise.

Code:
{code}

Documentation:
"""

    return generate(prompt)
