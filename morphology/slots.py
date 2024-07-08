from enum import Enum
from typing import Optional, List
from .version import Version
from Pythkuil.grammar.formative import Stem
from .function import Function
from .configuration import Configuration
from .specification import Specification
class SlotI:
    """Concatenation status"""
    def __init__(self, concatenation_type: Optional[str] = None):
        self.concatenation_type = concatenation_type  # None, 'Type-1', or 'Type-2'

class SlotII:
    """Stem and Version"""
    def __init__(self, stem: Stem = Stem.S1, version: Version = Version.PRC):
        self.stem = stem
        self.version = version

class SlotIII:
    """Root"""
    def __init__(self, root: str):
        self.root = root

class SlotIV:
    """Function, Specification, and Context"""
    def __init__(self, function: Function = Function.STA, 
                 specification: Specification = Specification.BSC, 
                 context: Context = Context.EXS):
        self.function = function
        self.specification = specification
        self.context = context

class SlotV:
    """Affixes (CSVX...)"""
    def __init__(self, affixes: Optional[List[str]] = None):
        self.affixes = affixes or []

class SlotVI:
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

    def generate_ca(self) -> str:
        # Logic to generate the CA consonant form
        pass

class SlotVII:
    """Affixes (VXCS...)"""
    def __init__(self, affixes: Optional[List[str]] = None):
        self.affixes = affixes or []

class SlotVIII:
    """VNCN - Valence or Aspect/Mood"""
    def __init__(self, valence: Optional[str] = None, aspect: Optional[str] = None, mood: Optional[str] = None):
        self.valence = valence
        self.aspect = aspect
        self.mood = mood

class SlotIX:
    """Case, Format, or Illocution and Validation"""
    def __init__(self, case: Optional[str] = None, format: Optional[str] = None, 
                 illocution: Optional[str] = None, validation: Optional[str] = None):
        self.case = case
        self.format = format
        self.illocution = illocution
        self.validation = validation

class SlotX:
    """Stress - determines whether the formative is a noun, unframed verb, or framed verb"""
    def __init__(self, stress: str):
        self.stress = stress  # 'noun', 'unframed_verb', or 'framed_verb'