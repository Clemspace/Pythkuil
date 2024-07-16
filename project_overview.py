import os
import ast
import chardet

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.overview = {}

    def visit_ClassDef(self, node):
        self.overview[node.name] = {
            'type': 'class',
            'methods': [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
        }
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.overview[node.name] = {
            'type': 'function',
            'args': [a.arg for a in node.args.args]
        }
        self.generic_visit(node)

def analyze_file(filepath):
    try:
        with open(filepath, 'rb') as file:
            raw_data = file.read()
        
        # Detect the file encoding
        result = chardet.detect(raw_data)
        encoding = result['encoding']

        # Use utf-8 as fallback if no encoding is detected
        if encoding is None:
            encoding = 'utf-8'

        # Decode the file content using the detected encoding
        file_content = raw_data.decode(encoding)

        tree = ast.parse(file_content, filename=filepath)
        analyzer = CodeAnalyzer()
        analyzer.visit(tree)
        return analyzer.overview
    except Exception as e:
        print(f"Error analyzing file {filepath}: {str(e)}")
        return {}

def crawl_project(directory):
    project_overview = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                file_overview = analyze_file(filepath)
                if file_overview:  # Only add if analysis was successful
                    project_overview[filepath] = file_overview
    return project_overview

def print_overview(overview):
    for filepath, content in overview.items():
        print(f"\nFile: {filepath}")
        for name, details in content.items():
            if details['type'] == 'class':
                print(f"  Class: {name}")
                for method in details['methods']:
                    print(f"    Method: {method}")
            elif details['type'] == 'function':
                print(f"  Function: {name} (Args: {', '.join(details['args'])})")

if __name__ == "__main__":
    # Set your project directory explicitly
    project_directory = r'C:\Users\Clemspace\Mistral\Pythkuil'
    
    # Ensure we're in the correct directory
    os.chdir(project_directory)
    
    overview = crawl_project(project_directory)
    print_overview(overview)