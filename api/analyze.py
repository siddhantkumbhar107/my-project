import json
from analyzer import analyze_pdf
from http.server import BaseHTTPRequestHandler
def handler(request):
    if request.method == "POST":
        file = request.files["file"]

        filepath = "/tmp/temp.pdf"
        file.save(filepath)

        result = analyze_pdf(filepath)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(result)
        }

    return {
        "statusCode": 405,
        "body": "Method Not Allowed"
    }
