from typing import Optional, Dict, List, Union
import json
from functools import lru_cache

class Specs:
    def __init__(self, BSC: str = '', CTE: str = '', CSV: str = '', OBJ: str = ''):
        self.BSC = BSC
        self.CTE = CTE
        self.CSV = CSV
        self.OBJ = OBJ

class SlotIII:
    """Main Root"""

    def __init__(self, root: str):
        self.root = root
        self._root_data: Optional[Dict] = None

    @staticmethod
    @lru_cache(maxsize=1)
    def _load_roots() -> Dict[str, Dict]:
        with open('Pythkuil/resources/lexicon.json', 'r', encoding='utf-8') as f:
            lexicon = json.load(f)
        return {root['root']: root for root in lexicon.get('roots', [])}

    def is_valid(self) -> bool:
        return self.root in self._load_roots()

    def _lazy_load_root_data(self):
        if self._root_data is None:
            self._root_data = self._load_roots().get(self.root)

    def generate(self) -> str:
        return self.root

    def parse(self, input: str) -> 'SlotIII':
        self.root = input
        return self

    def describe(self, stem: int = 0, spec: str = 'BSC') -> str:
        self._lazy_load_root_data()
        if self._root_data is None:
            return f"Invalid root: {self.root}"

        refers = self._root_data.get('refers', '')
        stems = self._root_data.get('stems', [])

        description = f"Root: {self.root}\nRefers to: {refers}\n"

        if 0 <= stem < len(stems):
            stem_data = stems[stem]
            if isinstance(stem_data, dict):
                description += f"Stem {stem}, {spec}: {stem_data.get(spec, 'N/A')}"
            elif isinstance(stem_data, str):
                description += f"Stem {stem}: {stem_data}"
            else:
                description += f"Stem {stem}: Invalid data"
        else:
            description += f"Invalid stem: {stem}"

        if 'notes' in self._root_data:
            description += f"\nNotes: {self._root_data['notes']}"

        if 'see' in self._root_data:
            description += f"\nSee also: {self._root_data['see']}"

        return description

    def get_stems(self) -> List[Union[Specs, str, None]]:
        self._lazy_load_root_data()
        if self._root_data is None:
            return [None, None, None]

        stems = self._root_data.get('stems', [])
        return [Specs(**stem) if isinstance(stem, dict) else stem for stem in stems]

    @classmethod
    def get_all_roots(cls) -> Dict[str, Dict]:
        return cls._load_roots()