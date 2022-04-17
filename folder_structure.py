import os
import sys
import pathlib
from uuid import uuid4
import json
import fnmatch
import re
from urllib.parse import quote


def path_to_dict(root_path, language):

    # Get environment variables
    if os.getenv('GITHUB_USERNAME') is None:
        os.environ["GITHUB_USERNAME"] = str(input("Github username: "))

    if os.getenv('GITHUB_PYTHON_NOTEBOOKS_REPO') is None:
        os.environ["GITHUB_PYTHON_NOTEBOOKS_REPO"] = str(
            input("Github repository name: "))

    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME') if os.getenv(
        'GITHUB_USERNAME') is not None else str(input("Github username: "))
    GITHUB_REPO = os.getenv('GITHUB_PYTHON_NOTEBOOKS_REPO') if os.getenv(
        'GITHUB_PYTHON_NOTEBOOKS_REPO') is not None else str(input("Github repository name: "))

    includes = ['*.md', '*.docx']  # for files only
    excludes = ['.vscode', '.git', '*/__pycache__', '*/.ipynb_checkpoints',
                'Books', 'Codes', 'Presentations', 'Temp']  # for dirs and files

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
            "child": []
        }

        tree["child"].extend(
            [path_to_dict(os.path.join(root, d), language)
             for d in dirs if len(d) > 0]
        )

        tree["child"].extend(
            [{
                "name": os.path.basename(os.path.join(root, f)),
                "test": str(uuid4()),
                "icon": "<img src={`/icons/${getIconForFile('index.md')}`} alt=\"markdown\" className=\"icon\" />",
                "link": str(
                    "https://raw.githubusercontent.com/" +
                        str(GITHUB_USERNAME) + "/" + str(GITHUB_REPO) +
                    "/main/" + "Notebooks" + "/"
                    + language + "/" +
                        quote(os.path.basename(root)) +
                    "/" + quote(os.path.basename(f))
                ),
            } for f in files]
        )

        tree = {k: v for k, v in tree.items() if v}

        return tree


def notebook_file_paths(folder_path, file_type):
    paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(file_type.lower()):
                paths.append(os.path.join(root, file))

    return paths
