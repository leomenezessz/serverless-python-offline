from requests import get
from validator import validate
from libs.notifier import notify


@notify.apigateway
def hello(event, context):
    event = validate(event)
    name = event.get("pathParameters")["name"]
    response = get(f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=5)
    if response.status_code == 200:
        return {"statusCode": 200, "body": response.json()["forms"]}
    else:
        return {"statusCode": 404, "body": {"message": "pokemon not found!"}}
