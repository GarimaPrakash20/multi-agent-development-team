from app.services.llm_service import generate

def generate_tests(code: str):
    prompt = f"""
Write pytest test cases for this code.

Rules:
- Only return Python test code
- No explanation

Code:
{code}

Tests:
"""

    return generate(prompt)
