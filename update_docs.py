#!/usr/bin/env python


import os
import sys
import json
import time
import uuid


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
    print(f"\"{ipynb_file}\" to \"{py_file}\" conversion complete...")


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


def to_json(md_file, json_file):
    pass


def to_pdf(md_file, pdf_file):
    print(f"{md_file} to \"{pdf_file}\" conversion started...")
    cmdlet = f"pandoc -t odt \"{md_file}\" -o \"{pdf_file}\""
    print(cmdlet)
    os.system(cmdlet)
    print(f"\"{md_file}\" to \"{pdf_file}\" conversion complete...")


if __name__ == "__main__":

    src_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    ipynb_file_list = notebook_file_paths(src_path, ".ipynb")

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
