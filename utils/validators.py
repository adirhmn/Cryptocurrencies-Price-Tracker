from sqlalchemy.orm import Session
from models import User, UserSignIn, Tracker
from .exception import CustomHTTPException
from .utils import hash_password
from dotenv import load_dotenv
import requests
import os
import re

# Load environment variables
load_dotenv()

BASE_URL_COINCAP = os.getenv("BASE_URL_COINCAP")

def validate_existing_user(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        raise CustomHTTPException(status_code=400, detail="Email already registered")

def validate_password_match(password: str, password_confirm: str):
    if password != password_confirm:
        raise CustomHTTPException(status_code=400, detail="Password not match")

def validate_password(password: str):
    if len(password) < 5:
        msg = "Password must be more than equal to 5 characters"
        raise CustomHTTPException(status_code=400, detail=msg)
    
    if not re.search(r"\d", password):
        msg = "Password must contain at least one number"
        raise CustomHTTPException(status_code=400, detail=msg)
    
    if not re.search(r"[^\w\s]", password):
        msg = "Password must contain at least one symbol"
        raise CustomHTTPException(status_code=400, detail=msg)

def validate_signin(userSignIn: UserSignIn, db: Session):
    user = db.query(User).filter(User.email == userSignIn.email).first()
    if not user:
        raise CustomHTTPException(status_code=404, detail="User not found")

    if not user.password == hash_password(userSignIn.password):
        raise CustomHTTPException(status_code=400, detail="Wrong password")

def validate_coin(coin: str, user: User, db: Session):
    url = BASE_URL_COINCAP + coin
    response = requests.get(url)
    if response.status_code != 200:
        raise CustomHTTPException(status_code=404, detail=f"{coin} not found")
    
    coin_exists = db.query(Tracker).filter(Tracker.id_user==user.id, Tracker.coin==coin).first()
    if coin_exists:
        raise CustomHTTPException(status_code=400, detail=f"{coin} already added")


