import os
from flask import Flask, request, render_template, jsonify
from analyzer import analyze_pdf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')

    if not file:
        return "No file uploaded"

    filepath = "temp.pdf"
    file.save(filepath)

    result = analyze_pdf(filepath)

    return render_template("result.html", result=result)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    file = request.files.get('file')

    if not file:
        return jsonify({"error": "No file uploaded"})

    filepath = "temp.pdf"
    file.save(filepath)

    result = analyze_pdf(filepath)

    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
