from enum import Enum

class Affiliation(Enum):
    CSL = ''  # Consolidative
    ASO = 'l'  # Associative
    VAR = 'r'  # Variative
    COA = 'ř'  # Coalescent

    def __str__(self):
        return self.value

    @classmethod
    def parse(cls, affix: str) -> 'Affiliation':
        return next((a for a in cls if a.value == affix), cls.CSL)