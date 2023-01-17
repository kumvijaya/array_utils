# File Utils

This repository keeps the util scripts to interact with files

## Update all the python source files
This [CLI utility/snippet](https://github.com/kumvijaya/file-utils/blob/main/append_to_py_source_files.py) can be used to update all the python files (*.py) in the repository by appending given content in the top.

This module takes below parameters.
- content -- content/source code to append. This will be appended in top (Example: 'import os;')

## Get all unit test files
This [CLI utility//snippet](https://github.com/kumvijaya/file-utils/blob/main/get_all_unit_test_files.py) can be used to all unit test python files (*.py) in the repository.

Refer more details 
- [glob](https://docs.python.org/3/library/glob.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [recursing files](https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/)