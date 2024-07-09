import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexicon.root_database import RootDatabase
from lexicon.root import Specs

current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the lexicon.json file
lexicon_path =  os.path.join(current_dir, "..", "resources", "lexicon.json")


def test_lexicon():
    # Load the lexicon
    db = RootDatabase.load_from_file(lexicon_path)

    # Count roots and affixes
    root_count = len(db.roots)
    standard_affix_count = len(db.affixes['standard'])
    accessor_affix_count = len(db.affixes['accessor'])
    stacking_affix_count = len(db.affixes['stacking'])

    print(f"Number of roots: {root_count}")
    print(f"Number of standard affixes: {standard_affix_count}")
    print(f"Number of case accessor affixes: {accessor_affix_count}")
    print(f"Number of case stacking affixes: {stacking_affix_count}")

    # Test searching by root
    test_root = 'L'  # You can change this to any root you want to test
    root = db.get_root(test_root)
    if root:
        print(f"\nFound root: {root.root}")
        print(f"Meaning: {root.stems[0].BSC if isinstance(root.stems[0], Specs) else root.stems[0]}")
    else:
        print(f"\nRoot {test_root} not found")

    # Test searching by English equivalent
    test_word = "be"  # You can change this to any English word you want to search for
    matching_roots = [
        root for root in db.roots.values() 
        if any(
            (isinstance(stem, Specs) and any(test_word.lower() in spec.lower() for spec in stem.to_dict().values())) or
            (isinstance(stem, str) and test_word.lower() in stem.lower())
            for stem in root.stems if stem
        )
    ]

    print(f"\nRoots containing '{test_word}':")
    for root in matching_roots[:5]:  # Limit to first 5 results
        print(f"Root: {root.root}")
        print(f"Meaning: {root.stems[0].BSC if isinstance(root.stems[0], Specs) else root.stems[0]}")
        print("---")

if __name__ == "__main__":
    test_lexicon()