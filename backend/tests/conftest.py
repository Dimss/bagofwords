import asyncio
import pytest
import os
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generator, AsyncGenerator
from fastapi.testclient import TestClient
from alembic.config import Config
from alembic import command

from app.models.base import Base
from app.settings.config import settings
from app.settings.database import create_async_database_engine, create_async_session_factory

from tests.fixtures.client import test_client
from tests.fixtures.user import create_user
from tests.fixtures.auth import login_user

from main import app

@pytest.fixture(scope="session")
def alembic_config():
    """Create Alembic configuration object."""
    print(f"Using test database URL: {settings.TEST_DATABASE_URL}")
    
    # Ensure the database directory exists
    db_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db")
    if not os.path.exists(db_dir):
        print(f"Creating database directory: {db_dir}")
        os.makedirs(db_dir, exist_ok=True)
    
    alembic_cfg = Config("alembic.ini")
    # Convert aiosqlite to sqlite for alembic
    sync_url = settings.TEST_DATABASE_URL.replace('sqlite+aiosqlite:', 'sqlite:')
    alembic_cfg.set_main_option("sqlalchemy.url", sync_url)
    return alembic_cfg

@pytest.fixture(scope="session", autouse=True)
def run_migrations(alembic_config):
    """Run migrations before tests and downgrade after."""
    print("Starting migrations...")
    command.upgrade(alembic_config, "head")
    print("Migrations completed!")
    yield
    print("Downgrading migrations...")
    command.downgrade(alembic_config, "base")

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "e2e: marks tests as end-to-end tests"
    )