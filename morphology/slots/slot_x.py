from enum import Enum
from typing import Optional

class Relation(Enum):
    UNFRAMED = 1
    FRAMED = 2

class Stress(Enum):
    ULTIMATE = 1      # Last syllable
    PENULTIMATE = 2   # Second-to-last syllable
    ANTEPENULTIMATE = 3  # Third-to-last syllable

class SlotX:
    def __init__(self, stress: Stress):
        self.stress = stress

    def generate(self) -> str:
        # This method doesn't actually generate anything, as stress is phonological
        # However, it could be used in a larger word-generation context
        return ""

    def parse(self, word: str) -> None:
        # In a real implementation, this would analyze the word's phonology
        # For now, we'll just set a default stress
        self.stress = Stress.ULTIMATE

    def get_relation(self) -> Relation:
        if self.stress == Stress.ANTEPENULTIMATE:
            return Relation.FRAMED
        else:
            return Relation.UNFRAMED

    def describe(self) -> str:
        relation = self.get_relation()
        return f"Stress: {self.stress.name}, Relation: {relation.name}"

# Usage example:
if __name__ == "__main__":
    slot_x = SlotX(Stress.ULTIMATE)
    print(slot_x.describe())  # Should print "Stress: ULTIMATE, Relation: UNFRAMED"

    slot_x = SlotX(Stress.ANTEPENULTIMATE)
    print(slot_x.describe())  # Should print "Stress: ANTEPENULTIMATE, Relation: FRAMED"