from enum import Enum

class Perspective(Enum):
    M = ''  # Monadic
    G = 'g'  # Agglomerative
    N = 'n'  # Nomic
    A = 'ň'  # Abstract

    def __str__(self):
        return self.value

    @classmethod
    def parse(cls, affix: str) -> 'Perspective':
        return next((p for p in cls if p.value == affix), cls.M)