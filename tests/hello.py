import json

import pytest
from assertpy import assert_that
from src.hello.handler import hello


@pytest.mark.vcr
def test_hello_handler(event, context):
    response = hello(event, context)
    body = json.loads(response.get("body"))[0]
    assert_that(body["name"]).is_equal_to("blastoise")


