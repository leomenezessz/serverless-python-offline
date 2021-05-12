import json

from libs.client import orders
from libs.notifier import notify
from validator import validate


@notify.execution
def save_order(event, context):
    order = json.loads(event["Records"][0]["Sns"]["Message"])
    order = validate(order)
    return orders.save(order)
