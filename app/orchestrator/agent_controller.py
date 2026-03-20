from app.agents.planner_agent import plan_tasks
from app.agents.developer_agent import generate_code
from app.agents.reviewer_agent import review_code
from app.agents.tester_agent import generate_tests
from app.agents.docs_agent import generate_docs
from app.utils.cleaner import clean_output

def is_valid(text):
    return text and len(text.strip()) > 20

def build_feature(request):

    tasks = clean_output(plan_tasks(request))
    if not is_valid(tasks):
        return {"error": "Task generation failed"}
    print("TASKS:", tasks)

    code = clean_output(generate_code(tasks))
    if not is_valid(code):
        return {"error": "Code generation failed"}    
    print("CODE:", code)

    review = clean_output(review_code(code))
    if not is_valid(review):
        return {"error": "Review generation failed"}
    print("REVIEW:", review)

    tests = clean_output(generate_tests(code))
    if not is_valid(tests):
        return {"error": "Tests generation failed"}
    print("TESTS:", tests)

    docs = clean_output(generate_docs(code))
    if not is_valid(docs):
        return {"error": "Docs generation failed"}
    print("DOCS:", docs)

    return {
        "tasks": tasks.strip(),
        "code": code.strip(),
        "review": review.strip(),
        "tests": tests.strip(),
        "documentation": docs.strip()
    }
