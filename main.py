6from flask import Flask, request, render_template, jsonify
from analyzer import analyze_pdf
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "PDF Malware Analyzer is running 🚀"


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']

    filepath = "temp.pdf"
    file.save(filepath)

    result = analyze_pdf(filepath)

    return render_template("result.html", result=result)


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    file = request.files['file']

    filepath = "temp.pdf"
    file.save(filepath)

    result = analyze_pdf(filepath)

    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
