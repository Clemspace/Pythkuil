import json
from typing import Dict, List
from .root import Root
from .affix import StandardAffix, CaseAccessorAffix, CaseStackingAffix

class RootDatabase:
    def __init__(self):
        self.roots: Dict[str, Root] = {}
        self.affixes: Dict[str, List] = {
            "standard": [],
            "accessor": [],
            "stacking": []
        }

    def add_root(self, root: Root):
        self.roots[root.root] = root

    def get_root(self, consonantal_form: str) -> Root:
        return self.roots.get(consonantal_form)

    def add_affix(self, affix_type: str, affix):
        if affix_type in self.affixes:
            self.affixes[affix_type].append(affix)

    def save_to_file(self, filename: str):
        data = {
            "roots": [root.to_dict() for root in self.roots.values()],
            "affixes": {
                "standard": [affix.to_dict() for affix in self.affixes["standard"]],
                "accessor": [affix.to_dict() for affix in self.affixes["accessor"]],
                "stacking": [affix.to_dict() for affix in self.affixes["stacking"]]
            }
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'RootDatabase':
        db = cls()
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for root_data in data['roots']:
                db.add_root(Root.from_dict(root_data))
            for affix_data in data['affixes']['standard']:
                db.add_affix("standard", StandardAffix.from_dict(affix_data))
            for affix_data in data['affixes']['accessor']:
                db.add_affix("accessor", CaseAccessorAffix(**affix_data))
            for affix_data in data['affixes']['stacking']:
                db.add_affix("stacking", CaseStackingAffix(**affix_data))
        return db

    def __len__(self) -> int:
        return len(self.roots)

    def __iter__(self):
        return iter(self.roots.values())

    def __getitem__(self, consonantal_form: str) -> Root:
        return self.roots[consonantal_form]

    def __contains__(self, consonantal_form: str) -> bool:
        return consonantal_form in self.roots