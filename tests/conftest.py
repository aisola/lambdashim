from wsgiref.simple_server import demo_app

import pytest

from lambdashim import LambdaWSGI


@pytest.fixture
def lambda_app() -> LambdaWSGI:
    return LambdaWSGI(app=demo_app)
