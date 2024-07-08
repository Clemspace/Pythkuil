from enum import Enum
from typing import Dict, List, Optional

class Case(Enum):
    # Transrelative Cases
    THM = 1  # Thematic
    INS = 2  # Instrumental
    ABS = 3  # Absolutive
    AFF = 4  # Affective
    STM = 5  # Stimulative
    EFF = 6  # Effectuative
    ERG = 7  # Ergative
    DAT = 8  # Dative
    IND = 9  # Inducive

    # Appositive Cases
    POS = 10  # Possessive
    PRP = 11  # Proprietive
    GEN = 12  # Genitive
    ATT = 13  # Attributive
    PDC = 14  # Productive
    ITP = 15  # Interpretative
    OGN = 16  # Originative
    IDP = 17  # Interdependent
    PAR = 18  # Partitive

    # Associative Cases
    APL = 19  # Applicative
    PUR = 20  # Purposive
    TRA = 21  # Transmissive
    DFR = 22  # Deferential
    CRS = 23  # Contrastive
    TSP = 24  # Transpositive
    CMM = 25  # Commutative
    CMP = 26  # Comparative
    CSD = 27  # Considerative

    # Adverbial Cases
    FUN = 28  # Functive
    TFM = 29  # Transformative
    CLA = 30  # Classificative
    RSL = 31  # Resultative
    CSM = 32  # Consumptive
    CON = 33  # Concessive
    AVR = 34  # Aversive
    CVS = 35  # Conversive
    SIT = 36  # Situative

    # Relational Cases
    PRN = 37  # Pertinential
    DSP = 38  # Descriptive
    COR = 39  # Correlative
    CPS = 40  # Compositive
    COM = 41  # Comitative
    UTL = 42  # Utilitative
    PRD = 43  # Predicative
    RLT = 44  # Relative

    # Affinitive Cases
    ACT = 45  # Activative
    ASI = 46  # Assimilative
    ESS = 47  # Essive
    TRM = 48  # Terminative
    SEL = 49  # Selective
    CFM = 50  # Conformative
    DEP = 51  # Dependent
    VOC = 52  # Vocative

    # Spatio-Temporal Cases I
    LOC = 53  # Locative
    ATD = 54  # Attendant
    ALL = 55  # Allative
    ABL = 56  # Ablative
    ORI = 57  # Orientative
    IRL = 58  # Interrelative
    INV = 59  # Intrative
    NAV = 60  # Navigative

    # Spatio-Temporal Cases II
    CNR = 61  # Concursive
    ASS = 62  # Assessive
    PER = 63  # Periodic
    PRO = 64  # Prolapsive
    PCV = 65  # Precursive
    PCR = 66  # Postcursive
    ELP = 67  # Elapsive
    PLM = 68  # Prolimitive
    
class CaseScope(Enum):
    CCN = 1  # Natural
    CCA = 2  # Antecedent
    CCS = 3  # Subaltern
    CCQ = 4  # Qualifier
    CCP = 5  # Precedent
    CCV = 6  # Successive    

class CaseProperties:
    def __init__(self, name: str, abbreviation: str, description: str, affix: str):
        self.name = name
        self.abbreviation = abbreviation
        self.description = description
        self.affix = affix

