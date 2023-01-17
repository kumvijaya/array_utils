"""This is the python module used to append given source content to all python source files in current repo recursively.

This module takes below parameters.
content -- source code to append. This will be appended in top (Example: 'import sys;sys.path.insert(0, 'dist-packages')')
"""

import argparse
import os
import logging
import glob
import pathlib
import json

parser = argparse.ArgumentParser(
    description='Appends given source content to python source files recursively'
)
parser.add_argument(
    '-c',
    '--content',
    required=True,
    help='source code to append e.g. import sys')

args = parser.parse_args()
append_content = args.content

logging.getLogger("AppendPySource").setLevel(logging.ERROR)

def read_file_info(filename):
    """Reads the py file and returns the lines and start indes to append.
    Return the read file info as map (Example: {"content_present": true, "lines": [..], "start_index": 1}).
    """
    file_info = {}
    start_index = 0
    lines = []
    content_present = False
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            check_line = line.strip()
            if check_line == '' or check_line.startswith('#'):
                start_index = start_index + 1
                continue
            else:
                content_present = True
                break
    file_info['filename'] = filename
    file_info['content_present'] = content_present
    file_info['lines'] = lines
    file_info['start_index'] = start_index
    return file_info

def insert_content(file_info, content):
    """inserts given content to file.
    """
    lines = file_info['lines']
    if lines:
        lines.insert(file_info['start_index'], content)
        write_file(file_info['filename'], lines)

def write_file(filename, lines):
    """Writes the lines to file.
    """
    with open(filename, 'w') as file:
        file.writelines(lines)

def to_be_included(filename, path):
    """Checks whether the given file to be included for source py file update.
    """
    return (not any(x in filename for x in ['/node_modules/', '/dist-packages/', '/dist/', '/__pycache__/', '/setup.py'])) and path.suffix == '.py'

def append_to_py_files(append_content):
    """Appends the given content to all py source files.
    """
    root_dir = os.getcwd()
    files_updated = []
    for filename in glob.iglob(root_dir + '**/**', recursive=True):
        path = pathlib.Path(filename)
        if to_be_included(filename, path):
            file_info = read_file_info(filename)
            if file_info['content_present']:
                insert_content(file_info, append_content + '\n')
                files_updated.append(filename)
    return files_updated

files_updated = append_to_py_files(append_content)
print(json.dumps(files_updated))

