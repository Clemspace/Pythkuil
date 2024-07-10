import os
import ast

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
    with open(filepath, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=filepath)
        analyzer = CodeAnalyzer()
        analyzer.visit(tree)
        return analyzer.overview

def crawl_project(directory):
    project_overview = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                file_overview = analyze_file(filepath)
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
    project_directory = '.'  # Set your project directory
    overview = crawl_project(project_directory)
    print_overview(overview)
