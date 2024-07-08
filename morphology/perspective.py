from enum import Enum

class Perspective(Enum):
    M = 1  # Monadic
    G = 2  # Agglomerative
    N = 3  # Nomic
    A = 4  # Abstract

def get_perspective_affix(persp: Perspective) -> str:
    affixes = {
        Perspective.M: '',  # Default, no affix
        Perspective.G: 'g',
        Perspective.N: 'n',
        Perspective.A: 'ň'
    }
    return affixes[persp]

@classmethod
def parse(cls, affix: str) -> 'Perspective':
    parse_map = {'': cls.M, 'g': cls.G, 'n': cls.N, 'ň': cls.A}
    return parse_map.get(affix, cls.M)  # Default to M if not found