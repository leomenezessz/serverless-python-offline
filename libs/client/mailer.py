from ..utils import randonic

_VALID_USER_IDS = {
    "b1ba31ba-2640-4898-82c2-395f02bd7xhg": {
        "name": "Joel",
        "mail": "joel.silva@@example.com",
    },
    "b1ba31ba-1111-4898-82c2-395f02bd7xZg": {
        "name": "Renanzinho",
        "mail": "renanzinho@example.com",
    },
}


def send(order):
    user_id = order.get("userId")
    if user_id in _VALID_USER_IDS.keys():
        return {"SendEmailResult": {"MessageId": randonic.random_uuid4()}}
    raise Exception("Mailer error")
