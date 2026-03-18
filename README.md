# PDF Malware Analysis Toolkit

A Python-based modular toolkit for performing static analysis on PDF files to identify potential security threats.

## 🚀 Features
- *Metadata Extraction*: Identifies author, creator, and producer information.
- *Suspicious Keyword Scanning*: Checks for triggers like /JavaScript and /OpenAction.
- *IOC Extraction*: Pulls indicators of compromise, such as malicious URLs.
- *Security Reporting*: Generates a structured final risk assessment.

## 🛠️ Project Structure
- main.py: The entry point that coordinates the analysis.
- analyzer.py: Logic for keyword and threat detection.
- metadata.py: Handles PDF metadata extraction.
- ioc_extractor.py: Extracts URLs and other network indicators.
- report_generator.py: Formats the findings into a readable report.

## 📋 How to Run
1. Ensure you have Python installed.
2. Install dependencies (e.g., pip install PyPDF2).
3. Place your sample in the root folder as TEST.pdf.
4. Run the toolkit:
   ```bash
   python main.py

