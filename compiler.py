from typing import List
from grammar.word_types import IthkuilWord
from grammar.parsers.ithkuil_parser import IthkuilParser

def parse_sentence(sentence: str) -> List[IthkuilWord]:
    words = sentence.split()  # This assumes words are space-separated
    parsed_words = []
    for word in words:
        try:
            parsed_word = IthkuilParser.parse_word(word)
            parsed_words.append(parsed_word)
        except ValueError as e:
            print(f"Error parsing word '{word}': {e}")
    return parsed_words

class IthkuilCompiler:
    @staticmethod
    def compile(text: str) -> List[IthkuilWord]:
        sentences = text.split('.')  # This assumes sentences are separated by periods
        compiled_text = []
        for sentence in sentences:
            compiled_text.extend(parse_sentence(sentence.strip()))
        return compiled_text

# Usage
if __name__ == "__main__":
    text = "Your Ithkuil text here."
    compiler = IthkuilCompiler()
    compiled_words = compiler.compile(text)
    for word in compiled_words:
        print(word.describe())