import os
import sys
import pathlib
from uuid import uuid4
import json
import fnmatch
import re

def path_to_dict(root_path):
    
    includes = ['*.md', '*.ipynb'] # for files only
    excludes = ['.vscode', '.git', '__pycache__', 'Books', 'Code', 'Presentations'] # for dirs and files

    # transform glob patterns to regular expressions
    includes = r'|'.join([fnmatch.translate(x) for x in includes])
    excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'
    
    for root, dirs, files in os.walk(root_path, topdown=True):
        
          # exclude dirs
        dirs[:] = [os.path.join(root, d) for d in dirs]
        dirs[:] = [d for d in dirs if not re.match(excludes, d)]

        # exclude/include files
        files = [os.path.join(root, f) for f in files]
        files = [f for f in files if not re.match(excludes, f)]
        files = [f for f in files if re.match(includes, f)]
        
        tree = {
            "name": os.path.basename(root),
            "test": str(uuid4()),
            "icon": "folder",
            "type": "folder",
            "child": []
        }

        tree["child"].extend(
            [path_to_dict(os.path.join(root, d)) for d in dirs]
        )
        
        tree["child"].extend(
            [{
                "name": os.path.basename(os.path.join(root, f)),
                "test": str(uuid4()),
                "icon": pathlib.Path(os.path.join(root, f)).suffix,
                "link": os.path.join(root, f),
                "type": "file"
            } for f in files]
        )

        return tree
    
def path_to_json_file(root_path, dict_path): 
    with open(root_path, 'w') as file:
        json_string = json.dumps(dict_path, default=lambda o: o.__dict__, sort_keys=True, indent=2)
        file.write(json_string)


def notebook_file_paths(folder_path, file_type):
    paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(file_type.lower()):
                paths.append(os.path.join(root, file))

    return paths

