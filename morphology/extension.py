from enum import Enum

class Extension(Enum):
    DEL = 1  # Delimitive
    PRX = 2  # Proximal
    ICP = 3  # Inceptive
    ATV = 4  # Attenuative
    GRA = 5  # Graduative
    DPL = 6  # Depletive

def get_extension_affix(ext: Extension) -> str:
    affixes = {
        Extension.DEL: '',  # Default, no affix
        Extension.PRX: 'n',
        Extension.ICP: 's',
        Extension.ATV: 'š',
        Extension.GRA: 'f',
        Extension.DPL: 't'
    }
    return affixes[ext]

@classmethod
def parse(cls, affix: str) -> 'Extension':
    parse_map = {'': cls.DEL, 'n': cls.PRX, 's': cls.ICP, 'š': cls.ATV, 'f': cls.GRA, 't': cls.DPL}
    return parse_map.get(affix, cls.DEL)  # Default to DEL if not found