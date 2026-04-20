import openai

def explain_code(input_code):
    """ Function to get an explanation for the given Python code. """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"""Explain the following Python code:
{input_code}
""",
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

# Example usage
if __name__ == "__main__":
    code_sample = """
def add(a, b):
    return a + b
"""
    explanation = explain_code(code_sample)
    print("Code Explanation:", explanation)
