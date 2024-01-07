from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path to the SQLite file database
DATABASE_URL = "sqlite:///./myappdb.db"

# Initialize the machine database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the model
Base = declarative_base()

def get_db():
    """Get instance database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
