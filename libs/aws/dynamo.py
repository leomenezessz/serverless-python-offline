import os

import boto3

_client = boto3.resource(
    "dynamodb",
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
    endpoint_url=os.environ["DYNAMO_ENDPOINT"],
)


def save(item, table):
    return _client.Table(table).put_item(Item=item)


def scan(table, **kwargs):
    return _client.Table(table).scan(**kwargs)


def update(table, **kwargs):
    return _client.Table(table).update_item(**kwargs)
