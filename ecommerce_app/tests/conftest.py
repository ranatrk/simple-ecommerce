import sys
import os


from ecommerce_app.ecommerce_app import create_app
import pytest


@pytest.fixture()
def app_client():
    with create_app().test_client() as test_client:
        return test_client

