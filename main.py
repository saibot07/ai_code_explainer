import openai
import os

def get_code_explanation(code_snippet):
    """Generate a code explanation using OpenAI GPT technology."""
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set!")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Explain the following Python code in detail:"},
                {"role": "user", "content": code_snippet}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("AI Code Explainer")
    code = input("Paste your Python code snippet here:\n")
    explanation = get_code_explanation(code)
    print("\nExplanation:\n", explanation)