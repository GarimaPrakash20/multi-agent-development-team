from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    max_new_tokens=300,
    do_sample=False,
    temperature=0.2,
    return_full_text=False
)

def generate(prompt: str):

    result = generator(prompt)

    text = result[0]["generated_text"]

    response = text.replace(prompt, "").strip()

    stop_words = ["---","Example:","Output:","Question","Solution"]

    for word in stop_words:
        if word in text:
            text = text.split(word)[0]

    return text.strip()
