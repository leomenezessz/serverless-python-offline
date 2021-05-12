from collections import namedtuple

import pytest


@pytest.fixture
def event():
    return {"pathParameters": {"name": "blastoise"}}


@pytest.fixture
def context():
    ctx = {"function_name": "test"}
    return namedtuple("context", ctx.keys())(*ctx.values())

