import json

from libs.aws import redis
from libs.client import pizzaria
from libs.notifier import notify
from validator import validate


@notify.apigateway
def pizzas(event, context):
    event = validate(event)
    limit = int(event.get("queryStringParameters")["limit"])

    if redis.get("20-pizzas") is None and limit == 20:
        items = pizzaria.get(limit)
        redis.add("20-pizzas", json.dumps(items))
    elif redis.get("20-pizzas") is not None and limit == 20:
        items = json.loads(redis.get("20-pizzas"))
    else:
        items = pizzaria.get(limit)

    return {"statusCode": 200, "body": items}
