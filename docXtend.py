import os
from importlib.metadata import PackageNotFoundError
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_PARAGRAPH_ALIGNMENT


class DocXtend():
    
    def __init__(self, source:str, destination:str, **formats) -> None:
        self.source = source
        self.destination = destination
        self.formats = formats 
