import json
import os

import boto3

client = boto3.client(
    "sns",
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
    endpoint_url=os.environ["SNS_ENDPOINT"],
)


def send(topic, message):
    return client.publish(TopicArn=topic, Message=json.dumps(message))
