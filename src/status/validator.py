from schema import Schema

body_validation = Schema({"status": str}, ignore_extra_keys=True)
path_validation = Schema({"id": str}, ignore_extra_keys=True)


def validate_path(event):
    return path_validation.validate(event)


def validate_body(body):
    return body_validation.validate(body)
