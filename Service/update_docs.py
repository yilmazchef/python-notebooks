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
from folder_manager import filter_files
from docx_manager import to_docx, add_header, add_footer
from pptx_manager import to_pptx
import pypandoc

if __name__ == "__main__":

    src_path = input(
        "Please paste here the absolute path of the root folder: "
    )

    if src_path == "":
        src = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    source_file_list = filter_files(src_path, ".md")

    pBarMax = len(source_file_list)
    widgets = [Percentage(),
               ' ', Bar(),
               ' ', ETA(),
               ' ', AdaptiveETA()]
    pBar = ProgressBar(widgets=widgets, maxval=pBarMax)

    pBar.start()
    pBarCount = 0
    for source_file in source_file_list:

        docx_path = source_file.replace(".md", ".docx")
        docx_file = pypandoc.convert_file(source_file, 'docx', outputfile=docx_path)
        print(f"DOCX -> {docx_path}")
        # docx_file = to_docx(source_file)
        
        header_image = os.getcwd() + os.path.sep + "Service" + os.path.sep + "header.png"
        header_text = open(os.getcwd() + os.path.sep + "Service" + os.path.sep + "header.txt", "r")
        add_header(docx_path, header_image, header_text)

        footer_image = os.getcwd() + os.path.sep + "Service" + os.path.sep + "footer.png"
        footer_text = open(os.getcwd() + os.path.sep + "Service" + os.path.sep + "footer.txt", "r")
        add_footer(docx_path, footer_image, footer_text)
        
        pptx_path = outputfile=source_file.replace(".md", ".pptx")
        pptx_file = to_pptx(source_file)
        print(f"PPTX -> {pptx_path}")
        
        pdf_path = outputfile=source_file.replace(".md", ".pdf")
        pdf_file = pypandoc.convert_file(source_file, 'pdf', outputfile=pdf_path, extra_args=['-V', 'geometry:margin=1.5cm'])
        print(f"PDF -> {pdf_path}")
        
        pBarCount += 1
        pBar.update(pBarCount)

    pBar.finish()

