from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database.session import Base
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class UserSignUp(UserSignIn):
    password_confirm: str

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    trackers = relationship("Tracker", back_populates="user")
