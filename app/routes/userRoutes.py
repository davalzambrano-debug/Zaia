from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import GetDB
from app.services.userService import UserService
from app.schemas.userSchema import UserCreate, UserUpdate
from app.core.security import get_current_user

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return UserService(db).GetAll()

@router.get("/{userID}")
def GetByID(userID: int, db: Session = Depends(GetDB)):
    return UserService(db).GetByID(userID)

@router.post("/")
def Create(data: UserCreate, db: Session = Depends(GetDB)):
    return UserService(db).Create(data)

@router.put("/{userID}")
def Update(userID: int, data: UserUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return UserService(db).Update(userID, data)

@router.delete("/{userID}")
def Delete(userID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return UserService(db).Delete(userID)
