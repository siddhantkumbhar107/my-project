import os
from flask import Flask, request, render_template, jsonify
from analyzer import analyze_pdf

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")


# WEB FORM ANALYSIS
@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')

    if not file:
        return "No file uploaded"

    filename = file.filename
    filepath = "temp.pdf"
    file.save(filepath)

    result = analyze_pdf(filepath)
    result["file_name"] = filename

    return render_template("result.html", result=result)


# API ANALYSIS (JSON)
@app.route('/api/analyze', methods=['POST'])
def api_analyze():   # ✅ IMPORTANT: DIFFERENT NAME
    file = request.files.get('file')

    if not file:
        return jsonify({"error": "No file uploaded"})

    filename = file.filename
    filepath = "temp.pdf"
    file.save(filepath)

    result = analyze_pdf(filepath)
    result["file_name"] = filename

    return jsonify(result)
