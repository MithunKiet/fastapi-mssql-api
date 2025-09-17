from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.user_models import UserCreate, UserOut
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserOut])
def get_users():
    return UserService.list_users()

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    user = UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate):
    return UserService.create_user(payload)
