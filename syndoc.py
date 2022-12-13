import os
import sys
import time
import watchdog.events
import watchdog.observers

import configparser
import json

from uuid import uuid4
from urllib.parse import quote

import collections.abc
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength


def get_notebook_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Notebooks"))

def get_markdown_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Markdowns"))

def get_html_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Website"))

def get_docx_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Documents"))

def get_pptx_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Presentations"))

def get_pdf_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "EBooks"))

def dir2file(path):
    json_file = os.path.join(path, "index.json")

    with open(json_file, "w") as f:
        json.dump(dir2json(path), f, indent=4)

    return json_file


def only4md(folder_path: str) -> list:
    paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".md"):
                paths.append(os.path.join(root, file))

    return paths


def only4ipynb(folder_path: str) -> list:
    paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".ipynb"):
                paths.append(os.path.join(root, file))

    return paths


def md2html(md_file: str) -> str:

    html_file = md_file.replace(".md", ".html")
    cmdlet = f"pandoc -o \"{html_file}\" \"{md_file}\""
    os.system(cmdlet)
    return html_file


def img2base64(image_file, output_file):

    # need base 64
    import base64
    import sys
    # open the image
    image = open(image_file, 'rb')
    # read it
    image_read = image.read()
    # encode it as base 64
    # after python>=3.9, use `encodebytes` instead of `encodestring`
    image_64_encode = base64.encodestring(image_read) if sys.version_info < (
        3, 9) else base64.encodebytes(image_read)
    # convert the image base 64 to a string
    image_string = str(image_64_encode)
    # replace the newline characters
    image_string = image_string.replace("\\n", "")
    # replace the initial binary
    image_string = image_string.replace("b'", "")
    # replace the final question mark
    image_string = image_string.replace("'", "")
    # add the image tags
    image_string = '<p><img src="data:image/png;base64,' + image_string + '"></p>'
    # write it out
    image_result = open(output_file, 'w')
    image_result.write(image_string)


def ipynb2md(ipynb_file: str) -> str:
    cmdlet = f"jupyter nbconvert --to markdown \"{ipynb_file}\""
    os.system(cmdlet)
    return ipynb_file.replace(".ipynb", ".md")


def md2ipynb(md_file: str) -> str:

    ipynb_file = md_file.replace(".md", ".ipynb")
    cmdlet = f"pandoc \"{md_file}\" -o \"{ipynb_file}\""
    os.system(cmdlet)
    return ipynb_file


def md2odt(md_file):
    odt_file = md_file.replace(".md", "odt")
    cmdlet = f"pandoc -t odt \"{md_file}\" -o \"{odt_file}\""
    os.system(cmdlet)


def md2pptx(md_file: str) -> str:

    c = collections
    c.abc = collections.abc

    pptx_path = md_file.replace(".md", ".pptx")
    cmdlet = f"pandoc -V fontsize=12pt \"{md_file}\" -s --wrap auto -o \"{pptx_path}\""
    os.system(cmdlet)

    return pptx_path


def md2docx(md_file: str) -> str:

    docx_file = md_file.replace(".md", ".docx")
    cmdlet = f"pandoc \"{md_file}\" -f markdown -o \"{docx_file}\""
    os.system(cmdlet)
    return docx_file


def img4docx(fileref, question, tpl, width=None):

    if fileref.__class__.__name__ in ('DAFile', 'DAFileList', 'DAFileCollection', 'DALocalFile', 'DAStaticFile'):
        file_info = dict(fullpath=fileref.path())
    else:
        file_info = server.file_finder(fileref, question=question)
    if 'path' in file_info and 'extension' in file_info:
        docassemble.base.filter.convert_svg_to_png(file_info)
    if 'fullpath' not in file_info:
        return '[FILE NOT FOUND]'
    if width is not None:
        m = re.search(r'^([0-9\.]+) *([A-Za-z]*)', str(width))
        if m:
            amount = float(m.group(1))
            units = m.group(2).lower()
            if units in ['in', 'inches', 'inch']:
                the_width = Inches(amount)
            elif units in ['pt', 'pts', 'point', 'points']:
                the_width = Pt(amount)
            elif units in ['mm', 'millimeter', 'millimeters']:
                the_width = Mm(amount)
            elif units in ['cm', 'centimeter', 'centimeters']:
                the_width = Cm(amount)
            elif units in ['twp', 'twip', 'twips']:
                the_width = Twips(amount)
            else:
                the_width = Pt(amount)
        else:
            the_width = Inches(2)
    else:
        the_width = Inches(2)
    return InlineImage(tpl, file_info['fullpath'], the_width)


