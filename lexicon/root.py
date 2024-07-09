from typing import Dict, Optional

class Root:
    def __init__(self, consonantal_form: str, meaning: str, stems: Dict[int, Dict[str, str]], associated_affix: Optional[str] = None):
        self.consonantal_form = consonantal_form
        self.meaning = meaning
        self.stems = stems
        self.associated_affix = associated_affix

    def __str__(self):
        return f"Root: {self.consonantal_form} - {self.meaning}"

    def get_stem(self, stem_number: int, specification: str) -> str:
        return self.stems.get(stem_number, {}).get(specification, "")

    def to_dict(self) -> Dict:
        return {
            "consonantal_form": self.consonantal_form,
            "meaning": self.meaning,
            "stems": self.stems,
            "associated_affix": self.associated_affix
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Root':
        return cls(
            data['consonantal_form'],
            data['meaning'],
            data['stems'],
            data.get('associated_affix')
        )