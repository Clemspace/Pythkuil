from compiler.word_analyzer import IthkuilWordAnalyzer
from compiler.slot_identifier import FormativeSlotIdentifier
from morphology.slot_parser import SlotParser
from grammar.formative_validator import FormativeValidator

class FormativeParser:
    def __init__(self):
        self.analyzer = IthkuilWordAnalyzer()
        self.slot_identifier = FormativeSlotIdentifier()
        self.slot_parser = SlotParser()
        self.validator = FormativeValidator()

    def parse(self, formative):
        if not self.analyzer.is_formative(formative):
            raise ValueError("Not a formative")

        identified_slots = self.slot_identifier.identify_slots(formative)
        
        if not self.slot_identifier.validate_slot_sequence(identified_slots):
            raise ValueError("Invalid slot sequence")

        parsed_slots = {}
        for slot_name, content in identified_slots.items():
            parsed_slots[slot_name] = self.slot_parser.parse_slot(slot_name, content)

        self.validator.validate(parsed_slots)

        return parsed_slots