import os
import sys
from uuid import uuid4
import json
import fnmatch
import re
import time
from urllib.parse import quote


def hierarchy_json(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x))
                         for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


def filter_files(folder_path: str, file_type: str) -> list:
    paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(file_type.lower()):
                paths.append(os.path.join(root, file))

    return paths
