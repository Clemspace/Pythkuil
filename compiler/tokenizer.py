class Tokenizer:
    def __init__(self):
        self.word_types = {
            'formative': self._is_formative,
            'adjunct': self._is_adjunct,
            # Add other word types as needed
        }

    def tokenize(self, text):
        words = text.split()
        tokens = []
        for word in words:
            token_type = self._identify_token_type(word)
            tokens.append((word, token_type))
        return tokens

    def _identify_token_type(self, word):
        for type_name, check_function in self.word_types.items():
            if check_function(word):
                return type_name
        return 'unknown'

    def _is_formative(self, word):
        # TODO: Implement formative identification logic
        # This should check if the word follows formative structure
        pass

    def _is_adjunct(self, word):
        # TODO: Implement adjunct identification logic
        pass

    # Add other word type identification methods as needed