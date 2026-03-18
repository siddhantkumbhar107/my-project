import re
keywords = [
"/JavaScript",
"/JS",
"/OpenAction",
"/Launch",
"/EmbeddedFile"
]

def analyze_pdf(file):
    # Check if 'file' is a string (a path) or a file object (from Postman)
    if isinstance(file, str):
        with open(file, 'rb') as f:
            content = f.read().decode(errors="ignore")
    else:
        content = file.read().decode(errors="ignore")
        file.seek(0)
    
    suspicious = [key for key in keywords if key in content]
    return suspicious

def get_object_count(file):
    try:
        if isinstance(file, str):
            with open(file, 'rb') as f:
                content = f.read()
        else:
            content = file.read()
            file.seek(0)
        
        count = content.count(b' obj')
        return count
    except Exception as e:
        return f"Error: {e}"
def calculate_risk(metadata, analysis, obj_count):
    risk_reasons = []
    
    # Check if obj_count is a number before comparing
    if isinstance(obj_count, int):
        if obj_count > 50:
            risk_reasons.append(f"High object count: {obj_count}")
    else:
        # If it's an error string, we treat it as 0 or handle it
        obj_count = 0 

    if analysis:
        risk_reasons.append(f"Suspicious keywords found: {', '.join(analysis)}")

    risk_level = "High" if risk_reasons else "Low"
    return risk_level, risk_reasons
def extract_iocs(some_argument):
    # Your extraction logic goes here
    results = []
    # e.g., search for IPs, URLs, etc.
    return results