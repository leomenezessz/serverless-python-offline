import os

import redis

_REDIS_URL = os.environ["REDIS_URL"]
_REDIS_PORT = os.environ["REDIS_PORT"]

_client = redis.Redis(host=_REDIS_URL, port=_REDIS_PORT, db=0)


def add(key, value):
    return _client.set(name=key, value=value)


def get(key):
    return _client.get(key)
