import os


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return(paths)


ipynb_file_list = list_files(os.getcwd(), ".ipynb")

for ipynb_file in ipynb_file_list:
    md_file = ipynb_file.replace(".ipynb", ".md")
    print("#" * 100)
    print(f"{ipynb_file} to {md_file} conversion started...")
    os.system(f"jupyter nbconvert --to markdown {ipynb_file}")
    print(f"{ipynb_file} to {md_file} conversion complete...")
    print("#" * 100)
