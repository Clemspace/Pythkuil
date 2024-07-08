from enum import Enum
from typing import Dict

class Stem(Enum):
    S0 = 0  # Stem Zero
    S1 = 1  # Stem 1
    S2 = 2  # Stem 2
    S3 = 3  # Stem 3

def get_stem_vowel(stem: Stem) -> str:
    vowels: Dict[Stem, str] = {
        Stem.S0: 'o',
        Stem.S1: 'a',
        Stem.S2: 'e',
        Stem.S3: 'u'
    }
    return vowels[stem]

def parse_stem(vowel: str) -> Stem:
    stems: Dict[str, Stem] = {
        'o': Stem.S0,
        'a': Stem.S1,
        'e': Stem.S2,
        'u': Stem.S3
    }
    return stems.get(vowel, Stem.S1)  # Default to Stem 1 if not found

def get_stem_description(stem: Stem) -> str:
    descriptions: Dict[Stem, str] = {
        Stem.S0: "Stem Zero: Specialized form referring to the overall conceptual meaning of the raw root.",
        Stem.S1: "Stem 1: The first instantiated meaning of the root.",
        Stem.S2: "Stem 2: The second instantiated meaning of the root.",
        Stem.S3: "Stem 3: The third instantiated meaning of the root."
    }
    return descriptions[stem]

def apply_stem_to_root(root: str, stem: Stem) -> str:
    stem_vowel = get_stem_vowel(stem)
    return f"{root[0]}{stem_vowel}{root[1:]}"

# Example usage
if __name__ == "__main__":
    root = "lk"
    stem = Stem.S2
    
    result = apply_stem_to_root(root, stem)
    print(f"Applied stem: {result}")
    
    parsed_stem = parse_stem(result[1])
    print(f"Parsed stem: {parsed_stem}")
    print(f"Stem description: {get_stem_description(parsed_stem)}")