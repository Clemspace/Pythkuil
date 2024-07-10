from .tokenizer import Tokenizer
from .formative_parser import FormativeParser
from .syntax_analyzer import SyntaxAnalyzer
from .semantic_analyzer import SemanticAnalyzer
from .error_reporter import ErrorReporter

class IthkuilCompiler:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.formative_parser = FormativeParser()
        self.syntax_analyzer = SyntaxAnalyzer()
        self.semantic_analyzer = SemanticAnalyzer()
        self.error_reporter = ErrorReporter()

    def compile(self, text):
        tokens = self.tokenizer.tokenize(text)
        parsed_formatives = []

        for token, token_type in tokens:
            if token_type == 'formative':
                parsed = self.formative_parser.parse(token)
                parsed_formatives.append(parsed)
            # Handle other token types as needed

        self.syntax_analyzer.analyze(parsed_formatives)
        self.semantic_analyzer.analyze(parsed_formatives)

        if self.error_reporter.has_errors():
            return self.error_reporter.get_errors()
        else:
            return parsed_formatives

    def generate(self, parsed_formatives):
        # TODO: Implement generation of Ithkuil text from parsed formatives
        pass