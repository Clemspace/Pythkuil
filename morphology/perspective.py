from enum import Enum

class Perspective(Enum):
    M = 1  # Monadic
    G = 2  # Agglomerative
    N = 3  # Nomic
    A = 4  # Abstract

def get_perspective_affix(persp: Perspective) -> str:
    # TODO: Implement the logic to return the appropriate affix
    pass