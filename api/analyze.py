import json
from analyzer import analyze_pdf

def handler(request):

    # ✅ Test in browser
    if request.method == "GET":
        return {
            "statusCode": 200,
            "body": "API is working"
        }

    # ✅ Handle POST
    if request.method == "POST":
        try:
            # 🔥 THIS IS THE CORRECT WAY IN VERCEL
            body = request.body

            if not body:
                return {
                    "statusCode": 400,
                    "body": "No file received"
                }

            filepath = "/tmp/temp.pdf"

            with open(filepath, "wb") as f:
                f.write(body)

            result = analyze_pdf(filepath)

            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(result)
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": str(e)
            }

    return {
        "statusCode": 405,
        "body": "Method Not Allowed"
    }
  
