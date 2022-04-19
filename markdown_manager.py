import os


def to_md(ipynb_file):
    cmdlet = f"jupyter nbconvert --to markdown \"{ipynb_file}\""
    os.system(cmdlet)
