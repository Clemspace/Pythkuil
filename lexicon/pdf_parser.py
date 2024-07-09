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

def extract_text_from_pdf(pdf_path: str) -> str:
    output = StringIO()
    with open(pdf_path, 'rb') as file:
        extract_text_to_fp(file, output, laparams=LAParams(), output_type='text', codec='utf-8')
    return output.getvalue()

def extract_roots_from_pdf(pdf_path: str) -> RootDatabase:
    root_db = RootDatabase()
    text = extract_text_from_pdf(pdf_path)
    
    # Improved regex for root extraction
    root_entries = re.finditer(r'(?:^|\n)(-[A-ZČŠŽŇ]\w+-)(?:\s+([^-]+?)(?=\n-[A-ZČŠŽŇ]\w+-|\Z)|\s*$)', text, re.DOTALL)
    
    for entry in root_entries:
        consonantal_form = entry.group(1)[1:-1]  # Remove hyphens
        content = entry.group(2).strip() if entry.group(2) else ""
        root = parse_root_entry(consonantal_form, content)
        if root:
            root_db.add_root(root)
        else:
            logging.warning(f"Failed to parse root: {consonantal_form}")
    
    expand_abbreviated_definitions(root_db)
    
    return root_db

def parse_root_entry(consonantal_form: str, content: str) -> Root:
    meaning = re.search(r'(.*?)(?=STEM 1:|STEM 2:|STEM 3:|$)', content, re.DOTALL)
    meaning = meaning.group(1).strip() if meaning else ""
    
    stems = defaultdict(dict)
    stem_matches = list(re.finditer(r'STEM (\d+)(?:\s*\((.*?)\))?:\s*(.*?)(?=STEM \d+|\Z)', content, re.DOTALL))
    
    if not stem_matches:
        # For roots that reference previous definitions or have a different format
        stem_contents = re.split(r'\s*\d+\.\s*', content)
        if len(stem_contents) > 1:
            for i, stem_content in enumerate(stem_contents[1:], start=1):
                stems[i]['BSC'] = stem_content.strip()
        else:
            stems[1]['BSC'] = content.strip()
    else:
        for stem_match in stem_matches:
            stem_number = int(stem_match.group(1))
            stem_info = stem_match.group(3).strip()
            
            spec_matches = re.finditer(r'(BSC|CTE|CSV|OBJ)(?:\s*\((.*?)\))?:\s*(.*?)(?=(?:BSC|CTE|CSV|OBJ)|\Z)', stem_info, re.DOTALL)
            for spec_match in spec_matches:
                spec, qualifier, definition = spec_match.groups()
                stems[stem_number][spec] = definition.strip()
                if qualifier:
                    stems[stem_number][f"{spec}_qualifier"] = qualifier.strip()
    
    # Ensure we have 18 stems
    for i in range(1, 19):
        if i not in stems:
            stems[i] = {'BSC': f"(Stem {i} not specified)"}
    
    associated_affix = re.search(r'Associated Affix:\s*(.*?)(?:\n|$)', content)
    associated_affix = associated_affix.group(1).strip() if associated_affix else None
    
    return Root(consonantal_form, meaning, dict(stems), associated_affix)

def expand_abbreviated_definitions(root_db: RootDatabase):
    pattern_roots = [root for root in root_db.roots.values() if "The following" in root.meaning]
    
    for pattern_root in pattern_roots:
        pattern = pattern_root.stems
        referenced_roots = [root for root in root_db.roots.values() if not root.meaning and len(root.stems) == len(pattern)]
        
        for ref_root in referenced_roots:
            for stem_num, stem_specs in pattern.items():
                for spec, _ in stem_specs.items():
                    if spec not in ref_root.stems[stem_num]:
                        ref_root.stems[stem_num][spec] = f"(As per {pattern_root.consonantal_form})"

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
    test_roots = ['CŇ', 'ČV', 'GPW', 'RČV']
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