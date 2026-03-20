import re
from PyPDF2 import PdfReader
from analyzer import analyze_pdf
import json
def handler(request):

    # 📄 File name
    result["file_name"] = filepath

    # 📊 Metadata
    try:
        reader = PdfReader(filepath)
        meta = reader.metadata
        result["metadata"] = str(meta)
    except:
        result["metadata"] = "Could not extract metadata"

    # 📝 Extract text
    text = ""
    try:
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        pass

    # 🔍 Suspicious keywords
    keywords = [
        "/JavaScript", "/JS", "/OpenAction", "/Launch",
        "/EmbeddedFile", "/URI", "/SubmitForm"
    ]

    found_keywords = [k for k in keywords if k.lower() in text.lower()]

    # 🌐 Extract URLs
    urls = re.findall(r'https?://\S+', text)

    # ⚠️ Risk calculation
    if len(found_keywords) > 2 or len(urls) > 2:
        risk = "High Risk ⚠️"
        mitigation = "Do NOT open this file. Scan with antivirus."
    elif found_keywords or urls:
        risk = "Medium Risk ⚠️"
        mitigation = "Open carefully in sandbox environment."
    else:
        risk = "Low Risk ✅"
        mitigation = "File appears safe for normal use."

    # 📦 Final result
    result["keyword_count"] = len(found_keywords)
    result["keywords"] = found_keywords

    result["url_count"] = len(urls)
    result["urls"] = urls

    result["risk"] = risk
    result["mitigation"] = mitigation
   return {
 def analyze_pdf(filepath):
     result = {}

    result["file_name"] = filepath
    result["metadata"] = "Sample metadata"
    result["keywords"] = []
    result["urls"] = []
    result["risk"] = "Low Risk"
    result["mitigation"] = "Safe to open"

    
}
    return result
