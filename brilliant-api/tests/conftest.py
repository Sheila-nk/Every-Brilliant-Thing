import pytest
from tortoise.contrib.test import finalizer, initializer

from brilliant_api.config import settings

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    settings.TESTING = True

    initializer(["brilliant_api.models"], db_url=settings.DATABASE_URL_TEST)
    yield
    finalizer()
