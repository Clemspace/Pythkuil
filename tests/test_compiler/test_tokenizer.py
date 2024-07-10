import unittest
from compiler.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize_simple_sentence(self):
        text = "Ithkuil word another_word"
        expected = [("Ithkuil", "unknown"), ("word", "unknown"), ("another_word", "unknown")]
        self.assertEqual(self.tokenizer.tokenize(text), expected)

    def test_tokenize_formative(self):
        # This is a placeholder test. You'll need to replace with a valid Ithkuil formative
        formative = "exampleformative"
        expected = [(formative, "formative")]
        self.assertEqual(self.tokenizer.tokenize(formative), expected)

    def test_tokenize_adjunct(self):
        # This is a placeholder test. You'll need to replace with a valid Ithkuil adjunct
        adjunct = "exampleadjunct"
        expected = [(adjunct, "adjunct")]
        self.assertEqual(self.tokenizer.tokenize(adjunct), expected)

    # Add more tests as you implement more token types and edge cases

if __name__ == '__main__':
    unittest.main()