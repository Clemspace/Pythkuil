from enum import Enum

class Extension(Enum):
    DEL = ''  # Delimitive
    PRX = 'n'  # Proximal
    ICP = 's'  # Inceptive
    ATV = 'š'  # Attenuative
    GRA = 'f'  # Graduative
    DPL = 't'  # Depletive

    def __str__(self):
        return self.value

    @classmethod
    def parse(cls, affix: str) -> 'Extension':
        return next((e for e in cls if e.value == affix), cls.DEL)