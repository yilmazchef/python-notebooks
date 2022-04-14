#!/usr/bin/env python


import os
import sys
import json


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))

    print(paths)

    return(paths)


def to_py(ipynb_file):
    py_file = ipynb_file.replace(".ipynb", ".py")
    print(f"\"{ipynb_file}\" to \"{py_file}\" conversion started...")
    code = json.load(open(ipynb_file))
    for cell in code['cells']:
        if cell['cell_type'] == 'code':
            print('# -------- code --------')
            for line in cell['source']:
                print(line, end='')
            print('\n')
        elif cell['cell_type'] == 'markdown':
            print('# -------- markdown --------')
            for line in cell['source']:
                print("#", line, end='')
            print('\n')
    print(f"\"{ipynb_file}\" to {py_file} conversion complete...")


def to_md(ipynb_file, md_file):
    print(f"\"{ipynb_file}\" to \"{md_file}\" conversion started...")
    cmdlet = f"jupyter nbconvert --to markdown \"{ipynb_file}\""
    print(cmdlet)
    os.system(cmdlet)
    print(f"\"{ipynb_file}\" to \"{md_file}\" conversion complete...")


def to_docx(md_file, docx_file):
    print(f"\"{md_file}\" to \"{docx_file}\" conversion started...")
    cmdlet = f"pandoc \"{md_file}\" -f markdown -o \"{docx_file}\""
    print(cmdlet)
    os.system(cmdlet)
    print(f"\"{md_file}\" to \"{docx_file}\" conversion complete...")


def to_odt(md_file, odt_file):
    print(f"{md_file} to \"{odt_file}\" conversion started...")
    cmdlet = f"pandoc -t odt \"{md_file}\" -o \"{odt_file}\""
    print(cmdlet)
    os.system(cmdlet)
    print(f"\"{md_file}\" to \"{odt_file}\" conversion complete...")


ipynb_file_list = list_files(os.getcwd(), ".ipynb")

for ipynb_file in ipynb_file_list:
    md_file = ipynb_file.replace(".ipynb", ".md")
    # docx_file = ipynb_file.replace(".ipynb", ".docx")
    # odt_file = ipynb_file.replace(".ipynb", ".odt")

    print("#" * 255)

    to_md(ipynb_file, md_file)
    # to_docx(md_file, docx_file)

    print("#" * 255)


print("#" * 255)
print("#" * 80, end="")
print("THE CONVERSION IS COMPLETED..", end="")
print("#" * 80, end="\n")
