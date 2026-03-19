import json
from analyzer import analyze_pdf
from http.server import BaseHTTPRequestHandler
def handler(request):
    return {
        "statusCode": 200,
        "body": "API is working"
    }
