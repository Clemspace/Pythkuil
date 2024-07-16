from enum import Enum

class Configuration(Enum):
    UPX = ''  # Uniplex
    DPX = 'd'  # Duplex
    MSS = 'l'  # Multiplex Similar Separate
    MSC = 'r'  # Multiplex Similar Connected
    MSF = 'ř'  # Multiplex Similar Fused
    MDS = 'z'  # Multiplex Dissimilar Separate
    MDC = 'ž'  # Multiplex Dissimilar Connected
    MDF = 'ļ'  # Multiplex Dissimilar Fused
    MFS = 'x'  # Multiplex Fuzzy Separate
    MFC = 'ç'  # Multiplex Fuzzy Connected
    MFF = 'j'  # Multiplex Fuzzy Fused

    def __str__(self):
        return self.value

    @classmethod
    def parse(cls, affix: str) -> 'Configuration':
        return next((c for c in cls if c.value == affix), cls.UPX)