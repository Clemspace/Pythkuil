from enum import Enum

class Affiliation(Enum):
    CSL = 1  # Consolidative
    ASO = 2  # Associative
    VAR = 3  # Variative
    COA = 4  # Coalescent

def get_affiliation_affix(affil: Affiliation) -> str:
    affixes = {
        Affiliation.CSL: '',  # Default, no affix
        Affiliation.ASO: 'l',
        Affiliation.VAR: 'r',
        Affiliation.COA: 'ř'
    }
    return affixes[affil]

@classmethod
def parse(cls, affix: str) -> 'Affiliation':
    parse_map = {'': cls.CSL, 'l': cls.ASO, 'r': cls.VAR, 'ř': cls.COA}
    return parse_map.get(affix, cls.CSL)  # Default to CSL if not found