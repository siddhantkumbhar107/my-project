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
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # This part uses the functions you already imported
    raw_content = file.read()
    metadata = extract_metadata(file)
    analysis = analyze_pdf(file)
    iocs = extract_iocs(raw_content)
    obj_count = get_object_count(file)
    risk_level, risk_reasons = calculate_risk(metadata, analysis, obj_count)

    return jsonify({
        "risk_level": risk_level,
        "risk_reasons": risk_reasons,
        "object_count": obj_count,
        "metadata": metadata
    })
if __name__ == "__main__":
     main()
