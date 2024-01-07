from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from models import User, TokenPayload
from utils.exception import CustomHTTPException
from database.session import get_db
import jwt
from jwt import PyJWTError
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Optional[User]:
    """
    Verify the JWT token and get the current user.
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError as e:
        error_message = str(e)
        raise CustomHTTPException(status_code=401, detail=error_message)
    
    user = db.query(User).filter(User.email == token_data.sub).first()
    if not user:
        raise CustomHTTPException(status_code=401, detail="Could not validate credentials")
    return user
