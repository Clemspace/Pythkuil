from typing import Optional, List
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
from ...morphology.slots.slot_v import SlotV
from ...morphology.slots.slot_vii import SlotVII
from ...morphology.slots.slot_viii import SlotVIII
from ...morphology.slots.slot_ix import SlotIX, Illocution, Validation

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
        self.slot_v: SlotV = SlotV()
        
        # Slot VI: CA Complex
        self.ca_complex: CAComplex = CAComplex(
            Configuration.UPX,
            Affiliation.CSL,
            Perspective.M,
            Extension.DEL,
            Essence.NRM
        )
        
        # Slot VII: VXCS Affixes
        self.slot_vii: SlotVII = SlotVII()
        
        # Slot VIII: VN or CN
        self.slot_viii: SlotVIII = SlotVIII()
        
        # Slot IX: Case or Illocution + Validation
        self.slot_ix: SlotIX = SlotIX(Case.THM)
        
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

        result = ""

        # Slot I
        result += self.concatenation_type or ""

        # Slot II
        result += combine_specification_and_stem(self.specification, self.stem, self.function)

        # Slot III
        result += apply_specification(self.root.root, self.specification, self.stem, self.function)

        # Slot IV
        result += get_specification_vowel(self.specification)

        # Slot V
        slot_v_str = self.slot_v.generate()
        result += slot_v_str

        # Slot VI (Ca complex)
        ca_complex_str = self.ca_complex.generate(self.context, self.function, self.specification)
        if slot_v_str:
            ca_complex_str = self.geminate_ca_complex(ca_complex_str)
        result += ca_complex_str

        # Slot VII
        result += self.slot_vii.generate()

        # Slot VIII
        result += self.slot_viii.generate()

        # Slot IX
        result += self.slot_ix.generate()

        # Slot X (Stress is applied to the whole word, not added as a string)

        return result

    def parse(self, formative_string: str):
        # TODO: Implement full parsing logic
        if len(formative_string) < 3:
            raise ValueError("Invalid formative string")

        # Parse Slot II and III
        root_consonants = formative_string[0] + formative_string[3:]
        self.root = Root(root_consonants, "", [{"BSC": f"Root {root_consonants}"}])
        
        spec, stem, func = parse_specification_and_stem(formative_string[1:3])
        self.specification = spec
        self.stem = stem
        self.function = func

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
               f"  Slot V Affixes: {self.slot_v.describe()}\n" \
               f"  CA Complex: {self.ca_complex}\n" \
               f"  Slot VII Affixes: {self.slot_vii.describe()}\n" \
               f"  Slot VIII: {self.slot_viii.describe()}\n" \
               f"  Slot IX: {self.slot_ix.describe()}\n" \
               f"  Stress: {self.stress}"

    def geminate_ca_complex(self, ca_complex: str) -> str:
        # TODO: Implement proper gemination rules
        return ca_complex + ca_complex[0]

    def apply_ca_stacking(self):
        for affix in self.slot_v.affixes:
            if affix.is_ca_stacking:
                stacked_ca = CAComplex.parse(affix.cs)
                self.ca_complex.apply_stacking(stacked_ca)

        for affix in self.slot_vii.affixes:
            if affix.is_ca_stacking:
                stacked_ca = CAComplex.parse(affix.cs)
                new_ca = CAComplex(self.ca_complex.configuration, self.ca_complex.affiliation,
                                   self.ca_complex.perspective, self.ca_complex.extension, self.ca_complex.essence)
                new_ca.apply_stacking(stacked_ca)
                self.ca_complex = new_ca

    def add_slot_v_affix(self, affix: VxCsAffix):
        self.slot_v.add_affix(affix)

    def add_slot_vii_affix(self, affix: VxCsAffix):
        self.slot_vii.add_affix(affix)

# Usage example remains the same

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