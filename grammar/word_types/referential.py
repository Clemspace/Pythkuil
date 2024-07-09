from .ithkuil_word import IthkuilWord

class Referential(IthkuilWord):
    def describe(self) -> str:
        return f"Referential: {self.__dict__}"

# Similar for Referential, Adjunct, SpecialConstruct, Numerical