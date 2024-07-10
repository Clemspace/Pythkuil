from ...morphology.configuration import Configuration
from ...morphology.affiliation import Affiliation
from ...morphology.perspective import Perspective
from ...morphology.extension import Extension
from ...morphology.essence import Essence
from ...morphology.version import Version
from ...morphology.context import Context
from ...morphology.ca_complex import CAComplex
from ...utils.shortcuts import apply_shortcut, decode_shortcut
from ...grammar.cases import Case, CaseScope
from ...lexicon.root import Root
from ...morphology.stem import Stem, get_stem_vowel, parse_stem, get_stem_description, apply_stem_to_root
from ...morphology.specification import (
    Specification, Function, get_specification_vowel, 
    combine_specification_and_stem, parse_specification_and_stem, 
    get_specification_description, apply_specification
)

class Formative:
    def __init__(self):
        # Slot I: Concatenation Type
        self.concatenation_type: Optional[str] = None
        
        # Slot II: Version + Stem + CA Shortcut
        self.version: Version = Version.PRC
        self.stem: Stem = Stem.S1
        self.ca_shortcut: bool = False
        
        # Slot III: Root
        self.root: Optional[Root] = None
        
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

    def set_root(self, root: Root):
        self.root = root

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
        if not self.root:
            raise ValueError("Root must be set before generating formative")

        # Generate Slot II
        slot_ii = combine_specification_and_stem(self.specification, self.stem, self.function)
        
        # Apply specification to root
        word = apply_specification(self.root.root, self.specification, self.stem, self.function)
        
        # TODO: Add generation logic for other slots

        return word

    def parse(self, formative_string: str):
        if len(formative_string) < 3:
            raise ValueError("Invalid formative string")

        # Parse Slot II and III
        root_consonants = formative_string[0] + formative_string[3:]
        self.root = Root(root_consonants, "", [{"BSC": f"Root {root_consonants}"}])
        
        spec, stem, func = parse_specification_and_stem(formative_string[1:3])
        self.specification = spec
        self.stem = stem
        self.function = func
        
        # TODO: Add parsing logic for other slots

    def get_stem_meaning(self) -> str:
        if self.root and self.stem.value < len(self.root.stems):
            stem_data = self.root.stems[self.stem.value]
            if isinstance(stem_data, dict):
                return stem_data.get(self.specification.name, "Undefined")
            elif isinstance(stem_data, str):
                return stem_data
        return "Undefined"

    def describe(self) -> str:
        return f"Formative:\n" \
               f"  Root: {self.root.root if self.root else 'Not set'}\n" \
               f"  Stem: {self.stem.name} ({get_stem_description(self.stem)})\n" \
               f"  Specification: {self.specification.name} ({get_specification_description(self.specification)})\n" \
               f"  Function: {self.function.name}\n" \
               f"  Meaning: {self.get_stem_meaning()}\n" \
               f"  Case: {self.case.name if self.case else 'Not set'}\n" \
               f"  CA Complex: {self.ca_complex.generate()}"

# Usage example:
if __name__ == "__main__":
    from Pythkuil.lexicon.root_database import RootDatabase

    # Load the lexicon
    db = RootDatabase.load_from_file(r"C:\Users\Clemspace\Mistral\Pythkuil\resources\lexicon.json")

    formative = Formative()
    root = db.get_root("RČV")  # Assuming 'RČV' is a valid root in your lexicon
    if root:
        formative.set_root(root)
        formative.stem = Stem.S2
        formative.case = Case.ERG
        formative.specification = Specification.OBJ
        formative.function = Function.DYN

        print(formative.describe())
        print(f"Generated formative: {formative.generate()}")

        # Test parsing
        parsed_formative = Formative()
        parsed_formative.parse("kial")
        print("\nParsed formative:")
        print(parsed_formative.describe())
    else:
        print("Root 'K' not found in the lexicon")