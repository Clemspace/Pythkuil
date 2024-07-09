from .ithkuil_word import IthkuilWord

class Special_Construct(IthkuilWord):
    def describe(self) -> str:
        return f"Special Construct: {self.__dict__}"

# Similar for Referential, Adjunct, SpecialConstruct, Numerical