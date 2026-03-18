import sys
from analyzer import analyze_pdf,get_object_count,calculate_risk,extract_iocs
from metadata import extract_metadata
from ioc_extractor import extract_iocs
from report_generator import generate_report

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

if __name__ == "__main__":
     main()