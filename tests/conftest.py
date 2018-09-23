import pytest

from aiohttpdemo_polls.main import init_app
from aiohttpdemo_polls.settings import get_config
from init_db import (
    setup_db,
    teardown_db,
    create_tables,
    sample_data,
    drop_tables
)


@pytest.fixture
async def cli(loop, test_client, db):
    app = await init_app()
    return await test_client(app)


@pytest.fixture(scope='module')
def db():
    test_config = get_config()

    setup_db(test_config['postgres'])
    yield
    teardown_db(test_config['postgres'])


@pytest.fixture
def tables_and_data():
    create_tables()
    sample_data()
    yield
    drop_tables()
