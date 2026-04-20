import unittest
from unittest.mock import patch
import main

class TestCodeExplainer(unittest.TestCase):

    @patch("main.openai.Completion.create")
    @patch("os.getenv", return_value="fake_api_key")
    def test_explain_code_success(self, mock_env, mock_openai):
        mock_openai.return_value = {
            "choices": [{"text": "This is an if-else statement."}]
        }
        result = main.explain_code("if x > 0:\n    print('Positive')")
        self.assertEqual(result, "This is an if-else statement.")

    @patch("os.getenv", return_value=None)
    def test_explain_code_missing_key(self, mock_env):
        result = main.explain_code("if x > 0:\n    print('Positive')")
        self.assertEqual(result, "API Key not found. Please configure it.")

    @patch("main.openai.Completion.create", side_effect=Exception("API Error"))
    @patch("os.getenv", return_value="fake_api_key")
    def test_explain_code_api_failure(self, mock_env, mock_openai):
        result = main.explain_code("if x > 0:\n    print('Positive')")
        self.assertEqual(result, "An unexpected error occurred.")

if __name__ == "__main__":
    unittest.main()