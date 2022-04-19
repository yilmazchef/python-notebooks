#!/usr/bin/env python


from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength
import os
import sys
import json
import time
import uuid
from folder_manager import notebook_file_paths
from docx_manager import to_docx, add_header, add_footer
from pptx_manager import 

if __name__ == "__main__":

    src_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    ipynb_file_list = notebook_file_paths(src_path, ".ipynb")

    pBarMax = len(ipynb_file_list)
    widgets = [Percentage(),
               ' ', Bar(),
               ' ', ETA(),
               ' ', AdaptiveETA()]
    pBar = ProgressBar(widgets=widgets, maxval=pBarMax)

    pBar.start()
    pBarCount = 0
    for ipynb_file in ipynb_file_list:

        md_file = ipynb_file.replace(".ipynb", ".md")
        docx_file = ipynb_file.replace(".ipynb", ".docx")
        pptx_file = ipynb_file.replace(".ipynb", ".pptx")

        to_md(ipynb_file, md_file)
        to_docx(md_file, docx_file)
        to_pptx(ipynb_file, pptx_file, os.path.join(
            os.getcwd(), "Temp", "IntecHeader.png"))

        pBarCount += 1
        pBar.update(pBarCount)

    pBar.finish()
