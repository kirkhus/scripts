import os
import re
import sys

def isfile(x):
    return True

def get_files(root, pattern=".*", tests=[isfile], **kwargs):
    """getFiles(root, pattern=".*", tests=[isfile], **kwargs) -> list of files

    Return a list of files in the specified path (root)
    applying the predicates listed in tests returning
    only the files that match the pattern. Some optional
    kwargs can be specified:

    * full=True        (Return full paths)
    * recursive=True   (Recursive mode)
    """

    def test(file, tests):
        for test in tests:
            if not test(file):
                return False
        return True

    full = kwargs.get("full", True)
    recursive = kwargs.get("recursive", True)

    files = []

    for file in os.listdir(root):
        path = os.path.abspath(os.path.join(root, file))
        if os.path.isdir(path):
            if recursive:
                files.extend(get_files(path, pattern, **kwargs))
        else:
            if full:
                files.append(path)
            else:
                files.append(file)

    return files
