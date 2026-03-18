from PyPDF2 import PdfReader

def extract_metadata(file):

    reader = PdfReader(file)

    meta = reader.metadata

    return meta