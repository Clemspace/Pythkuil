from enum import Enum

class Context(Enum):
    EXS = 1  # Existential
    FNC = 2  # Functional
    RPS = 3  # Representational
    AMG = 4  # Amalgamative

def get_context_vowel(ctx: Context) -> str:
    # TODO: Implement the logic to return the appropriate vowel
    pass