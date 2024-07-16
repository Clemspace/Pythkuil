from enum import Enum
from typing import Dict, List, Tuple

class Function(Enum):
    STA = 1  # Stative
    DYN = 2  # Dynamic

class Specification(Enum):
    BSC = 1  # Basic
    CTE = 2  # Contential
    CSV = 3  # Constitutive
    OBJ = 4  # Objective

class Context(Enum):
    EXS = 1  # Existential
    FNC = 2  # Functional
    RPS = 3  # Representational
    AMG = 4  # Amalgamative

class SlotIV:
    """Function, Specification, and Context"""

    vowel_matrix: Dict[Function, Dict[Specification, List[str]]] = {
        Function.STA: {
            Specification.BSC: ['a', 'ai', 'ia', 'ao'],
            Specification.CTE: ['ä', 'au', 'ie', 'aö'],
            Specification.CSV: ['e', 'ei', 'io', 'eo'],
            Specification.OBJ: ['i', 'eu', 'iö', 'eö'],
        },
        Function.DYN: {
            Specification.BSC: ['u', 'ui', 'ua', 'oa'],
            Specification.CTE: ['ü', 'iu', 'ue', 'öa'],
            Specification.CSV: ['o', 'oi', 'uo', 'oe'],
            Specification.OBJ: ['ö', 'ou', 'uö', 'öe'],
        }
    }

    alternate_rps_vowels: Dict[str, str] = {
        'ia': 'uä', 'ie': 'uë', 'io': 'üä', 'iö': 'üë',
        'ua': 'iä', 'ue': 'ië', 'uo': 'öä', 'uö': 'öë'
    }

    def __init__(self, function: Function = Function.STA, 
                 specification: Specification = Specification.BSC, 
                 context: Context = Context.EXS):
        self.function = function
        self.specification = specification
        self.context = context

    def generate(self) -> str:
        return self.get_context_vowel(self.context, self.function, self.specification)

    def parse(self, input: str):
        # Implement parsing logic here
        # This should set self.function, self.specification, and self.context based on the input
        pass

    def describe(self) -> str:
        return f"Function: {self.function.name}, Specification: {self.specification.name}, Context: {self.context.name}"

    @classmethod
    def get_context_vowel(cls, ctx: Context, func: Function, spec: Specification) -> str:
        return cls.vowel_matrix[func][spec][ctx.value - 1]

    @classmethod
    def get_alternate_rps_vowel(cls, vowel: str) -> str:
        return cls.alternate_rps_vowels.get(vowel, vowel)

    @staticmethod
    def is_valid_context(ctx: Context, func: Function, spec: Specification) -> bool:
        return all([isinstance(ctx, Context),
                    isinstance(func, Function),
                    isinstance(spec, Specification)])

    @classmethod
    def apply_context_rules(cls, word: str, ctx: Context, func: Function, spec: Specification) -> str:
        if not cls.is_valid_context(ctx, func, spec):
            raise ValueError("Invalid Context, Function, or Specification")
        
        vowel = cls.get_context_vowel(ctx, func, spec)
        
        # Apply RPS alternate forms if needed
        if ctx == Context.RPS and word.endswith(('y', 'w')):
            vowel = cls.get_alternate_rps_vowel(vowel)
            if word.endswith('y') and vowel.startswith('i'):
                word = word[:-1]  # Remove trailing 'y'
            elif word.endswith('w') and vowel.startswith('u'):
                word = word[:-1]  # Remove trailing 'w'
        
        return word + vowel

    @classmethod
    def get_function(cls, vowel: str) -> Function:
        for func, spec_dict in cls.vowel_matrix.items():
            for spec, vowels in spec_dict.items():
                if vowel in vowels:
                    return func
        raise ValueError(f"Invalid vowel: {vowel}")

    @classmethod
    def get_specification(cls, vowel: str) -> Specification:
        for func, spec_dict in cls.vowel_matrix.items():
            for spec, vowels in spec_dict.items():
                if vowel in vowels:
                    return spec
        raise ValueError(f"Invalid vowel: {vowel}")

    @classmethod
    def get_context(cls, vowel: str) -> Context:
        for func, spec_dict in cls.vowel_matrix.items():
            for spec, vowels in spec_dict.items():
                if vowel in vowels:
                    return Context(vowels.index(vowel) + 1)
        raise ValueError(f"Invalid vowel: {vowel}")