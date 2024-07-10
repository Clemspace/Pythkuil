from utils.character_utils import is_vowel, is_consonant

class IthkuilWordAnalyzer:
    def analyze_word(self, word):
        if self.is_formative(word):
            return self.analyze_formative(word)
        elif self.is_adjunct(word):
            return self.analyze_adjunct(word)
        else:
            raise ValueError(f"Unknown word type: {word}")

    def is_formative(self, word):
        # This is a basic check. You might need more sophisticated rules.
        return (len(word) >= 3 and
                is_consonant(word[0]) and
                is_vowel(word[-1]) and
                any(is_consonant(c) for c in word[1:-1]))

    def is_adjunct(self, word):
        # This is a placeholder. Implement actual adjunct identification rules.
        return not self.is_formative(word)

    def analyze_formative(self, formative):
        if self.is_shortened_formative(formative):
            return self.parse_shortened_formative(formative)
        else:
            return {'type': 'standard_formative', 'word': formative}

    def is_shortened_formative(self, formative):
        # Implement logic to identify if it's a shortened formative
        # This is a placeholder implementation
        return False

    def parse_shortened_formative(self, formative):
        # Implement logic to parse shortened formatives
        # This is a placeholder implementation
        return {'type': 'shortened_formative', 'word': formative}

    def analyze_adjunct(self, adjunct):
        # Implement logic to analyze adjuncts
        # This is a placeholder implementation
        return {'type': 'adjunct', 'word': adjunct}