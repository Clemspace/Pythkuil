import os
import sys
import re
import logging
from typing import Dict, List
from collections import defaultdict
from io import StringIO

from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexicon.root import Root
from lexicon.root_database import RootDatabase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ITHKUIL_CONSONANTS = r"[BCČÇDFJKLMNŇPQRSŠTVXZŽĻŘŢ]"
ITHKUIL_CONSONANTS_WITH_MODS = r"[BCČÇDFJKLMNŇPQRSŠTVXZŽĻŘŢ]['H]?"

def extract_text_from_pdf(pdf_path: str) -> str:
    output = StringIO()
    with open(pdf_path, 'rb') as file:
        extract_text_to_fp(file, output, laparams=LAParams(), output_type='text', codec='utf-8')
    return output.getvalue()

def extract_roots_from_pdf(pdf_path: str) -> RootDatabase:
    root_db = RootDatabase()
    text = extract_text_from_pdf(pdf_path)
    
    # Extract root patterns
    root_pattern = rf"(?:^|\n)(-({ITHKUIL_CONSONANTS_WITH_MODS})+-)(?:\s+([^-]+?)(?=\n-({ITHKUIL_CONSONANTS_WITH_MODS})+-|\Z)|\s*$)"
    root_entries = re.finditer(root_pattern, text, re.DOTALL)
    
    for entry in root_entries:
        consonantal_form = entry.group(1)[1:-1]  # Remove hyphens
        content = entry.group(3).strip() if entry.group(3) else ""
        root = parse_root_entry(consonantal_form, content, root_db)
        if root:
            root_db.add_root(root)
        else:
            logging.warning(f"Failed to parse root: {consonantal_form}")
    
    # Extract roots from the "The following stems" section
    extract_following_stems(text, root_db)
    
    expand_abbreviated_definitions(root_db)
    
    return root_db

def parse_root_entry(consonantal_form: str, content: str, root_db: RootDatabase) -> Root:
    meaning = re.search(r'(.*?)(?=STEM 1:|STEM 2:|STEM 3:|BSC|CTE|CSV|OBJ|$)', content, re.DOTALL)
    meaning = meaning.group(1).strip() if meaning else ""
    
    stems = defaultdict(dict)
    
    # Check for reference to previous pattern
    pattern_reference = re.search(r'(?:follow|have) the (?:same|following) (?:Specification|Stem) pattern as (?:the root|Sec\.) ([-\w]+)', content)
    if pattern_reference:
        referenced_root = pattern_reference.group(1)
        if referenced_root in root_db.roots:
            return Root(consonantal_form, meaning, root_db.roots[referenced_root].stems, None)
    
    # Check for the pattern with all specifications for stem 1
    full_spec_match = re.search(r'STEM 1.*?(?=STEM 2|\Z)', content, re.DOTALL)
    if full_spec_match:
        stem_info = full_spec_match.group(0)
        for spec in ['BSC', 'CTE', 'CSV', 'OBJ']:
            spec_match = re.search(rf'{spec}\s+(.*?)(?=BSC|CTE|CSV|OBJ|\Z)', stem_info, re.DOTALL)
            if spec_match:
                stems[1][spec] = spec_match.group(1).strip()
    
    # Check for the pattern with numbered stems
    stem_matches = list(re.finditer(r'(?:STEM|Stem) (\d+)(?:\s*\((.*?)\))?:\s*(.*?)(?=(?:STEM|Stem) \d+|\Z)', content, re.DOTALL))
    if stem_matches:
        for stem_match in stem_matches:
            stem_number = int(stem_match.group(1))
            stem_info = stem_match.group(3).strip()
            stems[stem_number]['BSC'] = stem_info
    
    # Check for the pattern with numbered definitions
    num_def_matches = re.finditer(r'(\d+)\.\s*(.*?)(?=\d+\.|\Z)', content, re.DOTALL)
    if num_def_matches:
        for i, match in enumerate(num_def_matches, start=1):
            stems[i]['BSC'] = match.group(2).strip()
    
    # Ensure we have 3 stems at least
    for i in range(1, 4):
        if i not in stems:
            stems[i] = {'BSC': f"(Stem {i} not specified)"}
    
    associated_affix = re.search(r'Associated Affix:\s*(.*?)(?:\n|$)', content)
    associated_affix = associated_affix.group(1).strip() if associated_affix else None
    
    return Root(consonantal_form, meaning, dict(stems), associated_affix)

def extract_following_stems(text: str, root_db: RootDatabase):
    following_stems_pattern = rf"The following (?:roots/stems|stems) .* (?:have|follow) the same Specification pattern as (?:the root|Sec\.) ([-\w]+).*?:\s*((?:-({ITHKUIL_CONSONANTS_WITH_MODS})+-.*?)+)(?=\n\n|\Z)"
    following_stems_sections = re.finditer(following_stems_pattern, text, re.DOTALL)
    for section in following_stems_sections:
        pattern_root = section.group(1)
        if pattern_root in root_db.roots:
            individual_root_pattern = rf"-({ITHKUIL_CONSONANTS_WITH_MODS}+)-\s*(.*?)(?=-({ITHKUIL_CONSONANTS_WITH_MODS})+-|\Z)"
            roots = re.finditer(individual_root_pattern, section.group(2), re.DOTALL)
            for root in roots:
                consonantal_form = root.group(1)
                content = root.group(2).strip()
                new_root = Root(consonantal_form, f"(As per {pattern_root})", root_db.roots[pattern_root].stems, None)
                root_db.add_root(new_root)

def expand_abbreviated_definitions(root_db: RootDatabase):
    for root in root_db.roots.values():
        if root.meaning.startswith("(As per"):
            referenced_root = root.meaning[8:-1]
            if referenced_root in root_db.roots:
                root.stems = root_db.roots[referenced_root].stems.copy()

def test_pdf_parsing():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "..", "resources", "newithkuil_lexicon.pdf")
    
    logging.info(f"Extracting roots from {pdf_path}")
    root_db = extract_roots_from_pdf(pdf_path)
    
    logging.info(f"Extracted {len(root_db.roots)} roots")
    
    json_path = os.path.join(current_dir, "..", "resources", "root_database.json")
    root_db.save_to_file(json_path)
    logging.info(f"Saved root database to {json_path}")
    
    loaded_db = RootDatabase.load_from_file(json_path)
    logging.info(f"Loaded {len(loaded_db.roots)} roots from JSON file")
    
    # Test a few specific roots
    test_roots = ['CŇ', 'ČV', 'GPW', 'RČV', 'S', 'T', 'ŇM', 'MSFR', 'MMZBW']
    for root in test_roots:
        if root in loaded_db.roots:
            logging.info(f"\nTesting root: {root}")
            logging.info(loaded_db.roots[root])
            logging.info(f"Associated Affix: {loaded_db.roots[root].associated_affix}")
            for stem_num, stem_data in loaded_db.roots[root].stems.items():
                logging.info(f"Stem {stem_num}:")
                for spec, value in stem_data.items():
                    logging.info(f"  {spec}: {value}")
        else:
            logging.warning(f"Root {root} not found in loaded database")
    
    logging.info("\nAll tests completed!")

if __name__ == "__main__":
    test_pdf_parsing()
