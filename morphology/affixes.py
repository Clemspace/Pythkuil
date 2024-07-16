from enum import Enum
from typing import List, Optional

class AffixType(Enum):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

class AffixDegree(Enum):
    DEGREE_0 = 0
    DEGREE_1 = 1
    DEGREE_2 = 2
    DEGREE_3 = 3
    DEGREE_4 = 4
    DEGREE_5 = 5
    DEGREE_6 = 6
    DEGREE_7 = 7
    DEGREE_8 = 8
    DEGREE_9 = 9

class VxCsAffix:
    def __init__(self, cs: str, vx: str, affix_type: AffixType, degree: AffixDegree, is_ca_stacking: bool = False):
        self.cs = cs
        self.vx = vx
        self.affix_type = affix_type
        self.degree = degree
        self.is_ca_stacking = is_ca_stacking

    def generate(self) -> str:
        return f"{self.vx}{self.cs}"

    def __str__(self):
        ca_stacking_str = " (CA stacking)" if self.is_ca_stacking else ""
        return f"VxCs Affix: -{self.vx}{self.cs}/{self.degree.value} (Type-{self.affix_type.value}){ca_stacking_str}"

class VxCsAffixSlot:
    def __init__(self):
        self.affixes: List[VxCsAffix] = []

    def add_affix(self, affix: VxCsAffix):
        self.affixes.append(affix)

    def generate(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def parse(self, input: str):
        raise NotImplementedError("Subclasses must implement this method")

    def describe(self) -> str:
        return ", ".join(str(affix) for affix in self.affixes)
    
    def has_ca_stacking(self) -> bool:
        return any(affix.is_ca_stacking for affix in self.affixes)