import hashlib
import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
BASE_URL_COINCAP = os.getenv("BASE_URL_COINCAP")
URL_CONVERTER_API = os.getenv("URL_CONVERTER_API")

def create_access_token(data: dict):
    """
    create jwt access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def hash_password(password: str) -> str:
    """
    hash password with SHA-256.
    """
    
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(password_bytes)
    hashed_password = hash_object.hexdigest()
    return hashed_password

def convert_usd_to_idr(price: float) -> float:
    url = URL_CONVERTER_API
    response = requests.get(url)
    return price * float(response.json()['rates']['IDR'])

def get_data_coin(coin: str) -> dict:
    url = BASE_URL_COINCAP + coin
    response = requests.get(url)
    if response.status_code != 200:
        data = {
            "name": coin,
            "symbol": "coin not found",
            "priceIdr": "coin not found"
        }
        return data
    data = {
        "name": response.json()['data']['name'],
        "symbol": response.json()['data']['symbol'],
        "priceIdr": convert_usd_to_idr(float(response.json()['data']['priceUsd']))
    }
    return data