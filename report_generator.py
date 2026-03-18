def generate_report(file, metadata, analysis, iocs , obj_count, risk_level, risk_reasons):
    print("\n" + "="*40)
    print("      PDF MALWARE ANALYSIS REPORT")
    print("="*40)
    
    print(f"\n[+] Target File: {file}")

    # 1. Metadata Section
    print("\n[i] Metadata Information:")
    if metadata:
        for key, value in metadata.items():
            # Cleans the '/' prefix from PDF metadata keys
            clean_key = key.replace('/', '')
            print(f"    - {clean_key}: {value}")
    else:
        print("    None found.")

    # 2. Suspicious Keywords (Analysis)
    print("\n[!] Suspicious Keywords Found:")
    if analysis:
        for item in analysis:
            print(f"    - {item}")
    else:
        print("    None found.")

    # 3. Indicators of Compromise (IOCs)
    print("\n[!] Network Indicators (URLs):")
    if iocs and iocs.get('urls'):
        for url in iocs['urls']:
            print(f"    - {url}")
    else:
        print("    None found.")

    print("\n" + "="*30)
    print(f"FINAL RISK ASSESSMENT: {risk_level}")
    print("="*30)
    for reason in risk_reasons:
     print(f"- {reason}")
    print("="*30)

    print("\n--- STEP 7: MITIGATION STRATEGY ---")
    if risk_level == "HIGH RISK":
        print("ACTION: Do not open this file. Quarantining is recommended.")
    elif risk_level == "MEDIUM RISK":
        print("ACTION: Proceed with caution. Inspect URLs before clicking.")
    else:
        print("ACTION: File appears safe for normal use.")
    print("="*30)