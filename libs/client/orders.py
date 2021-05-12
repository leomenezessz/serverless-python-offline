import os

from boto3.dynamodb.conditions import Attr
from ..aws import dynamo

_ORDERS_TABLE = os.environ["ORDERS_TABLE"]


def in_range(start_date, end_date):
    return dynamo.scan(
        _ORDERS_TABLE,
        FilterExpression=Attr("requestedAtDate").between(start_date, end_date),
    ).get("Items", [])


def save(order):
    return dynamo.save(order, _ORDERS_TABLE)


def update(order_id, status):
    return dynamo.update(
        _ORDERS_TABLE,
        Key={"id": order_id},
        UpdateExpression="set #st=:s",
        ExpressionAttributeValues={":s": status},
        ReturnValues="UPDATED_NEW",
        ExpressionAttributeNames={"#st": "status"},
    )
