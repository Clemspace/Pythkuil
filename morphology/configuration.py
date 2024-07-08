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
    affixes = {
        Configuration.UPX: '',  # Default, no affix
        Configuration.DPX: 'd',
        Configuration.MSS: 'l',
        Configuration.MSC: 'r',
        Configuration.MSF: 'ř',
        Configuration.MDS: 'z',
        Configuration.MDC: 'ž',
        Configuration.MDF: 'ļ',
        Configuration.MFS: 'x',
        Configuration.MFC: 'ç',
        Configuration.MFF: 'j'
    }
    return affixes[config]

@classmethod
def parse(cls, affix: str) -> 'Configuration':
    parse_map = {v: k for k, v in {
        cls.UPX: '', cls.DPX: 'd', cls.MSS: 'l', cls.MSC: 'r', cls.MSF: 'ř',
        cls.MDS: 'z', cls.MDC: 'ž', cls.MDF: 'ļ', cls.MFS: 'x', cls.MFC: 'ç', cls.MFF: 'j'
    }.items()}
    return parse_map.get(affix, cls.UPX)  # Default to UPX if not found