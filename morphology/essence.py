from enum import Enum

class Essence(Enum):
    NRM = ''  # Normal
    RPV = 'w'  # Representative

    def __str__(self):
        return self.value

    @classmethod
    def parse(cls, affix: str) -> 'Essence':
        return next((e for e in cls if e.value == affix), cls.NRM)