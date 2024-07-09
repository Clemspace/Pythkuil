import json
from typing import List, Dict, Optional, Iterator
from .root import Root

class RootDatabase:
    def __init__(self):
        self.roots: Dict[str, Root] = {}

    def add_root(self, root: Root):
        self.roots[root.consonantal_form] = root

    def get_root(self, consonantal_form: str) -> Optional[Root]:
        return self.roots.get(consonantal_form)

    def save_to_file(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.roots.items()}, f, indent=2, ensure_ascii=False)

    @classmethod
    def load_from_file(cls, filename: str) -> 'RootDatabase':
        db = cls()
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for consonantal_form, root_data in data.items():
                db.add_root(Root.from_dict(root_data))
        return db

    def search_by_meaning(self, query: str) -> List[Root]:
        return [root for root in self.roots.values() if query.lower() in root.meaning.lower()]

    def search_by_affix(self, affix: str) -> List[Root]:
        return [root for root in self.roots.values() if root.associated_affix and affix.lower() in root.associated_affix.lower()]

    def __len__(self) -> int:
        return len(self.roots)

    def __iter__(self) -> Iterator[Root]:
        return iter(self.roots.values())

    def __getitem__(self, consonantal_form: str) -> Root:
        return self.roots[consonantal_form]

    def __contains__(self, consonantal_form: str) -> bool:
        return consonantal_form in self.roots