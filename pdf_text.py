#pip install pdfplumber
import pdfplumber as pdftool

def retrieve_text(file_path):
    with pdftool.open(file_path) as tool:
        for page_number, page in enumerate(tool.pages, 1):
            print()
            print("------- PAGE NUMBER: ", page_number, " ------- ")
            print()
            data = page.extract_text()
            print(data)
        print()
        print("-------  All pages printed ------- ")

retrieve_text("PDF_text/samplePDF.pdf")