
def test_lambda_wsgi(lambda_app):
    event = {
        "httpMethod": "GET",
        "path": "/"
    }
    response = lambda_app.handle(event, {})
    assert response["statusCode"] == "200"
    assert not response["isBase64Encoded"]
    assert response["headers"] == {"Content-Type": "text/plain; charset=utf-8"}
    assert response["body"].startswith("Hello world!")
