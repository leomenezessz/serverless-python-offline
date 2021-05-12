from schema import Schema

validation = Schema({"pathParameters": {"name": str}}, ignore_extra_keys=True)


def validate(event):
    return validation.validate(event)
