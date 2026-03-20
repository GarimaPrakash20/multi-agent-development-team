from app.services.llm_service import generate

def review_code(code: str):

    prompt = f"""
You are a senior code reviewer.

Review the following code and identify:
- bugs
- performance issues
- bad practices

Code:
{code}
"""

    return generate(prompt)
