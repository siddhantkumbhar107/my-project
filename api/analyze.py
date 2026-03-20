import json
from analyzer import analyze_pdf

def handler(request):

    if request.method == "GET":
        return {
            "statusCode": 200,
            "body": "API is working"
        }

    if request.method == "POST":
        try:
            body = request.body

            if not body:
                return {
                    "statusCode": 400,
                    "body": "No file received"
                }

            filepath = "/tmp/temp.pdf"

            with open(filepath, "wb") as f:
                f.write(body)

            # 🔥 DEBUG START
            try:
                result = analyze_pdf(filepath)
            except Exception as e:
                return {
                    "statusCode": 500,
                    "body": "Analyzer error: " + str(e)
                }
            # 🔥 DEBUG END

            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(result)
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": "Main error: " + str(e)
            }

    return {
        "statusCode": 405,
        "body": "Method Not Allowed"
    }