class CaseSystem:
    def __init__(self):
        self.cases: Dict[Case, CaseProperties] = self._initialize_cases()
        self.case_scopes: Dict[CaseScope, str] = self._initialize_case_scopes()

    def _initialize_cases(self) -> Dict[Case, CaseProperties]:
        return {
            Case.THM: CaseProperties("Thematic", "THM", "The (usually inanimate) party which is a participant to the verbal predicate which does not undergo any tangible change of state.", "-a"),
            Case.INS: CaseProperties("Instrumental", "INS", "The entity acting as means utilized by an explicit or implicit agent to implement/carry out the effect/impact of an act/event.", "-ä"),
            Case.ABS: CaseProperties("Absolutive", "ABS", "The party that is the target of, or undergoes, the effect/impact or change of state as a result of a tangible act/event.", "-e"),
            Case.AFF: CaseProperties("Affective", "AFF", "The party who undergoes an unwilled, affective experience.", "-i"),
            Case.STM: CaseProperties("Stimulative", "STM", "The party/entity/idea/thought/situation or mental state which triggers an unwilled, affective response or is the trigger for an existential state.", "-ëi"),
            Case.EFF: CaseProperties("Effectuative", "EFF", "The party/force that initiates a chain of causal events or who induces another party to act as an agent.", "-ö"),
            Case.ERG: CaseProperties("Ergative", "ERG", "The animate party or inanimate force which initiates/causes an act/event which creates a tangible effect or change of state in a patient.", "-o"),
            Case.DAT: CaseProperties("Dative", "DAT", "The party which is the (intended) recipient of a verb of transference, transmission, or communication.", "-ü"),
            Case.IND: CaseProperties("Inducive", "IND", "The patient who undergoes the tangible effect, impact, or change of state of an act/event initiated/caused by that self-same party.", "-u"),
            Case.POS: CaseProperties("Possessive", "POS", "Alienable possession.", "-ai"),
            Case.PRP: CaseProperties("Proprietive", "PRP", "Alienable possession in the sense of ownership.", "-au"),
            Case.GEN: CaseProperties("Genitive", "GEN", "Inalienable possession.", "-ei"),
            Case.ATT: CaseProperties("Attributive", "ATT", "Inalienable attribute or characteristic.", "-eu"),
            Case.PDC: CaseProperties("Productive", "PDC", "The creator or originator of another entity.", "-ëu"),
            Case.ITP: CaseProperties("Interpretative", "ITP", "The subjective interpretational context for another noun.", "-ou"),
            Case.OGN: CaseProperties("Originative", "OGN", "The literal or figurative source or origin of another.", "-oi"),
            Case.IDP: CaseProperties("Interdependent", "IDP", "Mutually dependent or complementary relationship.", "-iu"),
            Case.PAR: CaseProperties("Partitive", "PAR", "Quantitative or content-to-container relationship.", "-ui"),
            Case.APL: CaseProperties("Applicative", "APL", "The purpose of another noun.", "-ia"),
            Case.PUR: CaseProperties("Purposive", "PUR", "The purpose or reason for which another noun exists or occurs.", "-ie"),
            Case.TRA: CaseProperties("Transmissive", "TRA", "The party for whose benefit an action/event occurs or a state exists.", "-io"),
            Case.DFR: CaseProperties("Deferential", "DFR", "The party to which a formality or courtesy is paid.", "-iö"),
            Case.CRS: CaseProperties("Contrastive", "CRS", "The party being replaced or substituted for.", "-eë"),
            Case.TSP: CaseProperties("Transpositive", "TSP", "The party for which another is substituted or which is replaced by another.", "-uö"),
            Case.CMM: CaseProperties("Commutative", "CMM", "The party in exchange for which a given action/event/state occurs.", "-uo"),
            Case.CMP: CaseProperties("Comparative", "CMP", "The party being compared to another.", "-ue"),
            Case.CSD: CaseProperties("Considerative", "CSD", "The party or entity according to which a given action/event/state occurs.", "-ua"),
            Case.FUN: CaseProperties("Functive", "FUN", "The manner in which an action/event/state occurs.", "-ao"),
            Case.TFM: CaseProperties("Transformative", "TFM", "The outcome or final state of a process.", "-aö"),
            Case.CLA: CaseProperties("Classificative", "CLA", "The basis for arranging, sorting, classifying, or counting.", "-eo"),
            Case.RSL: CaseProperties("Resultative", "RSL", "The result or consequence of another noun.", "-eö"),
            Case.CSM: CaseProperties("Consumptive", "CSM", "The entity consumed or used as a resource.", "-oë"),
            Case.CON: CaseProperties("Concessive", "CON", "Despite what / in spite of what / notwithstanding what / although / even though.", "-öe"),
            Case.AVR: CaseProperties("Aversive", "AVR", "The source or object of fear, dislike, or avoidance.", "-oe"),
            Case.CVS: CaseProperties("Conversive", "CVS", "The exception or 'loophole' by which an otherwise expected outcome does not occur.", "-öa"),
            Case.SIT: CaseProperties("Situative", "SIT", "The background context for an act/event/state.", "-oa"),
            Case.PRN: CaseProperties("Pertinential", "PRN", "The general referent of another formative.", "-a'"),
            Case.DSP: CaseProperties("Descriptive", "DSP", "The formative described or characterized by another formative.", "-ä'"),
            Case.COR: CaseProperties("Correlative", "COR", "An abstract general relationship between one formative and another.", "-e'"),
            Case.CPS: CaseProperties("Compositive", "CPS", "The literal or figurative substance or component(s) of which another is made/composed.", "-i'"),
            Case.COM: CaseProperties("Comitative", "COM", "The formative that accompanies another.", "-ëi'"),
            Case.UTL: CaseProperties("Utilitative", "UTL", "The formative being used while another activity or state is in progress.", "-ö'"),
            Case.PRD: CaseProperties("Predicative", "PRD", "The non-causal basis, foundation, sustenance, or required existential condition for another formative.", "-o'"),
            Case.RLT: CaseProperties("Relative", "RLT", "The formative constituting a relative clause associated with another formative.", "-u'"),
            Case.ACT: CaseProperties("Activative", "ACT", "The experiencer of a modal state.", "-ai'"),
            Case.ASI: CaseProperties("Assimilative", "ASI", "The formative used as a context for analogy or metaphorical comparison.", "-au'"),
            Case.ESS: CaseProperties("Essive", "ESS", "The role or name by which an entity is known or contextually identified.", "-ei'"),
            Case.TRM: CaseProperties("Terminative", "TRM", "The goal of an act/event.", "-eu'"),
            Case.SEL: CaseProperties("Selective", "SEL", "Recurring time period.", "-ëu'"),
            Case.CFM: CaseProperties("Conformative", "CFM", "The entity in accordance with which, or in conformance to which, another entity is, or an act/event occurs.", "-ou'"),
            Case.DEP: CaseProperties("Dependent", "DEP", "The basis of a dependency phrase on which another formative or phrase is dependent.", "-oi'"),
            Case.VOC: CaseProperties("Vocative", "VOC", "The party being directly addressed.", "-ui'"),
            Case.LOC: CaseProperties("Locative", "LOC", "The location where something is situated or occurs.", "-ia'"),
            Case.ATD: CaseProperties("Attendant", "ATD", "The entity in whose presence something is/occurs.", "-ie'"),
            Case.ALL: CaseProperties("Allative", "ALL", "The entity toward which another is moving/approaching.", "-io'"),
            Case.ABL: CaseProperties("Ablative", "ABL", "The entity away from which another is moving/receding.", "-iö'"),
            Case.ORI: CaseProperties("Orientative", "ORI", "The entity serving as the orientational reference point of another.", "-eë'"),
            Case.IRL: CaseProperties("Interrelative", "IRL", "The entity between which and another, a spatiotemporal relation exists.", "-uö'"),
            Case.INV: CaseProperties("Intrative", "INV", "The spatio-temporal boundary point of a series or sequence of entities.", "-uo'"),
            Case.NAV: CaseProperties("Navigative", "NAV", "The entity whose literal or metaphorical 'path' is being traveled or followed.", "-ua'"),
            Case.CNR: CaseProperties("Concursive", "CNR", "The time during which an event/state occurs.", "-ao'"),
            Case.ASS: CaseProperties("Assessive", "ASS", "The increment of space or time by which a contextual ratio of measurement is created.", "-aö'"),
            Case.PER: CaseProperties("Periodic", "PER", "The span of time/space at whose beginning point an event/state occurs.", "-eo'"),
            Case.PRO: CaseProperties("Prolapsive", "PRO", "The duration of an act, condition, or event.", "-eö'"),
            Case.PCV: CaseProperties("Precursive", "PCV", "The duration of time / span of space preceding an act, condition, or event.", "-oë'"),
            Case.PCR: CaseProperties("Postcursive", "PCR", "The duration of time / span of space following an act, condition, or event.", "-öe'"),
            Case.ELP: CaseProperties("Elapsive", "ELP", "The amount of time or space elapsed between the contextual present and the time/space of the given act/state/event.", "-oe'"),
            Case.PLM: CaseProperties("Prolimitive", "PLM", "The spatio-temporal limit beyond which an act/state/event does not or will not occur.", "-oa'"),
        }

    def _initialize_case_scopes(self) -> Dict[CaseScope, Dict[str, str]]:
        return {
            CaseScope.CCN: {
                "name": "Natural",
                "pattern1": "h",
                "pattern2": "w/y",
                "meaning": "X's case is governed by the noun-case of the formative marked CN = -hl-/-hw-; in the absence of such, X's case is associated with the main verb (or framed verb if within a case-frame)."
            },
            CaseScope.CCA: {
                "name": "Antecedent",
                "pattern1": "hl",
                "pattern2": "hw",
                "meaning": "X is the 'head' whose case governs all CN-unmarked nouns in the clause (or nouns marked with CN = -h- or -w-/y-)"
            },
            CaseScope.CCS: {
                "name": "Subaltern",
                "pattern1": "hr",
                "pattern2": "hrw",
                "meaning": "X is the formative to which formatives in the clause marked with CN = -hm-/-hmw- are associated"
            },
            CaseScope.CCQ: {
                "name": "Qualifier",
                "pattern1": "hm",
                "pattern2": "hmw",
                "meaning": "X is associated by noun-case to the formative marked by CN = -hr-/-hrw-"
            },
            CaseScope.CCP: {
                "name": "Precedent",
                "pattern1": "hn",
                "pattern2": "hnw",
                "meaning": "X's noun-case associates only with the immediately following formative"
            },
            CaseScope.CCV: {
                "name": "Successive",
                "pattern1": "hň",
                "pattern2": "hňw",
                "meaning": "X's noun-case associates only with the immediately preceding formative"
            }
        }

    def get_case_properties(self, case: Case) -> CaseProperties:
        return self.cases[case]

    def get_case_by_affix(self, affix: str) -> Optional[Case]:
        for case, props in self.cases.items():
            if props.affix == affix:
                return case
        return None

    def get_case_scope(self, scope: CaseScope) -> str:
        return self.case_scopes[scope]

    def apply_case_accessor(self, case: Case, is_inverse: bool = False) -> str:
        # TODO: Implement case accessor logic
        pass

    def apply_case_stacking(self, base_case: Case, stacked_case: Case) -> str:
        # TODO: Implement case stacking logic
        pass

# Usage example:
if __name__ == "__main__":
    case_system = CaseSystem()
    thm_case = case_system.get_case_properties(Case.THM)
    print(f"Case: {thm_case.name}, Affix: {thm_case.affix}, Description: {thm_case.description}")

    case_from_affix = case_system.get_case_by_affix("-a")
    if case_from_affix:
        print(f"Case for affix '-a': {case_from_affix.name}")

    ccn_scope = case_system.get_case_scope(CaseScope.CCN)
    print(f"Case-Scope for CCN: {ccn_scope}")