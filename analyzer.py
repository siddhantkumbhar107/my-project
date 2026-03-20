import re
from PyPDF2 import PdfReader

def analyze_pdf(filepath):
    try:
        result = {}

        reader = PdfReader(filepath)
        text = ""

        for page in reader.pages:
            try:
                text += page.extract_text() or ""
            except:
                pass

        keywords_list = [
            "/JavaScript", "/JS", "/OpenAction", "/Launch",
            "/EmbeddedFile", "/URI", "/SubmitForm"
        ]

        found_keywords = [kw for kw in keywords_list if kw in text]
        urls = re.findall(r'https?://\S+', text)

        result["file_name"] = filepath
        metadata_clean = {}

if reader.metadata:
    for key, value in reader.metadata.items():
        clean_key = key.replace("/", "")
        metadata_clean[clean_key] = str(value)

        result["metadata"] = metadata_clean

        result["keywords"] = found_keywords
        result["urls"] = urls
        result["risk"] = "Low Risk"
        result["mitigation"] = "Safe to open"

        return result

    except Exception as e:
        return {"error": str(e)}
