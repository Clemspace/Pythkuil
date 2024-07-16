from enum import Enum
from typing import Union
from ...grammar.cases import Case, CaseSystem, case_system

class Illocution(Enum):
    ASR = 'á'    # Assertive
    DIR = 'â'    # Directive
    DEC = 'é'    # Declarative
    IRG = 'í'    # Interrogative
    VER = 'ô'    # Verificative
    ADM = 'ó'    # Admonitive
    POT = 'û'    # Potentiative
    HOR = 'ú'    # Hortative
    CNJ = 'î'    # Conjectural

class Validation(Enum):
    OBS = 'á'    # Observational
    REC = 'â'    # Recollective
    PUP = 'é'    # Purportive
    RPR = 'í'    # Reportive
    USP = 'êi'   # Unspecified
    IMA = 'ô'    # Imaginary
    CVN = 'ó'    # Conventional
    ITU = 'û'    # Intuitive
    INF = 'ú'    # Inferential

class SlotIX:
    def __init__(self, value: Union[Case, tuple[Illocution, Validation]]):
        self.value = value

    def generate(self) -> str:
        if isinstance(self.value, Case):
            return case_system.get_case_properties(self.value).affix
        else:
            illocution, validation = self.value
            return illocution.value + validation.value

    def parse(self, input: str, relation: 'Relation'):
        if relation == Relation.FRAMED:
            # If FRAMED, it must be a Case
            case = case_system.get_case_by_affix(input)
            if case:
                self.value = case
            else:
                raise ValueError(f"Unable to parse Case input: {input}")
        else:
            # If UNFRAMED, it must be Illocution + Validation
            if len(input) == 2:
                illocution = next((i for i in Illocution if i.value == input[0]), None)
                validation = next((v for v in Validation if v.value == input[1]), None)
                if illocution and validation:
                    self.value = (illocution, validation)
                else:
                    raise ValueError(f"Unable to parse Illocution+Validation input: {input}")
            else:
                raise ValueError(f"Invalid input length for Illocution+Validation: {input}")

    def describe(self) -> str:
        if isinstance(self.value, Case):
            props = case_system.get_case_properties(self.value)
            return f"Case: {props.name} ({props.abbreviation})"
        else:
            illocution, validation = self.value
            return f"Illocution: {illocution.name}, Validation: {validation.name}"

# Usage example:
if __name__ == "__main__":
    from slot_x import Relation

    # Case example (FRAMED)
    slot_ix_case = SlotIX(Case.THM)
    print(slot_ix_case.generate())  # Should print "-a"
    print(slot_ix_case.describe())  # Should print "Case: Thematic (THM)"

    # Illocution + Validation example (UNFRAMED)
    slot_ix_ill_val = SlotIX((Illocution.ASR, Validation.OBS))
    print(slot_ix_ill_val.generate())  # Should print "áá"
    print(slot_ix_ill_val.describe())  # Should print "Illocution: ASR, Validation: OBS"

    # Parsing example
    slot_ix_parsed = SlotIX(Case.THM)  # Initialize with any value
    slot_ix_parsed.parse("-a", Relation.FRAMED)
    print(slot_ix_parsed.describe())  # Should print "Case: Thematic (THM)"

    slot_ix_parsed = SlotIX((Illocution.ASR, Validation.OBS))  # Initialize with any value
    slot_ix_parsed.parse("áá", Relation.UNFRAMED)
    print(slot_ix_parsed.describe())  # Should print "Illocution: ASR, Validation: OBS"