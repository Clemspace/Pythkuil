from enum import Enum

class Configuration(Enum):
    UPX = 1  # Uniplex
    DPX = 2  # Duplex
    MSS = 3  # Multiplex Similar Separate
    MSC = 4  # Multiplex Similar Connected
    MSF = 5  # Multiplex Similar Fused
    MDS = 6  # Multiplex Dissimilar Separate
    MDC = 7  # Multiplex Dissimilar Connected
    MDF = 8  # Multiplex Dissimilar Fused
    MFS = 9  # Multiplex Fuzzy Separate
    MFC = 10  # Multiplex Fuzzy Connected
    MFF = 11  # Multiplex Fuzzy Fused

def get_configuration_affix(config: Configuration) -> str:
    # TODO: Implement the logic to return the appropriate affix
    pass