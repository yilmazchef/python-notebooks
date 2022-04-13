import pdfquery as pq
import pandas as pd
import os

path = os.getcwd()
pdf_path = path + "/hand/pdf/lidl.pdf"
print(pdf_path)

pdf_file = pq.PDFQuery(pdf_path)
pdf_file.load()
pdf_file.tree.write('pdfXML.txt', pretty_print=True)

