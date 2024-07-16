from typing import List, Dict, Optional, Union
from dataclasses import dataclass

@dataclass
class Specs:
    BSC: str = ""
    CTE: str = ""
    CSV: str = ""
    OBJ: str = ""

    def to_dict(self) -> Dict[str, str]:
        return {
            "BSC": self.BSC,
            "CTE": self.CTE,
            "CSV": self.CSV,
            "OBJ": self.OBJ
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Specs':
        return cls(**data)

class Root:
    def __init__(self, root: str, refers: Optional[str] = None, 
                 stems: Optional[List[Union[Specs, str]]] = None,
                 notes: Optional[str] = None, see: Optional[str] = None):
        self.root = root
        self.refers = refers
        self.stems = stems or [None, None, None]
        self.notes = notes
        self.see = see

    def to_dict(self) -> Dict:
        return {
            "root": self.root,
            "refers": self.refers,
            "stems": [stem.to_dict() if isinstance(stem, Specs) else stem for stem in self.stems if stem is not None],
            "notes": self.notes,
            "see": self.see
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Root':
        stems = []
        for stem in data.get('stems', []):
            if isinstance(stem, dict):
                stems.append(Specs.from_dict(stem))
            else:
                stems.append(stem)
        
        return cls(
            root=data['root'],
            refers=data.get('refers'),
            stems=stems,
            notes=data.get('notes'),
            see=data.get('see')
        )

    def get_stem(self, index: int) -> Optional[Union[Specs, str]]:
        if 0 <= index < len(self.stems):
            return self.stems[index]
        return None

    def get_spec(self, stem_index: int, spec: str) -> Optional[str]:
        stem = self.get_stem(stem_index)
        if isinstance(stem, Specs):
            return getattr(stem, spec, None)
        return stem if isinstance(stem, str) else None

    def describe(self, stem_index: int = 0, spec: str = 'BSC') -> str:
        description = f"Root: {self.root}\n"
        if self.refers:
            description += f"Refers to: {self.refers}\n"
        
        stem = self.get_stem(stem_index)
        if stem is None:
            description += f"Invalid stem: {stem_index}\n"
        elif isinstance(stem, Specs):
            description += f"Stem {stem_index}, {spec}: {getattr(stem, spec, 'N/A')}\n"
        else:
            description += f"Stem {stem_index}: {stem}\n"
        
        if self.notes:
            description += f"Notes: {self.notes}\n"
        if self.see:
            description += f"See also: {self.see}\n"
        
        return description.strip()