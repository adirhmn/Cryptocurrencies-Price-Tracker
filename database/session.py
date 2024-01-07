from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path ke file database SQLite
DATABASE_URL = "sqlite:///./myappdb.db"

# Inisialisasi engine database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Membuat sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Membuat base class untuk model
Base = declarative_base()

def get_db():
    """Get instance database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
