keywords = ["/JS", "/JavaScript", "/AA", "/OpenAction", "/AcroForm", "/RichMedia", "/Launch", "/EmbeddedFile"]
from flask import Flask, request, jsonify
import os
import sys
from analyzer import analyze_pdf,get_object_count,calculate_risk,extract_iocs
from metadata import extract_metadata
from ioc_extractor import extract_iocs
from report_generator import generate_report
app = Flask(__name__)

@app.route('/')
def home():
    return "PDF Malware Analysis API is running!"
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py file.pdf")
        return

    file = sys.argv[1]
    print("\n[+] Starting PDF Malware Analysis\n")
    with open(file, 'rb') as f:
        raw_content = f.read()
    metadata = extract_metadata(file)
    iocs = extract_iocs(file)
    analysis = analyze_pdf(file)
    obj_count = get_object_count(file)
    risk_level, risk_reasons = calculate_risk(metadata, analysis, obj_count)
    ips = extract_iocs(raw_content)
    generate_report(file, metadata, analysis, iocs, obj_count, risk_level, risk_reasons)

def analyze_pdf(file):
    # Check if 'file' is a string (a path on your computer)
    if isinstance(file, str):
        with open(file, 'rb') as f:
            content = f.read().decode(errors="ignore")
    else:
        # If it's a web upload from Postman, it's already an object
        content = file.read().decode(errors="ignore")
        file.seek(0) # Reset the pointer for other functions
    
    suspicious = [key for key in keywords if key in content]
    return suspicious

def get_object_count(file):
    try:
        # Read the raw bytes directly
        content = file.read()
        file.seek(0)  # Move back to the start again
        count = content.count(b' obj')
        return count
    except Exception as e:
        return f"Error: {e}"
if __name__ == "__main__":
   main()
