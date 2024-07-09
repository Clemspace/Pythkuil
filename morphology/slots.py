from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List, Any

from Pythkuil.lexicon.root import Root
from .version import Version
from .function import Function
from .configuration import Configuration
from .specification import Specification
from .context import Context
from .affiliation import Affiliation
from .perspective import Perspective
from .extension import Extension
from .essence import Essence
from .stem import Stem, get_stem_vowel, parse_stem, get_stem_description, apply_stem_to_root

class Slot(ABC):
    @abstractmethod
    def generate(self) -> str:
        """Generate the string representation of the slot."""
        pass

    @abstractmethod
    def parse(self, input: str):
        """Parse the input string and set the slot's attributes."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Return a description of the slot's current state."""
        pass

class SlotI(Slot):
    """Concatenation status"""
    def __init__(self, concatenation_type: Optional[str] = None):
        self.concatenation_type = concatenation_type  # None, 'Type-1', or 'Type-2'

    def generate(self) -> str:
        return self.concatenation_type or ""

    def parse(self, input: str):
        self.concatenation_type = input if input in ['Type-1', 'Type-2'] else None

    def describe(self) -> str:
        return f"Concatenation: {self.concatenation_type or 'None'}"

class SlotII(Slot):
    """Stem and Version"""
    def __init__(self, stem: Stem = Stem.S1, version: Version = Version.PRC):
        self.stem = stem
        self.version = version

    def generate(self) -> str:
        stem_vowel = get_stem_vowel(self.stem)
        # Note: This is a placeholder. You'll need to implement version vowel logic.
        version_vowel = 'a' if self.version == Version.PRC else 'ä'
        return f"{stem_vowel}{version_vowel}"

    def parse(self, input: str):
        if len(input) != 2:
            raise ValueError("Invalid input for SlotII")
        self.stem = parse_stem(input[0])
        # Note: This is a placeholder. You'll need to implement version parsing logic.
        self.version = Version.PRC if input[1] == 'a' else Version.CPT

    def describe(self) -> str:
        return f"Stem: {self.stem.name} ({get_stem_description(self.stem)}), Version: {self.version.name}"

class SlotIII(Slot):
    """Root"""
    def __init__(self, root: Optional[Root] = None):
        self.root = root

    def set_root(self, root: Root):
        self.root = root

    def get_root_form(self) -> str:
        return self.root.root if self.root else ""

    def get_stem_meaning(self, stem: Stem, specification: Specification) -> str:
        if self.root and stem.value < len(self.root.stems):
            stem_data = self.root.stems[stem.value]
            if isinstance(stem_data, dict):
                return stem_data.get(specification.name, "Undefined")
            elif isinstance(stem_data, str):
                return stem_data
        return "Undefined"

    def generate(self) -> str:
        return self.get_root_form()

    def parse(self, input: str):
        # Placeholder implementation
        self.root = Root(input, "", [{"BSC": f"Root {input}"}])

    def describe(self) -> str:
        return f"Root: {self.get_root_form()}"

class SlotIV(Slot):
    """Function, Specification, and Context"""
    def __init__(self, function: Function = Function.STA, 
                 specification: Specification = Specification.BSC, 
                 context: Context = Context.EXS):
        self.function = function
        self.specification = specification
        self.context = context

    def generate(self) -> str:
        # Placeholder implementation
        return f"{self.function.name}-{self.specification.name}-{self.context.name}"

    def parse(self, input: str):
        # Placeholder implementation
        func, spec, ctx = input.split('-')
        self.function = Function[func]
        self.specification = Specification[spec]
        self.context = Context[ctx]

    def describe(self) -> str:
        return f"Function: {self.function.name}, Specification: {self.specification.name}, Context: {self.context.name}"

class SlotV(Slot):
    """Affixes (CSVX...)"""
    def __init__(self, affixes: Optional[List[str]] = None):
        self.affixes = affixes or []

    def generate(self) -> str:
        return "-".join(self.affixes)

    def parse(self, input: str):
        self.affixes = input.split('-')

    def describe(self) -> str:
        return f"Affixes: {', '.join(self.affixes)}"

class SlotVI(Slot):
    """CA complex"""
    def __init__(self, configuration: Configuration = Configuration.UPX,
                 affiliation: Affiliation = Affiliation.CSL,
                 perspective: Perspective = Perspective.M,
                 extension: Extension = Extension.DEL,
                 essence: Essence = Essence.NRM):
        self.configuration = configuration
        self.affiliation = affiliation
        self.perspective = perspective
        self.extension = extension
        self.essence = essence

    def generate(self) -> str:
        # Placeholder implementation
        return f"{self.configuration.name}-{self.affiliation.name}-{self.perspective.name}-{self.extension.name}-{self.essence.name}"

    def parse(self, input: str):
        # Placeholder implementation
        config, affil, persp, ext, ess = input.split('-')
        self.configuration = Configuration[config]
        self.affiliation = Affiliation[affil]
        self.perspective = Perspective[persp]
        self.extension = Extension[ext]
        self.essence = Essence[ess]

    def describe(self) -> str:
        return f"CA: {self.configuration.name}, {self.affiliation.name}, {self.perspective.name}, {self.extension.name}, {self.essence.name}"

class SlotVII(Slot):
    """Affixes (VXCS...)"""
    def __init__(self, affixes: Optional[List[str]] = None):
        self.affixes = affixes or []

    def generate(self) -> str:
        return "-".join(self.affixes)

    def parse(self, input: str):
        self.affixes = input.split('-')

    def describe(self) -> str:
        return f"Affixes: {', '.join(self.affixes)}"

class SlotVIII(Slot):
    """VNCN - Valence or Aspect/Mood"""
    def __init__(self, valence: Optional[str] = None, aspect: Optional[str] = None, mood: Optional[str] = None):
        self.valence = valence
        self.aspect = aspect
        self.mood = mood

    def generate(self) -> str:
        return f"{self.valence or ''}-{self.aspect or ''}-{self.mood or ''}"

    def parse(self, input: str):
        self.valence, self.aspect, self.mood = input.split('-')

    def describe(self) -> str:
        return f"Valence: {self.valence or 'None'}, Aspect: {self.aspect or 'None'}, Mood: {self.mood or 'None'}"

class SlotIX(Slot):
    """Case, Format, or Illocution and Validation"""
    def __init__(self, case: Optional[str] = None, format: Optional[str] = None, 
                 illocution: Optional[str] = None, validation: Optional[str] = None):
        self.case = case
        self.format = format
        self.illocution = illocution
        self.validation = validation

    def generate(self) -> str:
        return f"{self.case or ''}-{self.format or ''}-{self.illocution or ''}-{self.validation or ''}"

    def parse(self, input: str):
        self.case, self.format, self.illocution, self.validation = input.split('-')

    def describe(self) -> str:
        return f"Case: {self.case or 'None'}, Format: {self.format or 'None'}, Illocution: {self.illocution or 'None'}, Validation: {self.validation or 'None'}"

class SlotX(Slot):
    """Stress - determines whether the formative is a noun, unframed verb, or framed verb"""
    def __init__(self, stress: str = "ultimate"):
        self.stress = stress  # 'ultimate', 'penultimate', or 'antepenultimate'

    def generate(self) -> str:
        return self.stress

    def parse(self, input: str):
        if input in ['ultimate', 'penultimate', 'antepenultimate']:
            self.stress = input
        else:
            raise ValueError("Invalid stress pattern")

    def describe(self) -> str:
        return f"Stress: {self.stress}"