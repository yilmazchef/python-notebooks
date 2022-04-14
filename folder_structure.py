import os
import sys
from uuid import uuid4
import json

def path_to_dict(root_path):
    for root, dirs, files in os.walk(root_path, topdown=True):
        tree = {
            "id": str(uuid4()),
            "name": root,
            "icon": "folder",
            "type": "folder",
            "children": []
        }

        tree["children"].extend(
            [path_to_dict(os.path.join(root, d)) for d in dirs]
        )

        tree["children"].extend(
            [{
                "id": str(uuid4()),
                "name": os.path.join(root, f),
                "icon": ".py",
                "link": "some_link_here",
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


def mock():
    return [
        {
            "name": 'Python',
            "test": 'parent1',
            "icon": "filename.py",
            "child": [
                {
                    "name": 'Module1',
                    "test": 'py_child1',
                    "child": [
                        {
                            "name": 'leaf',
                            "test": 'py_childofpy_child1',
                            "link": "linkgelecekburaya",
                        }
                    ],
                },
                {
                    "name": 'Module 2',
                    "test": 'py_child2',
                    "child": [
                        {
                            "test": 'py_childofpy_child2',
                            "name": 'asdasd',
                            "link": "linkgelecekburaya",
                        },
                    ],
                },
                {
                    "name": 'Module 3',
                    "test": 'py_child3',
                    "child": [
                        {
                            "test": 'py_childofpy_child3',
                            "name": 'asdasd',
                            "link": "linkgelecekburaya",
                        },
                    ],
                },
                {
                    "name": 'Module 4',
                    "test": 'py_child4',
                    "child": [
                        {
                            "test": 'py_childofpy_child4',
                            "name": 'asdasd',
                            "link": "linkgelecekburaya",
                        },
                    ],
                },
                {
                    "name": 'Module 5',
                    "test": 'py_child5',
                    "child": [
                        {
                            "test": 'py_childofpy_child5',
                            "name": 'asdasd',
                            "link": "linkgelecekburaya",
                        },
                    ],
                },

            ],
        },
    ]
