import json
import os

from libs.aws import sqs
from validator import validate
from datetime import datetime
from libs.utils import randonic
from libs.notifier import notify

_ORDERS_QUEUE = os.environ["ORDERS_QUEUE"]


def _generate_order_stamps(order):
    stamp = datetime.now()
    order["requestedAtDate"] = stamp.strftime("%Y-%m-%d")
    order["requestedAtTime"] = stamp.strftime("%H:%M:%S")
    order["status"] = "received"
    order["id"] = randonic.random_uuid4()
    return order


@notify.apigateway
def send_order(event, context):
    payload = json.loads(event.get("body"))
    order = validate(payload)
    response = sqs.send(_ORDERS_QUEUE, _generate_order_stamps(order))
    return {"statusCode": 200, "body": response}
