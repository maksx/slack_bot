import os
import pytest

from slack_sdk import WebClient
from slack_bolt import App


@pytest.fixture
def mocked_slack_app(monkeypatch):
    signing_secret = "secret"
    valid_token = "xoxb-valid"
    mock_api_server_base_url = "http://localhost:8888"

    web_client = WebClient(
        token=valid_token,
        base_url=mock_api_server_base_url
    )
    app = App(
        client=web_client,
        signing_secret=signing_secret
    )

    monkeypatch.setattr('slack_bolt.App', app)
