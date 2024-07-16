from ..ca_complex import CAComplex, generate_short_form
from ..configuration import Configuration
from ..affiliation import Affiliation
from ..perspective import Perspective
from ..extension import Extension
from ..essence import Essence
from ..slots.slot_iv import Context,Function,Specification

class SlotVI:
    """Slot VI: Ca complex"""

    def __init__(self, ca_complex: CAComplex = None):
            self.ca_complex = ca_complex if ca_complex else CAComplex(
                Configuration.UPX,  # default Configuration
                Affiliation.CSL,    # default Affiliation
                Perspective.M,      # default Perspective
                Extension.DEL,      # default Extension
                Essence.NRM         # default Essence
            )

    def generate(self, context: Context, function: Function, specification: Specification) -> str:
        return self.ca_complex.generate(context, function, specification)

    def parse(self, input: str):
        self.ca_complex = CAComplex.parse(input)

    def describe(self) -> str:
        return str(self.ca_complex)

    def get_short_form(self, context: Context, function: Function, specification: Specification) -> str:
        short_form = generate_short_form(self.ca_complex, context, function, specification)
        return short_form if short_form else self.generate(context, function, specification)

    @classmethod
    def from_components(cls, config: Configuration, affil: Affiliation, persp: Perspective, 
                        ext: Extension, ess: Essence) -> 'SlotVI':
        ca_complex = CAComplex(config, affil, persp, ext, ess)
        return cls(ca_complex)

    @property
    def configuration(self) -> Configuration:
        return self.ca_complex.configuration

    @property
    def affiliation(self) -> Affiliation:
        return self.ca_complex.affiliation

    @property
    def perspective(self) -> Perspective:
        return self.ca_complex.perspective

    @property
    def extension(self) -> Extension:
        return self.ca_complex.extension

    @property
    def essence(self) -> Essence:
        return self.ca_complex.essence