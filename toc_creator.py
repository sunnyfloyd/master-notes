import os
import sys
import pyperclip

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def list_files(base_dir=BASE_DIR):
    toc = ''
    for root, _, files in os.walk(base_dir):
        if 'venv' in root or not has_md_file(root):
            continue
        level = root.replace(base_dir, '').count(os.sep)
        indent = f"{' ' * 2 * level}- "
        toc += f'{indent}[{os.path.basename(root)}](\{os.path.relpath(root)})\n'
        subindent = f"{' ' * 2 * (level + 1)}- "
        for file in files:
            if file.endswith('.md'):
                toc += f'{subindent}[{file}](\{os.path.relpath(root)}\{file})\n'
    pyperclip.copy(toc)

def has_md_file(branch):
    return any(
        any(file.endswith('.md') for file in files) for *_, files in os.walk(branch)
    )

if __name__ == '__main__':
    try:
        base_dir = sys.argv[1]
    except IndexError:
        base_dir = BASE_DIR
    
    list_files(base_dir)
