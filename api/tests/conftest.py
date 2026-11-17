import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
 
from api.database import get_db
from api.main import app
from api.models import Base
 
TEST_KEY = "test-key"
 
 
@pytest.fixture()
def _test_database(monkeypatch):
    """A brand-new, empty, in-memory database for every single test."""
    monkeypatch.setenv("API_KEY", TEST_KEY)
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,          # keep one connection so the in-memory DB survives
    )
    Base.metadata.create_all(engine)   # safe here: this is the throw-away test database
    TestingSession = sessionmaker(bind=engine, autoflush=False)
 
    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()
 
    app.dependency_overrides[get_db] = override_get_db
    yield
    app.dependency_overrides.clear()
    engine.dispose()
 
 
@pytest.fixture()
def client(_test_database):
    """A test client that sends the correct API key."""
    with TestClient(app, headers={"X-API-Key": TEST_KEY}) as test_client:
        yield test_client
 
 
@pytest.fixture()
def anon_client(_test_database):
    """A test client that sends NO API key."""
    with TestClient(app) as test_client:
        yield test_client
