from enum import Enum

class Affiliation(Enum):
    CSL = 1  # Consolidative
    ASO = 2  # Associative
    VAR = 3  # Variative
    COA = 4  # Coalescent

def get_affiliation_affix(affil: Affiliation) -> str:
    # TODO: Implement the logic to return the appropriate affix
    pass