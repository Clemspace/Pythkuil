from enum import Enum
from typing import Optional
from Pythkuil.morphology.configuration import Configuration
from Pythkuil.morphology.affiliation import Affiliation
from Pythkuil.morphology.perspective import Perspective
from Pythkuil.morphology.extension import Extension
from Pythkuil.morphology.essence import Essence
from Pythkuil.morphology.version import Version
from Pythkuil.morphology.function import Function
from Pythkuil.morphology.context import Context
from Pythkuil.morphology.ca_complex import CAComplex
from Pythkuil.utils.shortcuts import apply_shortcut, decode_shortcut
from Pythkuil.grammar.cases import Case, CaseScope

class Stem(Enum):
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3

class Specification(Enum):
    BSC = 1  # Basic
    CTE = 2  # Contential
    CSV = 3  # Constitutive
    OBJ = 4  # Objective

class Formative:
    def __init__(self):
        # Slot I: Concatenation Type
        self.concatenation_type: Optional[str] = None
        
        # Slot II: Version + Stem + CA Shortcut
        self.version: Version = Version.PRC
        self.stem: Stem = Stem.S1
        self.ca_shortcut: bool = False
        
        # Slot III: Root
        self.root: str = ""
        
        # Slot IV: Function + Specification + Context
        self.function: Function = Function.STA
        self.specification: Specification = Specification.BSC
        self.context: Context = Context.EXS
        
        # Slot V: VXCS Affixes
        self.slot_v_affixes: list = []
        
        # Slot VI: CA Complex
        self.ca_complex: CAComplex = CAComplex(
            Configuration.UPX,
            Affiliation.CSL,
            Perspective.M,
            Extension.DEL,
            Essence.NRM
        )
        
        # Slot VII: VXCS Affixes
        self.slot_vii_affixes: list = []
        
        # Slot VIII: VN or CN
        self.vn: Optional[str] = None
        self.cn: Optional[CaseScope] = None
        
        # Slot IX: Case or Illocution + Validation
        self.case: Optional[Case] = None
        self.illocution: Optional[str] = None
        self.validation: Optional[str] = None
        
        # Slot X: Stress
        self.stress: str = "ultimate"  # Can be "ultimate", "penultimate", or "antepenultimate"

    def apply_ca_shortcut(self):
        shortcut = apply_shortcut(self.concatenation_type, self.stem.value)
        if shortcut:
            self.ca_shortcut = True
            decoded = decode_shortcut(shortcut)
            self.function = decoded['function']
            self.specification = decoded['specification']
            self.context = decoded['context']
            self.ca_complex = CAComplex(**decoded['ca_complex'])

    def generate(self) -> str:
        # TODO: Implement the generation of the formative string
        pass

    def parse(self, formative_string: str):
        # TODO: Implement parsing of a formative string into this object
        pass

# Usage example:
if __name__ == "__main__":
    formative = Formative()
    formative.root = "kš"
    formative.stem = Stem.S2
    formative.case = Case.ERG
    formative.specification = Specification.OBJ
    
    print(f"Root: {formative.root}")
    print(f"Stem: {formative.stem}")
    print(f"Case: {formative.case}")
    print(f"Specification: {formative.specification}")
    print(f"CA Complex: {formative.ca_complex.generate()}")