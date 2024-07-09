from typing import List, Dict, Union, Optional

class Degree:
    def __init__(self, value: Union[str, List[str]]):
        self.value = value

    def to_dict(self) -> Union[str, List[str]]:
        return self.value

class StandardAffix:
    def __init__(self, name: str, description: str, gradient_type: str, cs: str,
                 associated_root: bool, degrees: List[Optional[Degree]], notes: Optional[str] = None):
        self.name = name
        self.description = description
        self.gradient_type = gradient_type
        self.cs = cs
        self.associated_root = associated_root
        self.degrees = degrees
        self.notes = notes

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "gradient_type": self.gradient_type,
            "cs": self.cs,
            "associated_root": self.associated_root,
            "degrees": [degree.to_dict() if degree else None for degree in self.degrees],
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'StandardAffix':
        degrees = [Degree(d) if d else None for d in data['degrees']]
        return cls(
            name=data['name'],
            description=data['description'],
            gradient_type=data['gradient_type'],
            cs=data['cs'],
            associated_root=data['associated_root'],
            degrees=degrees,
            notes=data.get('notes')
        )

class Case:
    def __init__(self, cs: str, vx: List[str], description: str):
        self.cs = cs
        self.vx = vx
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "cs": self.cs,
            "vx": self.vx,
            "description": self.description
        }

class CaseAccessorAffix:
    def __init__(self, name: str, description: str, gradient_type: str, types: List[List[Case]]):
        self.name = name
        self.description = description
        self.gradient_type = gradient_type
        self.types = types

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "gradient_type": self.gradient_type,
            "types": [[case.to_dict() for case in type_] for type_ in self.types]
        }

class CaseStackingAffix:
    def __init__(self, name: str, description: str, gradient_type: str, cases: List[Case]):
        self.name = name
        self.description = description
        self.gradient_type = gradient_type
        self.cases = cases

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "gradient_type": self.gradient_type,
            "cases": [case.to_dict() for case in self.cases]
        }