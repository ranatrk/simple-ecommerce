from app.app import create_app
import pytest


@pytest.fixture()
def app_client():
    with create_app().test_client() as test_client:
        # app = create_app()
        return test_client

