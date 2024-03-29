from server.database import config
import pytest
from server.managers.user import User


@pytest.fixture(scope="module", autouse=True)
def fake_db():
    # config.db = config.client.test_db
    User.users = config.client.test_db.users
    yield
    config.client.drop_database('test_db')
