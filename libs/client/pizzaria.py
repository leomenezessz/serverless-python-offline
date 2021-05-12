import os

from ..aws import dynamo

PIZZAS_TABLE = os.environ["PIZZAS_TABLE"]


def get(limit):
    return dynamo.scan(
        PIZZAS_TABLE,
        Limit=limit,
        TableName=PIZZAS_TABLE,
        ProjectionExpression="id,#n,price",
        ExpressionAttributeNames={"#n": "name"},
    ).get("Items", [])
