import json
import os
from datetime import datetime
from libs.aws import sns
from validator import validate
from libs.notifier import notify

_ORDERS_TOPIC = os.environ["ORDERS_TOPIC"]


def _fake_payment(order, status):
    stamp = datetime.now()
    order["processedAtDate"] = stamp.strftime("%Y-%m-%d")
    order["processedAtTime"] = stamp.strftime("%H:%M:%S")
    order["status"] = status
    return order


@notify.execution
def process_order(event, context):
    order = json.loads(event.get("Records")[0]["body"])
    order = validate(order)
    if not sns.send(_ORDERS_TOPIC, _fake_payment(order, "processed")).get("MessageId"):
        sns.send(_ORDERS_TOPIC, _fake_payment(order, "fail"))
