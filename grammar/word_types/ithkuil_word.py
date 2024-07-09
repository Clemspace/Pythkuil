from abc import ABC, abstractmethod

class IthkuilWord(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass