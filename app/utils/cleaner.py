def clean_output(text: str):

    if not text:
        return ""

    # Remove junk patterns
    junk = [
        "```",
        "python",
        "Solution",
        "Example",
        "Output",
        "Question"
    ]

    for j in junk:
        text = text.replace(j, "")

    return text.strip()
