from libs.client import orders
from validator import validate
from libs.notifier import notify


@notify.apigateway
def orders_in_range(event, context):
    event = validate(event)
    start_at = event.get("queryStringParameters")["startAt"]
    end_at = event.get("queryStringParameters")["endAt"]
    items = orders.in_range(start_at, end_at)
    return {"statusCode": 200, "body": items}
