from enum import Enum
from typing import Optional

class Valence(Enum):
    MNO = 'a'    # Monoactive
    PRL = 'ä'    # Parallel
    CRO = 'e'    # Corollary
    RCP = 'i'    # Reciprocal
    CPL = 'ëi'   # Complementary
    DUP = 'ö'    # Duplicative
    DEM = 'o'    # Demonstrative
    CNG = 'ü'    # Contingent
    PTI = 'u'    # Participative

class Phase(Enum):
    PCT = 'ai'   # Punctual
    ITR = 'au'   # Iterative
    REP = 'ei'   # Repetitive
    ITM = 'eu'   # Intermittent
    RCT = 'ëu'   # Recurrent
    FRE = 'ou'   # Frequentative
    FRG = 'oi'   # Fragmentative
    VAC = 'iu'   # Vacillative
    FLC = 'ui'   # Fluctuative

class Effect(Enum):
    BEN1 = 'ia'  # Beneficial to Speaker
    BEN2 = 'ie'  # Beneficial to Addressee
    BEN3 = 'io'  # Beneficial to Third Party
    BEN0 = 'iö'  # Beneficial to Self
    UNK  = 'eë'  # Unknown Benefit
    DET0 = 'uö'  # Detrimental to Self
    DET3 = 'uo'  # Detrimental to Third Party
    DET2 = 'ue'  # Detrimental to Addressee
    DET1 = 'ua'  # Detrimental to Speaker

class Level(Enum):
    MIN = 'ao'   # Minimal
    SBE = 'aö'   # Subequative
    IFR = 'eo'   # Inferior
    DFT = 'eö'   # Deficient
    EQU = 'oë'   # Equative
    SUR = 'oe'   # Surpassive
    SPL = 'öe'   # Superlative
    SPQ = 'öa'   # Superequative
    MAX = 'oa'   # Maximal

class Mood(Enum):
    FAC = 'h'    # Factual
    SUB = 'hl'   # Subjunctive
    ASM = 'hr'   # Assumptive
    SPC = 'hm'   # Speculative
    COU = 'hn'   # Counterfactive
    HYP = 'hň'   # Hypothetical

class SlotVIII:
    def __init__(self, valence: Optional[Valence] = None, 
                 phase: Optional[Phase] = None, 
                 effect: Optional[Effect] = None, 
                 level: Optional[Level] = None,
                 mood: Optional[Mood] = None):
        self.valence = valence
        self.phase = phase
        self.effect = effect
        self.level = level
        self.mood = mood

    def generate(self) -> str:
        vn = ''
        if self.valence:
            vn = self.valence.value
        elif self.phase:
            vn = self.phase.value
        elif self.effect:
            vn = self.effect.value
        elif self.level:
            vn = self.level.value
        
        cn = self.mood.value if self.mood else ''
        
        return vn + cn

    def parse(self, input: str):
        # Implement parsing logic here
        pass

    def describe(self) -> str:
        components = []
        if self.valence:
            components.append(f"Valence: {self.valence.name}")
        if self.phase:
            components.append(f"Phase: {self.phase.name}")
        if self.effect:
            components.append(f"Effect: {self.effect.name}")
        if self.level:
            components.append(f"Level: {self.level.name}")
        if self.mood:
            components.append(f"Mood: {self.mood.name}")
        return ", ".join(components)