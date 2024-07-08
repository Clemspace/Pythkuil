from .configuration import Configuration, get_configuration_affix
from .affiliation import Affiliation, get_affiliation_affix
from .perspective import Perspective, get_perspective_affix
from .extension import Extension, get_extension_affix
from .essence import Essence, get_essence_affix
from .version import Version, get_version_vowel, apply_version
from .function import Function
from .context import Context, get_context_vowel
from .ca_complex import CAComplex, generate_short_form
from .affix import Affix  # Assuming you have an Affix class in affix.py
from .phonology import (is_valid_syllable, apply_phonological_rules, 
                        gemination_rule, consonant_mutation_rule, assign_stress, 
                        syllabify, is_valid_vowel_sequence, transliterate)
from .slots import Slot  # Assuming you have a Slot class or enum in slots.py
from .specification import (Specification, get_specification_vowel, 
                            combine_specification_and_stem, parse_specification_and_stem, 
                            get_specification_description, apply_specification)
from .stem import Stem, get_stem_vowel, parse_stem, get_stem_description, apply_stem_to_root

