import re
from PyPDF2 import PdfReader

def analyze_pdf(filepath):
    reader = PdfReader(filepath)
    text = ""

    # 📄 Extract text from PDF
    for page in reader.pages:
        try:
            text += page.extract_text() or ""
        except:
            pass

    # 🔍 Suspicious keywords
    keywords_list = [
        "/JavaScript", "/JS", "/OpenAction", "/Launch",
        "/EmbeddedFile", "/URI", "/SubmitForm"
    ]

    found_keywords = [kw for kw in keywords_list if kw in text]

    # 🌐 Extract URLs
    urls = re.findall(r'https?://\S+', text)

    # 🚨 Risk calculation
    if len(found_keywords) > 2 or len(urls) > 2:
        risk = "High Risk ⚠"
        mitigation = "Do NOT open this file. Scan with antivirus."
    elif found_keywords or urls:
        risk = "Medium Risk ⚠"
        mitigation = "Open carefully in sandbox environment."
    else:
        risk = "Low Risk ✅"
        mitigation = "File appears safe."

    # 📊 Final result
    return {
        "file": filepath,
        "keyword_count": len(found_keywords),
        "keywords": found_keywords,
        "url_count": len(urls),
        "urls": urls,
        "risk": risk,
        "mitigation": mitigation
    }
