from enum import Enum

class Essence(Enum):
    NRM = 1  # Normal
    RPV = 2  # Representative

def get_essence_affix(ess: Essence) -> str:
    affixes = {
        Essence.NRM: '',  # Default, no affix
        Essence.RPV: 'w'
    }
    return affixes[ess]

@classmethod
def parse(cls, affix: str) -> 'Essence':
    parse_map = {'': cls.NRM, 'w': cls.RPV}
    return parse_map.get(affix, cls.NRM)  # Default to NRM if not found