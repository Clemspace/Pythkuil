from typing import Union
from ..word_types import Formative, Referential, Adjunct, SpecialConstruct, Numerical
from .formative_parser import FormativeParser
from .referential_parser import ReferentialParser
from .adjunct_parser import AdjunctParser
from .special_construct_parser import SpecialConstructParser
from .numerical_parser import NumericalParser

class IthkuilParser:
    @staticmethod
    def parse_word(word: str) -> Union[Formative, Referential, Adjunct, SpecialConstruct, Numerical]:
        if IthkuilParser.is_formative(word):
            return FormativeParser.parse(word)
        elif IthkuilParser.is_referential(word):
            return ReferentialParser.parse(word)
        elif IthkuilParser.is_adjunct(word):
            return AdjunctParser.parse(word)
        elif IthkuilParser.is_special_construct(word):
            return SpecialConstructParser.parse(word)
        elif IthkuilParser.is_numerical(word):
            return NumericalParser.parse(word)
        else:
            raise ValueError(f"Unknown word type: {word}")

    @staticmethod
    def is_formative(word: str) -> bool:
        # Implement formative identification logic
        pass

    # Similar methods for other word types