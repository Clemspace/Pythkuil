from typing import List, Dict, Optional, Union

class Specs:
    def __init__(self, **kwargs):
        self.BSC = kwargs.get('BSC', '')
        self.CTE = kwargs.get('CTE', '')
        self.CSV = kwargs.get('CSV', '')
        self.OBJ = kwargs.get('OBJ', '')

    def to_dict(self) -> Dict[str, str]:
        return {
            "BSC": self.BSC,
            "CTE": self.CTE,
            "CSV": self.CSV,
            "OBJ": self.OBJ
        }

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
                stems.append(Specs(**stem))
            else:
                stems.append(stem)
        
        return cls(
            root=data['root'],
            refers=data.get('refers'),
            stems=stems,
            notes=data.get('notes'),
            see=data.get('see')
        )