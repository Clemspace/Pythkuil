from typing import Optional
from ...morphology.slots.slot_i import SlotI, ConcatenationStatus
from ...morphology.slots.slot_ii import SlotII, Version, Stem
from ...morphology.slots.slot_iii import SlotIII
from ...morphology.slots.slot_iv import SlotIV, Function, Specification, Context
from ...morphology.slots.slot_v import SlotV
from ...morphology.slots.slot_vi import SlotVI
from ...morphology.slots.slot_vii import SlotVII
from ...morphology.slots.slot_viii import SlotVIII
from ...morphology.slots.slot_ix import SlotIX
from ...morphology.slots.slot_x import SlotX, Stress
from ...morphology.ca_complex import CAComplex
from ...grammar.cases import Case
from ...lexicon.root import Root


class Formative:
    def __init__(self):
        self.slot_i: SlotI = SlotI(ConcatenationStatus.NONE)
        self.slot_ii: SlotII = SlotII()
        self.slot_iii: SlotIII = SlotIII("")
        self.slot_iv: SlotIV = SlotIV()
        self.slot_v: SlotV = SlotV()
        self.slot_vi: SlotVI = SlotVI()
        self.slot_vii: SlotVII = SlotVII()
        self.slot_viii: Optional[SlotVIII] = None
        self.slot_ix: SlotIX = SlotIX(Case.THM)
        self.slot_x: SlotX = SlotX(Stress.ULTIMATE)

    def set_root(self, root: Root):
        self.slot_iii = SlotIII(root.root)

    def generate(self) -> str:
        result = (
            self.slot_i.generate() +
            self.slot_ii.generate() +
            self.slot_iii.generate() +
            self.slot_iv.generate() +
            self.slot_v.generate() +
            self.slot_vi.generate(
                context=self.slot_iv.context,
                function=self.slot_iv.function,
                specification=self.slot_iv.specification
            ) +
            self.slot_vii.generate()
        )
        if self.slot_viii:
            result += self.slot_viii.generate()
        result += self.slot_ix.generate()
        # Note: Slot X (stress) is not represented in the string directly
        return result

    def parse(self, formative_string: str):
        # This is a simplified parsing logic. In a real implementation,
        # you'd need more sophisticated parsing based on Ithkuil rules.
        self.slot_i.parse(formative_string[0] if formative_string[0] in ['h', 'hw'] else '')
        self.slot_ii.parse(formative_string[1])
        self.slot_iii.parse(formative_string[2:5])  # Assuming a 3-consonant root
        self.slot_iv.parse(formative_string[5])
        # ... continue parsing other slots ...
        self.slot_x.parse(formative_string)  # This would analyze the stress pattern

    def describe(self) -> str:
        return (
            f"Formative:\n"
            f"  Slot I: {self.slot_i.describe()}\n"
            f"  Slot II: {self.slot_ii.describe()}\n"
            f"  Slot III: {self.slot_iii.describe()}\n"
            f"  Slot IV: {self.slot_iv.describe()}\n"
            f"  Slot V: {self.slot_v.describe()}\n"
            f"  Slot VI: {self.slot_vi.describe()}\n"
            f"  Slot VII: {self.slot_vii.describe()}\n"
            f"  Slot VIII: {self.slot_viii.describe() if self.slot_viii else 'Not present'}\n"
            f"  Slot IX: {self.slot_ix.describe()}\n"
            f"  Slot X: {self.slot_x.describe()}"
        )