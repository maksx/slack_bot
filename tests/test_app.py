import pytest


def test_simple_sum(mocked_slack_app):
    assert app.app.simple_sum(2, 5)
