from enum import Enum
from typing import Optional

class ConcatenationStatus(Enum):
    NONE = ""
    TYPE1 = "h"
    TYPE2 = "hw"

class SlotI:
    """Concatenation Status Indicator"""

    def __init__(self, concatenation_status: ConcatenationStatus = ConcatenationStatus.NONE):
        self.concatenation_status = concatenation_status

    def generate(self) -> str:
        return self.concatenation_status.value

    def parse(self, input: Optional[str]):
        if input is None or input == "":
            self.concatenation_status = ConcatenationStatus.NONE
        elif input == "h":
            self.concatenation_status = ConcatenationStatus.TYPE1
        elif input == "hw":
            self.concatenation_status = ConcatenationStatus.TYPE2
        else:
            raise ValueError(f"Invalid input for SlotI: {input}")

    def describe(self) -> str:
        descriptions = {
            ConcatenationStatus.NONE: "No concatenation",
            ConcatenationStatus.TYPE1: "Type-1 concatenation: the formative represents the beginning of a new conceptual unit",
            ConcatenationStatus.TYPE2: "Type-2 concatenation: the formative represents a continuation of the previous conceptual unit"
        }
        return f"Concatenation Status: {self.concatenation_status.name} ({descriptions[self.concatenation_status]})"

    @classmethod
    def is_valid_concatenation(cls, input: Optional[str]) -> bool:
        return input in ["", None, "h", "hw"]