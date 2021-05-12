import json
import os

import boto3

_client = boto3.client(
    "sqs",
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
    endpoint_url=os.environ["SQS_ENDPOINT"],
)


def send(queue, message):
    return _client.send_message(QueueUrl=queue, MessageBody=json.dumps(message))
