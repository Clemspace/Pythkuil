from enum import Enum
from typing import Dict

class Version(Enum):
    PRC = 1  # Processual
    CPT = 2  # Completive

def get_version_vowel(ver: Version, stem: int) -> str:
    version_vowels: Dict[Version, Dict[int, str]] = {
        Version.PRC: {0: 'o', 1: 'a', 2: 'e', 3: 'u'},
        Version.CPT: {0: 'ö', 1: 'ä', 2: 'i', 3: 'ü'}
    }
    return version_vowels[ver][stem]

@classmethod
def parse(cls, vowel: str, stem: int) -> 'Version':
    parse_map = {
        0: {'o': cls.PRC, 'ö': cls.CPT},
        1: {'a': cls.PRC, 'ä': cls.CPT},
        2: {'e': cls.PRC, 'i': cls.CPT},
        3: {'u': cls.PRC, 'ü': cls.CPT}
    }
    return parse_map[stem].get(vowel, cls.PRC)  # Default to PRC if not found

def apply_version(stem_vowel: str, ver: Version) -> str:
    stem_map = {'o': 0, 'a': 1, 'e': 2, 'u': 3, 'ö': 0, 'ä': 1, 'i': 2, 'ü': 3}
    stem = stem_map.get(stem_vowel, 1)  # Default to Stem 1 if not found
    return get_version_vowel(ver, stem)