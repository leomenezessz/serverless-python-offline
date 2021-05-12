import json


def response(status_code, body, isBase64=False):
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json",
        },
        "isBase64Encoded": isBase64,
    }
