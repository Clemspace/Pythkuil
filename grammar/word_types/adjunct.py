from .ithkuil_word import IthkuilWord

class Adjunct(IthkuilWord):
    def describe(self) -> str:
        return f"Adjunct: {self.__dict__}"

# Similar for Referential, Adjunct, SpecialConstruct, Numerical