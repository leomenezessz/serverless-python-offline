import json

from libs.client import mailer
from validator import validate
from libs.notifier import notify


@notify.execution
def send_mail(event, context):
    order = json.loads(event["Records"][0]["Sns"]["Message"])
    order = validate(order)
    return mailer.send(order)
