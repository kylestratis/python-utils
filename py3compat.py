import ast
import os
from os.path import isfile, join

"""
Quick and dirty script to get Python 3 compatibility status for files in a directory.
Code from this discussion: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
"""

def test_source_code_compatible(code_data):
    try:
        return ast.parse(code_data)
    except SyntaxError as exc:
        return False

files = [f for f in os.listdir(".") if isfile(join(".", f))]

for file_name in files:
    ast_tree = test_source_code_compatible(open(file_name).read())
    if not ast_tree:
        print(f"File {file_name} couldn't get loaded")
    else:
        print(f"File {file_name} is Python 3 compatible")
