import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Pythkuil.morphology.slots.slot_i import SlotI, ConcatenationStatus
from Pythkuil.morphology.slots.slot_ii import SlotII, Version, Stem
from Pythkuil.morphology.slots.slot_iii import SlotIII
from Pythkuil.morphology.slots.slot_iv import SlotIV, Function, Specification, Context
from Pythkuil.morphology.slots.slot_v import SlotV
from Pythkuil.morphology.slots.slot_vi import SlotVI
from Pythkuil.morphology.slots.slot_vii import SlotVII
from Pythkuil.morphology.slots.slot_viii import SlotVIII
from Pythkuil.morphology.slots.slot_ix import SlotIX, Illocution, Validation
from Pythkuil.morphology.slots.slot_x import SlotX, Stress, Relation
from Pythkuil.grammar.word_types.formative import Formative
from Pythkuil.lexicon.root_database import RootDatabase
from Pythkuil.grammar.cases import Case
from Pythkuil.morphology.ca_complex import CAComplex
from typing import Dict




import re
from typing import Dict, Any

class FormativeParser:
    def __init__(self):
        self.position = 0
        self.formative_string = ""

    def parse(self, formative_string: str) -> Formative:
        self.formative_string = formative_string
        self.position = 0

        formative = Formative()

        # Parse Slot I
        formative.slot_i = self.parse_slot_i()

        # Parse Slot II
        formative.slot_ii = self.parse_slot_ii()

        # Parse Slot III
        formative.slot_iii = self.parse_slot_iii()

        # Parse Slot IV
        formative.slot_iv = self.parse_slot_iv()

        # Parse Slot V
        formative.slot_v = self.parse_slot_v()

        # Parse Slot VI
        formative.slot_vi = self.parse_slot_vi()

        # Parse Slot VII
        formative.slot_vii = self.parse_slot_vii()

        # Parse Slot VIII
        formative.slot_viii = self.parse_slot_viii()

        # Parse Slot IX
        formative.slot_ix = self.parse_slot_ix()

        # Parse Slot X
        formative.slot_x = self.parse_slot_x()

        return formative

    def consume(self, n: int) -> str:
        result = self.formative_string[self.position:self.position + n]
        self.position += n
        return result

    def consume_pattern(self, pattern: str) -> str:
        match = re.match(pattern, self.formative_string[self.position:])
        if match:
            result = match.group(0)
            self.position += len(result)
            return result
        return ''

    def parse_slot_i(self) -> SlotI:
        concat_status = self.consume(1)
        if concat_status == 'h':
            next_char = self.consume(1)
            if next_char == 'w':
                concat_status = 'hw'
            else:
                self.position -= 1  # Put the character back if it's not 'w'
        elif concat_status != '':
            self.position -= 1  # Put the character back if it's not 'h' or ''
            concat_status = ''
        
        slot_i = SlotI()
        slot_i.parse(concat_status)
        return slot_i

    def parse_slot_ii(self) -> SlotII:
        vv = self.consume_pattern(r'^[aeiouäëöü]+')
        return SlotII.parse(vv)

    def parse_slot_iii(self) -> SlotIII:
        root = self.consume_pattern(r'^[^aeiouäëöü]+')
        return SlotIII(root)

    def parse_slot_iv(self) -> SlotIV:
        vr = self.consume_pattern(r'^[aeiouäëöü]+')
        return SlotIV.parse(vr)

    def parse_slot_v(self) -> SlotV:
        # This is a simplified version. You might need to adjust based on your specific implementation
        vxcs_pattern = self.consume_pattern(r'^(-?[^aeiouäëöü]+[aeiouäëöü]+)*')
        return SlotV.parse(vxcs_pattern)

    def parse_slot_vi(self) -> SlotVI:
        ca = self.consume_pattern(r'^[^aeiouäëöü]{1,5}')
        return SlotVI(CAComplex.parse(ca))

    def parse_slot_vii(self) -> SlotVII:
        # Similar to Slot V
        vxcs_pattern = self.consume_pattern(r'^(-?[aeiouäëöü]+[^aeiouäëöü]+)*')
        return SlotVII.parse(vxcs_pattern)

    def parse_slot_viii(self) -> SlotVIII:
        vncn = self.consume_pattern(r'^[aeiouäëöü][^aeiouäëöü]')
        return SlotVIII.parse(vncn) if vncn else None

    def parse_slot_ix(self) -> SlotIX:
        vc = self.consume_pattern(r'^[aeiouäëöü]')
        return SlotIX(Case.parse(vc))

    def parse_slot_x(self) -> SlotX:
        # Slot X is determined by stress, which isn't visible in the string representation
        # You might need to handle this differently
        return SlotX(Stress.ULTIMATE)

    def validate(self, formative: Formative) -> bool:
        # Implement validation logic here
        # Check for required slots, consistency between slots, etc.
        return True

# Usage example:
if __name__ == "__main__":
    from lexicon.root_database import RootDatabase

    # Load the lexicon
    db = RootDatabase.load_from_file(r"Pythkuil\resources\lexicon.json")

    parser = FormativeParser()
    
    # Parsing example
    formative_string = "holakšila"  # This is a made-up example
    parsed_formative = parser.parse(formative_string)
    
    if parser.validate(parsed_formative):
        print(parsed_formative.describe())
    else:
        print("Invalid formative")

    # Generation example
    formative = Formative()
    root = db.get_root("KŠL")  # Assuming 'KŠL' is a valid root in your lexicon
    if root:
        formative.set_root(root)
        formative.slot_ii.stem = Stem.S1
        formative.slot_ix.value = Case.ERG
        formative.slot_iv.specification = Specification.OBJ
        formative.slot_iv.function = Function.DYN

        print(formative.describe())
        print(f"Generated formative: {formative.generate()}")
    else:
        print("Root 'KŠL' not found in the lexicon")