def h4docx(docx_file, header_image, header_text=None):

    document = None

    # checking if file already present and creating it if not present
    if os.path.isfile(rf"{docx_file}"):

        # opening the existing document
        document = Document(docx_file)

        header = document.sections[0].header

        htable = header.add_table(1, 2, Inches(4))
        htab_cells = htable.rows[0].cells
        ht0 = htab_cells[0].add_paragraph()
        kh = ht0.add_run()
        kh.add_picture(header_image, width=Inches(3))

        if header_text is not None:
            ht1 = htab_cells[1].add_paragraph(header_text)
            ht1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            # font size of header text
            ht1.style.font.size = Pt(10)

            # saving the blank document
        document.save(docx_file)


def f4docx(docx_file, footer_image, footer_text=None):

    document = None

    # checking if file already present and creating it if not present
    if os.path.isfile(rf"{docx_file}"):

        # opening the existing document
        document = Document(docx_file)

        footer = document.sections[0].footer

        ftable = footer.add_table(1, 2, Inches(4))
        ftab_cells = ftable.rows[0].cells
        ft0 = ftab_cells[0].add_paragraph()
        fh = ft0.add_run()

        imgSize = Inches(4)

        if footer_text is not None:
            imgSize = Inches(4.5)
            ft1 = ftab_cells[1].add_paragraph(footer_text)
            ft1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            ft1.style.font.size = Pt(10)

        fh.add_picture(footer_image, width=imgSize)

        document.save(docx_file)


def md2pdf(md_file: str) -> str:

    pdf_file = md_file.replace(".md", ".pdf")
    cmdlet = f"pandoc \"{md_file}\" -o \"{pdf_file}\""
    os.system(cmdlet)
    return pdf_file


def md2epub(md_file: str) -> str:

    epub_file = md_file.replace(".md", ".epub")
    cmdlet = f"pandoc \"{md_file}\" -o \"{epub_file}\""
    os.system(cmdlet)
    return epub_file


def update_all():

    src_path = input(
        "Source folder: "
    )

    if src_path == "":
        src = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    notebook_file_list = only4ipynb(src_path)

    for notebook_file in notebook_file_list:
        md_file = ipynb2md(notebook_file)

    source_file_list = only4md(src_path)

    pBarMax = len(source_file_list)
    widgets = [Percentage(),
               ' ', Bar(),
               ' ', ETA(),
               ' ', AdaptiveETA()]
    pBar = ProgressBar(widgets=widgets, maxval=pBarMax)

    pBar.start()
    pBarCount = 0

    for source_file in source_file_list:

        docx_file = md2docx(source_file)
        h4docx(docx_file, os.path.join(os.getcwd(), "Templates", "header.png"), open(
            os.path.join(os.getcwd(), "templates", "header.txt"), 'r'))
        f4docx(docx_file, os.path.join(os.getcwd(), "Templates", "footer.png"), open(
            os.path.join(os.getcwd(), "templates", "footer.txt"), 'r'))

        pptx_file = md2pptx(source_file)

        pdf_file = md2pdf(source_file)

        pBarCount += 1
        pBar.update(pBarCount)

    pBar.finish()


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.ipynb'],
                                                             ignore_directories=True, case_sensitive=False)
        print(sys.getdefaultencoding())

    def on_created(self, event):
        print(f"{event.src_path} is created.")
        # Event is created, you can process it now

    def on_modified(self, event):
        print(f"{event.src_path} is modified.")
        # Event is modified, you can process it now

        md_file = ipynb2md(event.src_path)

        docx_file = md2docx(md_file)
        h4docx(docx_file, os.path.join(os.getcwd(), "Templates", "header.png"), open(
            os.path.join(os.getcwd(), "templates", "header.txt"), 'r'))
        f4docx(docx_file, os.path.join(os.getcwd(), "Templates", "footer.png"), open(
            os.path.join(os.getcwd(), "templates", "footer.txt"), 'r'))

        pptx_file = md2pptx(md_file)
        pdf_file = md2pdf(md_file)

    def on_deleted(self, event):

        print(f"{event.src_path} is deleted.")
        # Event is deleted, you can process it now

        md_file = event.src_path.replace(".ipynb", ".md")
        os.remove(md_file)
        os.remove(md_file.replace(".md", ".docx"))
        os.remove(md_file.replace(".md", ".pptx"))
        os.remove(md_file.replace(".md", ".pdf"))


if __name__ == "__main__":
    
    # ask user if they want to update all files in the folder
    
    update_all_manually = input("Update all files in the folder? (y/n): ")
    
    if update_all_manually == "y":
        update_all()
        
    # ask user if they want to watch the folder for changes

    watch_folder = input("Watch folder for changes? (y/n): ")
     
    if watch_folder == "y":
        src_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
        event_handler = Handler()
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, path=src_path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
