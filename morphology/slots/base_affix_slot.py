from typing import List
from ..affixes import VxCsAffix

class BaseAffixSlot:
    def __init__(self):
        self.affixes: List[VxCsAffix] = []

    def add_affix(self, affix: VxCsAffix):
        self.affixes.append(affix)

    def generate(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def has_ca_stacking(self) -> bool:
        return any(affix.is_ca_stacking for affix in self.affixes)

    def describe(self) -> str:
        if not self.affixes:
            return "No affixes"
        return ", ".join(str(affix) for affix in self.affixes)