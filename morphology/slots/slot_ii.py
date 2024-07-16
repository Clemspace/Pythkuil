from enum import Enum
from typing import Dict, Tuple, Optional

class Version(Enum):
    PRC = 1  # Processual
    CPT = 2  # Completive

class Stem(Enum):
    S0 = 0  # Stem Zero
    S1 = 1  # Stem 1
    S2 = 2  # Stem 2
    S3 = 3  # Stem 3

class SlotII:
    """Stem and Version"""
    vowel_map: Dict[Tuple[Stem, Version], str] = {
        (Stem.S0, Version.PRC): 'o', (Stem.S0, Version.CPT): 'ö',
        (Stem.S1, Version.PRC): 'a', (Stem.S1, Version.CPT): 'ä',
        (Stem.S2, Version.PRC): 'e', (Stem.S2, Version.CPT): 'i',
        (Stem.S3, Version.PRC): 'u', (Stem.S3, Version.CPT): 'ü'
    }

    inverse_vowel_map: Dict[str, Tuple[Stem, Version]] = {v: k for k, v in vowel_map.items()}

    def __init__(self, stem: Stem = Stem.S1, version: Version = Version.PRC):
        self.stem = stem
        self.version = version

    def generate(self) -> str:
        return self.vowel_map[(self.stem, self.version)]

    def parse(self, input: str) -> 'SlotII':
        if not self.is_valid_vowel(input):
            raise ValueError(f"Invalid input for SlotII: {input}")
        self.stem, self.version = self.inverse_vowel_map[input]
        return self

    def describe(self) -> str:
        stem_descriptions = {
            Stem.S0: "Stem Zero: Overall conceptual meaning of the raw root",
            Stem.S1: "Stem 1: The first instantiated meaning of the root",
            Stem.S2: "Stem 2: The second instantiated meaning of the root",
            Stem.S3: "Stem 3: The third instantiated meaning of the root"
        }
        version_descriptions = {
            Version.PRC: "Processual: Default version, describing entities/acts not focused on an anticipated outcome",
            Version.CPT: "Completive: Describing entities/acts intended to achieve an anticipated outcome"
        }
        return f"Stem: {self.stem.name} ({stem_descriptions[self.stem]})\nVersion: {self.version.name} ({version_descriptions[self.version]})"

    @classmethod
    def get_stem_vowel(cls, stem: Stem) -> str:
        return cls.vowel_map[(stem, Version.PRC)]

    @classmethod
    def get_version_vowel(cls, version: Version, stem: Stem) -> str:
        return cls.vowel_map[(stem, version)]

    @classmethod
    def parse_stem(cls, vowel: str) -> Stem:
        return cls.inverse_vowel_map[vowel][0]

    @classmethod
    def parse_version(cls, vowel: str) -> Version:
        return cls.inverse_vowel_map[vowel][1]

    @classmethod
    def is_valid_vowel(cls, input: str) -> bool:
        return input in cls.inverse_vowel_map