import re
from PyPDF2 import PdfReader

def analyze_pdf(filepath):
    result = {}

    reader = PdfReader(filepath)
    text = ""

    # Extract text
    for page in reader.pages:
        try:
            text += page.extract_text() or ""
        except:
            pass

    # Suspicious keywords
    keywords_list = [
        "/JavaScript", "/JS", "/OpenAction", "/Launch",
        "/EmbeddedFile", "/URI", "/SubmitForm"
    ]

    found_keywords = [kw for kw in keywords_list if kw in text]

    # Extract URLs
    urls = re.findall(r'https?://\S+', text)

    # Risk calculation
    if len(found_keywords) > 2 or len(urls) > 2:
        risk = "High Risk"
        mitigation = "Do NOT open this file."
    elif found_keywords or urls:
        risk = "Medium Risk"
        mitigation = "Open carefully."
    else:
        risk = "Low Risk"
        mitigation = "Safe to open."

    result["file_name"] = filepath
    result["metadata"] = str(reader.metadata)
    result["keywords"] = found_keywords
    result["urls"] = urls
    result["risk"] = risk
    result["mitigation"] = mitigation

    return result
