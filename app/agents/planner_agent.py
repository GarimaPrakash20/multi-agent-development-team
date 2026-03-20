from app.services.llm_service import generate


def plan_tasks(feature_request: str):
    try:
        prompt = f"""
You are a senior software architect.

Break the following feature into EXACTLY 5 clear development tasks.

Feature:
{feature_request}

Return ONLY a numbered list.
"""

        response = generate(prompt)

        if not response or len(response.strip()) == 0:
            raise ValueError("Empty LLM response")

        return response.strip()

    except Exception as e:
        print("❌ Task generation failed:", str(e))
        return "1. Define requirements\n2. Design API\n3. Implement logic\n4. Write tests\n5. Deploy"
