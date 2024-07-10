from utils.character_utils import get_char_pattern, is_vowel, is_consonant

class FormativeSlotIdentifier:
    def __init__(self):
        self.slot_patterns = {
            'I': r'^(h?w?)',
            'II': r'^([aeiouäëöü]+)',
            'III': r'^([^aeiouäëöü]+)',
            'IV': r'^([aeiouäëöü]+)',
            'V': r'^([^aeiouäëöü]+[aeiouäëöü]+)*',
            'VI': r'^([^aeiouäëöü]+)',
            'VII': r'^([aeiouäëöü]+[^aeiouäëöü]+)*',
            'VIII': r'^([aeiouäëöü][^aeiouäëöü])',
            'IX': r'^([aeiouäëöü]+)',
            'X': r'([^aeiouäëöü]+)$'
        }

    def identify_slots(self, formative):
        char_pattern = get_char_pattern(formative)
        slots = {}
        remaining = formative

        for slot, pattern in self.slot_patterns.items():
            match = re.match(pattern, remaining)
            if match:
                content = match.group(1)
                slots[slot] = content
                remaining = remaining[len(content):]

        return slots

    def validate_slot_sequence(self, slots):
        expected_sequence = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        actual_sequence = [slot for slot in expected_sequence if slot in slots]
        return actual_sequence == list(slots.keys())