from .slots import (
    SlotI, SlotII, SlotIII, SlotIV, SlotV, SlotVI, SlotVII, SlotVIII, SlotIX, SlotX
)
from .slots.slot_ii import Version
from .configuration import Configuration
from .affiliation import Affiliation
from .perspective import Perspective
from .extension import Extension
from .essence import Essence

from .ca_complex import CAComplex
from .affixes import VxCsAffix
from .phonology import (
    is_valid_syllable, apply_phonological_rules, gemination_rule, 
    consonant_mutation_rule, assign_stress, syllabify, 
    is_valid_vowel_sequence, transliterate
)