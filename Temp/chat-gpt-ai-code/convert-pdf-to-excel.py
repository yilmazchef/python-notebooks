import pypdf2
from openpyxl import Workbook

# Open the PDF file in read-only mode
with open('file.pdf', 'rb') as file:
    # Create a PDF object
    pdf = pypdf2.PdfFileReader(file)
    
    # Create a new Excel workbook
    workbook = Workbook()
    # Create a new sheet
    sheet = workbook.active
    
    # Iterate through all the pages in the PDF
    for page in range(pdf.getNumPages()):
        # Get the current page
        current_page = pdf.getPage(page)
        # Extract the text from the page
        text = current_page.extractText()
        # Split the text into rows
        rows = text.split('\n')
        # Iterate through the rows
        for row_index, row in enumerate(rows):
            # Split the row into cells
            cells = row.split(' ')
            # Iterate through the cells
            for cell_index, cell in enumerate(cells):
                # Write the cell value to the sheet
                sheet.cell(row=row_index+1, column=cell_index+1).value = cell
    
    # Save the Excel file
    workbook.save('file.xlsx')
