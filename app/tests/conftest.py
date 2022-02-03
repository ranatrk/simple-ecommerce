import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from app.server import create_app
import pytest


@pytest.fixture()
def app_client():
    with create_app().test_client() as test_client:
        return test_client

