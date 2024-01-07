import pytest
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.api import router as api_router
from utils.exception import CustomHTTPException 

def start_application():
    app = FastAPI()
    app.include_router(api_router)
    @app.exception_handler(CustomHTTPException)
    async def custom_http_exception_handler(request, exc: CustomHTTPException):
        return exc.as_response()
    return app

# Inisialisasi database engine sekali untuk seluruh sesi pengujian
@pytest.fixture(scope="session")
def db_engine() -> Engine:
    """Create a database engine once for the entire testing session."""
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    return engine

# Membuat FastAPI instance untuk setiap fungsi pengujian
@pytest.fixture(scope="function")
def app(db_engine: Engine) -> FastAPI:
    """Create a new FastAPI instance for each test function."""
    _app = start_application()
    return _app

# Membuat database session baru untuk setiap fungsi pengujian
@pytest.fixture(scope="function")
def db_session(db_engine: Engine) -> Session:
    """Create a new database session for each test function."""
    SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    connection = db_engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()
