from enum import Enum
from typing import Dict, Tuple

class Specification(Enum):
    BSC = 1  # Basic
    CTE = 2  # Contential
    CSV = 3  # Constitutive
    OBJ = 4  # Objective

class Function(Enum):
    STA = 1  # Stative
    DYN = 2  # Dynamic

class Stem(Enum):
    S0 = 0  # Stem Zero
    S1 = 1  # Stem 1
    S2 = 2  # Stem 2
    S3 = 3  # Stem 3

def get_specification_vowel(spec: Specification) -> str:
    vowels = {
        Specification.BSC: 'a',
        Specification.CTE: 'ä',
        Specification.CSV: 'e',
        Specification.OBJ: 'i'
    }
    return vowels[spec]

def get_stem_vowel(stem: Stem) -> str:
    vowels = {
        Stem.S0: 'o',
        Stem.S1: 'a',
        Stem.S2: 'e',
        Stem.S3: 'u'
    }
    return vowels[stem]

def combine_specification_and_stem(spec: Specification, stem: Stem, func: Function) -> str:
    spec_vowel = get_specification_vowel(spec)
    stem_vowel = get_stem_vowel(stem)
    
    if func == Function.STA:
        return f"{stem_vowel}{spec_vowel}"
    else:  # Function.DYN
        return f"{spec_vowel}{stem_vowel}"

def parse_specification_and_stem(vowel_form: str) -> Tuple[Specification, Stem, Function]:
    reverse_spec = {v: k for k, v in {s: get_specification_vowel(s) for s in Specification}.items()}
    reverse_stem = {v: k for k, v in {s: get_stem_vowel(s) for s in Stem}.items()}
    
    if vowel_form[0] in reverse_stem:
        func = Function.STA
        stem = reverse_stem[vowel_form[0]]
        spec = reverse_spec[vowel_form[1]]
    else:
        func = Function.DYN
        spec = reverse_spec[vowel_form[0]]
        stem = reverse_stem[vowel_form[1]]
    
    return spec, stem, func

def get_specification_description(spec: Specification) -> str:
    descriptions = {
        Specification.BSC: "BASIC: A holistic instantiation of a stem, encompassing both the 'contential' and 'constitutive' meanings.",
        Specification.CTE: "CONTENTIAL: The content, essence, or purposeful function of the stem.",
        Specification.CSV: "CONSTITUTIVE: The form or shape in which the stem is expressed or realized.",
        Specification.OBJ: "OBJECTIVE: The most salient concrete associated object or semantic patient of the stem."
    }
    return descriptions[spec]

def apply_specification(root: str, spec: Specification, stem: Stem, func: Function) -> str:
    vowel_form = combine_specification_and_stem(spec, stem, func)
    return f"{root[0]}{vowel_form}{root[1:]}"

# Example usage
if __name__ == "__main__":
    root = "lk"
    spec = Specification.BSC
    stem = Stem.S1
    func = Function.STA
    
    result = apply_specification(root, spec, stem, func)
    print(f"Applied specification: {result}")
    
    parsed_spec, parsed_stem, parsed_func = parse_specification_and_stem(result[1:3])
    print(f"Parsed result: Specification={parsed_spec}, Stem={parsed_stem}, Function={parsed_func}")
    print(f"Specification description: {get_specification_description(parsed_spec)}")