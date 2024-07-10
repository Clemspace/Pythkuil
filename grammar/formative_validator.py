class FormativeValidator:
    def validate(self, parsed_slots):
        if not self.check_required_slots(parsed_slots):
            raise ValueError("Missing required slots")
        if not self.check_slot_consistency(parsed_slots):
            raise ValueError("Inconsistent slot values")
        if not self.check_grammatical_rules(parsed_slots):
            raise ValueError("Grammatical rules violated")

    def check_required_slots(self, parsed_slots):
        required_slots = {'II', 'III', 'IV'}  # At minimum, these slots should be present
        return all(slot in parsed_slots for slot in required_slots)

    def check_slot_consistency(self, parsed_slots):
        # This is where you'd implement checks for consistency between slots
        # For example, checking if the stem and function in Slot II and IV are compatible
        # This is a placeholder implementation
        return True

    def check_grammatical_rules(self, parsed_slots):
        # This is where you'd implement checks for adherence to Ithkuil's grammatical rules
        # For example, checking if the case in Slot IX is compatible with the function in Slot IV
        # This is a placeholder implementation
        return True