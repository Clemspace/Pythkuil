import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path):
    if not os.path.exists(path):
        open(path, 'a').close()
        print(f"Created file: {path}")
    else:
        print(f"File already exists (not modified): {path}")

def move_file(src, dst):
    if os.path.exists(src):
        if not os.path.exists(dst):
            os.rename(src, dst)
            print(f"Moved {src} to {dst}")
        else:
            print(f"Destination file already exists (not moved): {dst}")
    else:
        print(f"Source file does not exist (not moved): {src}")

def restructure_project():
    # Define the new structure
    new_structure = {
        'compiler': ['__init__.py', 'tokenizer.py', 'formative_parser.py', 'syntax_analyzer.py', 
                     'semantic_analyzer.py', 'error_reporter.py', 'ithkuil_compiler.py'],
        'grammar': ['__init__.py', 'cases.py'],
        'grammar/word_types': ['__init__.py', 'formative.py', 'adjunct.py'],
        'grammar/parsers': ['__init__.py'],
        'lexicon': ['__init__.py', 'root.py', 'affix.py', 'root_database.py'],
        'morphology': ['__init__.py', 'slots.py', 'affiliation.py', 'configuration.py'],
        'phonology': ['__init__.py', 'phonology.py'],
        'utils': ['__init__.py', 'validators.py', 'shortcuts.py'],
        'tests': ['__init__.py'],
        'tests/test_compiler': ['__init__.py', 'test_tokenizer.py', 'test_formative_parser.py'],
        'tests/test_grammar': ['__init__.py'],
        'tests/test_morphology': ['__init__.py', 'test_slots.py'],
    }

    # Create new directories and files
    for directory, files in new_structure.items():
        create_directory(directory)
        for file in files:
            create_file(os.path.join(directory, file))

    # Move existing files to their new locations
    moves = [
        ('compiler.py', 'compiler/ithkuil_compiler.py'),
        ('grammar/cases.py', 'grammar/cases.py'),
        ('grammar/word_types/formative.py', 'grammar/word_types/formative.py'),
        ('grammar/parsers/formative_parser.py', 'grammar/parsers/formative_parser.py'),
        ('lexicon/root.py', 'lexicon/root.py'),
        ('lexicon/affix.py', 'lexicon/affix.py'),
        ('lexicon/root_database.py', 'lexicon/root_database.py'),
        ('morphology/slots.py', 'morphology/slots.py'),
        ('morphology/affiliation.py', 'morphology/affiliation.py'),
        ('morphology/configuration.py', 'morphology/configuration.py'),
        ('utils/shortcuts.py', 'utils/shortcuts.py'),
    ]

    for src, dst in moves:
        move_file(src, dst)

    # Create main.py if it doesn't exist
    create_file('main.py')

    print("Project structure update completed!")

if __name__ == "__main__":
    restructure_project()