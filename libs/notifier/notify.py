from functools import wraps
from loguru import logger
from ..aws import apigtw


def apigateway(function):
    @wraps(function)
    def wrapper(event, context):
        try:
            logger.info(f"starting lambda - {context.function_name} | event - {event}")
            result = function(event, context)
        except Exception as e:
            logger.exception(e)
            return apigtw.response(400, e.__repr__())
        else:
            logger.success(f"success lambda - {context.function_name} | result - {result}")
            return apigtw.response(result["statusCode"], result["body"])

    return wrapper


def execution(function):
    @wraps(function)
    def wrapper(event, context):
        try:
            logger.info(f"starting lambda - {context.function_name} | event - {event}")
            result = function(event, context)
        except Exception as e:
            logger.exception(e)
            return "fail"
        else:
            logger.success(f"success lambda - {context.function_name} | result - {result}")
            return "success"

    return wrapper




