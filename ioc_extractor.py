import re

def extract_iocs(content):
    # 1. Convert the binary PDF data into a string so we can search it
    # We use 'latin-1' because it won't crash on PDF binary data
    if isinstance(content, bytes):
        content = content.decode('latin-1', errors='ignore')
    
    # 2. Define the pattern for IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    # 3. Find the IPs directly in the content (no need to open a file!)
    ips = re.findall(ip_pattern, content)
    
    return ips