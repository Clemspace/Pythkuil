from enum import Enum
from Pythkuil.morphology.function import Function
from Pythkuil.grammar.word_types.formative import Specification

class Context(Enum):
    EXS = 1  # Existential
    FNC = 2  # Functional
    RPS = 3  # Representational
    AMG = 4  # Amalgamative

def get_context_vowel(ctx: Context, func: Function, spec: Specification) -> str:
    vowel_matrix = {
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
    
    return vowel_matrix[func][spec][ctx.value - 1]

def get_alternate_rps_vowel(vowel: str) -> str:
    alternates = {
        'ia': 'uä', 'ie': 'uë', 'io': 'üä', 'iö': 'üë',
        'ua': 'iä', 'ue': 'ië', 'uo': 'öä', 'uö': 'öë'
    }
    return alternates.get(vowel, vowel)

def is_valid_context(ctx: Context, func: Function, spec: Specification) -> bool:
    return all([isinstance(ctx, Context),
                isinstance(func, Function),
                isinstance(spec, Specification)])

def apply_context_rules(word: str, ctx: Context, func: Function, spec: Specification) -> str:
    if not is_valid_context(ctx, func, spec):
        raise ValueError("Invalid Context, Function, or Specification")
    
    vowel = get_context_vowel(ctx, func, spec)
    
    # Apply RPS alternate forms if needed
    if ctx == Context.RPS and word.endswith(('y', 'w')):
        vowel = get_alternate_rps_vowel(vowel)
        if word.endswith('y') and vowel.startswith('i'):
            word = word[:-1]  # Remove trailing 'y'
        elif word.endswith('w') and vowel.startswith('u'):
            word = word[:-1]  # Remove trailing 'w'
    
    return word + vowel