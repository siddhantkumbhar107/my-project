import json

def handler(request):
    try:
        return {
            "statusCode": 200,
            "body": "API WORKING ✅"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
