from enum import Enum
from typing import Optional
from .ithkuil_word import IthkuilWord

class NumberType(Enum):
    CARDINAL = 1
    INTEGER = 2
    RATIONAL = 3
    REAL = 4
    IRRATIONAL = 5
    IMAGINARY = 6
    VARIABLE = 7
    COEFFICIENT = 8
    CONSTANT = 9

class MathOperation(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4

class Numerical(IthkuilWord):
    def __init__(self, value: int, root: str, stem: int, specification: str, number_type: NumberType):
        super().__init__()
        self.value = value
        self.root = root
        self.stem = stem
        self.specification = specification
        self.number_type = number_type
        self.tnx_affix: Optional[int] = None
        self.comitative_case: Optional[int] = None
        self.coo_affix: Optional[int] = None
        self.operation: Optional[MathOperation] = None

    def describe(self) -> str:
        description = f"Numerical: {self.value}\n"
        description += f"Root: {self.root}\n"
        description += f"Stem: {self.stem}\n"
        description += f"Specification: {self.specification}\n"
        description += f"Number Type: {self.number_type.name}\n"
        if self.tnx_affix is not None:
            description += f"TNX Affix: {self.tnx_affix}\n"
        if self.comitative_case is not None:
            description += f"Comitative Case: {self.comitative_case}\n"
        if self.coo_affix is not None:
            description += f"COO Affix: {self.coo_affix}\n"
        if self.operation is not None:
            description += f"Operation: {self.operation.name}\n"
        return description

    def to_ithkuil_text(self) -> str:
        # Implementation depends on specific rules of number formation in Ithkuil
        pass