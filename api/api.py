from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models import User, UserSignIn, UserSignUp, Tracker, SuccessResponse
from utils.exception import CustomHTTPException
from utils.validators import validate_existing_user, validate_password_match, validate_signin, validate_coin, validate_password
from utils.utils import hash_password, create_access_token, get_data_coin
from utils.jwt_utils import get_current_user


router = APIRouter()

@router.post("/signup/")
def create_user(user: UserSignUp, db: Session = Depends(get_db), response_model=SuccessResponse):
    validate_existing_user(db, user.email)
    validate_password(user.password)
    validate_password_match(user.password, user.password_confirm)

    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    response = {
        "email": new_user.email,
    }
    return SuccessResponse(data=response)

@router.post("/signin/")
def signin_user(user: UserSignIn, db: Session = Depends(get_db), response_model=SuccessResponse):
    validate_signin(user, db)
    access_token = create_access_token(data={"sub": user.email})
    response = {
        "email": user.email,
        "token" : access_token
    }
    return SuccessResponse(data=response)

@router.get("/signout/")
def signout_user(current_user: User = Depends(get_current_user), 
                 response_model=SuccessResponse):
    return SuccessResponse(data=f"{current_user.email} success signout")

@router.get("/tracker/")
def get_user_tracker(db: Session = Depends(get_db), 
                     current_user: User = Depends(get_current_user), 
                     response_model=SuccessResponse):
    """Retrieve tracker data for a user."""
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise CustomHTTPException(status_code=404, detail="User not found")

    user_tracker = db.query(Tracker).filter(Tracker.id_user == current_user.id).all()
    response = []
    for item in user_tracker:
        response_item = {}
        data_coin = get_data_coin(item.coin)
        response_item['name'] = data_coin.get('name', '')
        response_item['priceIdr'] = data_coin.get('priceIdr', '')
        response.append(response_item)
    return SuccessResponse(data=response)

@router.post("/tracker/{coin}")
def add_coin_tracker(coin: str, db: Session = Depends(get_db), 
                     current_user: User = Depends(get_current_user), response_model=SuccessResponse):
    """Add coin to a user's tracker."""
    coin = str.lower(coin)
    validate_coin(coin, current_user, db)
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise CustomHTTPException(status_code=404, detail="User not found")

    new_tracker= Tracker(id_user=current_user.id, coin=coin)
    db.add(new_tracker)
    db.commit()
    db.refresh(new_tracker)
    user_tracker = db.query(Tracker).filter(Tracker.id_user == current_user.id).all()
    response = []
    for item in user_tracker:
        response_item = {}
        data_coin = get_data_coin(item.coin)
        response_item['name'] = data_coin.get('name', '')
        response_item['priceIdr'] = data_coin.get('priceIdr', '')
        response.append(response_item)
    return SuccessResponse(data=response)

@router.delete("/tracker/{coin}")
def delete_coin_tracker(coin: str, db: Session = Depends(get_db),
                             current_user: User = Depends(get_current_user), 
                             response_model=SuccessResponse):
    """Removing coin from tracker."""
    coin = str.lower(coin)
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise CustomHTTPException(status_code=404, detail="User not found")
    
    mycoin = db.query(Tracker).filter(
        Tracker.id_user == current_user.id,
        Tracker.coin == coin
    ).first()

    if not mycoin:
        raise CustomHTTPException(status_code=404, detail=f"{coin} not found")

    db.delete(mycoin)
    db.commit()

    return SuccessResponse(data=f"{coin} success deleted")


@router.get("/health", tags=["health"])
def check_health():
    """Checking health of app."""
    return {"status": "success", "message": "App running well"}