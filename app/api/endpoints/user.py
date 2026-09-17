from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import UserModel
from app.schemas.user import UserCreate, UserResponse, TokenResponse
from app.models.token import BlockedTokenModel
from app.core.security import create_access_token, create_refresh_token, verify_token, get_current_user_id
import uuid

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="A user with that username already exists")

    new_user = UserModel(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=TokenResponse)
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == user_data.username).first()
    if user and user.verify_password(user_data.password):
        jti = str(uuid.uuid4())
        is_admin = user.id == 1
        access_token = create_access_token(data={"sub": user.id, "isAdmin": is_admin, "jti": jti, "fresh": True})
        refresh_token = create_refresh_token(data={"sub": user.id, "jti": str(uuid.uuid4())})
        return {"access_token": access_token, "refresh_token": refresh_token}

    raise HTTPException(status_code=401, detail="Invalid username or password")

@router.post("/logout")
def logout(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    jti = payload.get("jti")
    user_id = payload.get("sub")
    if jti:
        blocked_token = BlockedTokenModel(jti=jti)
        db.add(blocked_token)
        db.commit()
    return {"message": f"User {user_id} has successfully Logged out."}

@router.post("/refresh", response_model=TokenResponse)
def refresh(payload: dict = Depends(verify_token)):
    user_id = payload.get("sub")
    is_admin = payload.get("isAdmin", False)
    new_jti = str(uuid.uuid4())
    new_access_token = create_access_token(data={"sub": user_id, "isAdmin": is_admin, "jti": new_jti, "fresh": False})
    return {"access_token": new_access_token, "refresh_token": ""}

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Couldn't find the user")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Couldn't find the user")
    db.delete(user)
    db.commit()
    return {"message": "User has been deleted"}
