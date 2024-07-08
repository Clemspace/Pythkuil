from enum import Enum

class Extension(Enum):
    DEL = 1  # Delimitive
    PRX = 2  # Proximal
    ICP = 3  # Inceptive
    ATV = 4  # Attenuative
    GRA = 5  # Graduative
    DPL = 6  # Depletive

def get_extension_affix(ext: Extension) -> str:
    # TODO: Implement the logic to return the appropriate affix
    pass