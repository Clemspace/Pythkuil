from abc import ABC, abstractmethod
from .slot_i import SlotI
from .slot_ii import SlotII
from .slot_iii import SlotIII
from .slot_iv import SlotIV
from .slot_v import SlotV
from .slot_vi import SlotVI
from .slot_vii import SlotVII
from .slot_viii import SlotVIII
from .slot_ix import SlotIX
from .slot_x import SlotX

class Slot(ABC):
    @abstractmethod
    def generate(self) -> str:
        """Generate the string representation of the slot."""
        pass

    @abstractmethod
    def parse(self, input: str):
        """Parse the input string and set the slot's attributes."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Return a description of the slot's current state."""
        pass
