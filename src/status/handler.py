import json

from libs.client import orders
from libs.notifier import notify
from validator import validate_path, validate_body


@notify.execution
def update_order(event, context):
    path_param = validate_path(event.get("pathParameters"))
    body = validate_body(json.loads(event.get("body")))
    return orders.update(path_param["id"], body["status"])
