import re
keywords = [
"/JavaScript",
"/JS",
"/OpenAction",
"/Launch",
"/EmbeddedFile"
]

def analyze_pdf(file):

    with open(file,"rb") as f:
        content = f.read().decode(errors="ignore")

    suspicious = []

    for key in keywords:
        if key in content:
            suspicious.append(key)

    return suspicious
def get_object_count(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            count = content.count(b' obj') 
            return count
    except Exception as e:
        return f"Error: {e}"
def calculate_risk(metadata, analysis, obj_count):
    score = 0
    reasons = []

    # Check Step 3: Suspicious Keywords
    if any(kw in analysis for kw in ["/JavaScript", "/JS", "/OpenAction"]):
        score += 5
        reasons.append("Contains executable scripts (JS/OpenAction)")

    # Check Step 4: Encoded Streams
    if obj_count > 50: # High complexity can be suspicious
        score += 2
        reasons.append("High object count (Complex structure)")

    # Determine Level
    if score >= 5:
        return "HIGH RISK", reasons
    elif score >= 2:
        return "MEDIUM RISK", reasons
    else:
        return "LOW RISK (Safe)", ["No major threats found"]
def extract_iocs(some_argument):
    # Your extraction logic goes here
    results = []
    # e.g., search for IPs, URLs, etc.
    return results