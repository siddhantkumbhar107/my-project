import json
from analyzer import analyze_pdf

def handler(request):

    # ✅ For browser test
    if request.method == "GET":
        return {
            "statusCode": 200,
            "body": "API is working"
        }

    # ✅ THIS IS WHERE YOU ADD IT
    if request.method == "POST":

        file = request.files.get("file")   

        if not file:
            return {
                "statusCode": 400,
                "body": "No file uploaded"
            }

        filepath = "/tmp/temp.pdf"
        file.save(filepath)

        result = analyze_pdf(filepath)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(result)
        }
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(result)
}
    return {
        "statusCode": 405,
        "body": "Method Not Allowed"
    }
