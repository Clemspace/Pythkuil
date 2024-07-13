from enum import Enum
from typing import Optional
from .configuration import Configuration
from .affiliation import Affiliation
from .perspective import Perspective
from .extension import Extension
from .essence import Essence
from .slots.slot_iv import Context, Function, Specification, apply_context_rules

class CAComplex:
    def __init__(self, config: Configuration, affil: Affiliation, persp: Perspective, ext: Extension, ess: Essence):
        self.configuration = config
        self.affiliation = affil
        self.perspective = persp
        self.extension = ext
        self.essence = ess

    def generate(self, context: Context, function: Function, specification: Specification) -> str:
        ca_form = self._generate_ca_form()
        return apply_context_rules(ca_form, context, function, specification)

    def _generate_ca_form(self) -> str:
        components = [
            self.affiliation.value,
            self.configuration.value,
            self.extension.value,
            self.perspective.value,
            self.essence.value
        ]
        return ''.join(component for component in components if component)

    def apply_stacking(self, stacked_ca: 'CAComplex'):
        # Apply stacking rules here
        # For example:
        self.configuration = stacked_ca.configuration
        self.affiliation = stacked_ca.affiliation
        self.perspective = stacked_ca.perspective
        self.extension = stacked_ca.extension
        self.essence = stacked_ca.essence

    @classmethod
    def parse(cls, ca_string: str) -> 'CAComplex':
        # This method parses a CA string and returns a CAComplex object
        affil = Affiliation.parse(ca_string[0])
        config = Configuration.parse(ca_string[1])
        ext = Extension.parse(ca_string[2])
        persp = Perspective.parse(ca_string[3])
        ess = Essence.parse(ca_string[4])
        return cls(config, affil, persp, ext, ess)

    def __str__(self):
            return f"CAComplex(config={self.configuration}, affil={self.affiliation}, persp={self.perspective}, ext={self.extension}, ess={self.essence})"
        
def generate_short_form(ca_complex: CAComplex, context: Context, function: Function, specification: Specification) -> Optional[str]:
    # Implement the short-form generation as described in section 3.10
    if (ca_complex.affiliation == Affiliation.CSL and
        ca_complex.configuration == Configuration.UPX and
        ca_complex.extension == Extension.DEL and
        ca_complex.essence == Essence.NRM):
        
        if ca_complex.perspective == Perspective.M:
            prefix = 'w'
        elif ca_complex.perspective == Perspective.G:
            prefix = 'w'
        elif ca_complex.perspective == Perspective.N:
            prefix = 'w'
        elif ca_complex.perspective == Perspective.A:
            prefix = 'y'
        else:
            return None  # No short form available

        vowel = apply_context_rules('', context, function, specification)
        return prefix + vowel

    return None  # No short form available

# Example usage:
if __name__ == "__main__":
    ca = CAComplex(Configuration.UPX, Affiliation.CSL, Perspective.M, Extension.DEL, Essence.NRM)
    print(ca.generate(Context.FNC, Function.DYN, Specification.BSC))  # Example output
    
    short_form = generate_short_form(ca, Context.FNC, Function.DYN, Specification.BSC)
    print(f"Short form: {short_form}")  # Example short form output

    parsed_ca = CAComplex.parse("upxmn")
    print(parsed_ca)