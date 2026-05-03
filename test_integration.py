import unittest
from unittest.mock import patch
import main

class TestIntegration(unittest.TestCase):

    @patch('main.openai.Completion.create')
    def test_explain_code_success(self, mock_openai):
        mock_openai.return_value = {
            "choices": [
                {"text": "This code iterates over a list and prints each item."}
            ]
        }
        code_snippet = "for item in items: print(item)"
        result = main.explain_code(code_snippet)
        self.assertEqual(result, "This code iterates over a list and prints each item.")

    @patch('main.openai.Completion.create')
    def test_explain_code_rate_limit_error(self, mock_openai):
        from openai.error import RateLimitError
        mock_openai.side_effect = RateLimitError()
        code_snippet = "for item in items: print(item)"
        result = main.explain_code(code_snippet)
        self.assertIn("Error: Rate limit exceeded", result)

    @patch('main.openai.Completion.create')
    def test_explain_code_generic_error(self, mock_openai):
        from openai.error import OpenAIError
        mock_openai.side_effect = OpenAIError("Server error")
        code_snippet = "for item in items: print(item)"
        result = main.explain_code(code_snippet)
        self.assertIn("Error: Server error", result)

if __name__ == "__main__":
    unittest.main()