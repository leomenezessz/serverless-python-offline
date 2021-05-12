from schema import Schema

schema = Schema({"queryStringParameters": {"limit": str}}, ignore_extra_keys=True)


def validate(event):
    return schema.validate(event)
