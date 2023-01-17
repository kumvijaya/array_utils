"""This is the python module used to py test files recursively.
"""
import os
import logging
import glob
import pathlib
import json

logging.getLogger("UnitTestPyFiles").setLevel(logging.ERROR)

def is_unit_test_file(filename, path):
    """Checks whether the given file is unit test file.
    """
    return (not any(x in filename for x in ['/.git/', '/.github/','/deploy/','/node_modules/','/dist-packages/'])) and path.suffix == '.py' and (path.stem.startswith('test_') or path.stem.endswith('_test'))

def get_unit_test_py_files():
    """gets the unit test files.
    """
    root_dir = os.getcwd()
    test_files = []
    for filename in glob.iglob(root_dir + '**/**', recursive=True):
        path = pathlib.Path(filename)
        if is_unit_test_file(filename, path):
            test_files.append(filename)
    return test_files

files = get_unit_test_py_files()
print(json.dumps(files))