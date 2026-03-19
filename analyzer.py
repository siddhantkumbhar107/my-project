import re
from PyPDF2 import PdfReader

def analyze_pdf(filepath):
    result = {}

    
    result["file_name"] = filepath

    
    try:
        reader = PdfReader(filepath)
        meta = reader.metadata
        result["metadata"] = str(meta)
    except:
        result["metadata"] = "Could not extract metadata"

    
    text = ""
    try:
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        pass

    
    keywords = ["JavaScript", "/JS", "/OpenAction", "/AA", "/URI"]
    found_keywords = [k for k in keywords if k.lower() in text.lower()]
    result["keywords"] = found_keywords if found_keywords else ["None"]

    
    urls = re.findall(r'https?://\S+', text)
    result["urls"] = urls if urls else ["None"]

    
    if found_keywords or urls:
        result["risk"] = "High Risk ⚠"
    else:
        result["risk"] = "Low Risk ✅"

    
    result["solution"] = "Do not open suspicious PDFs. Use antivirus and sandbox tools."

    return result
