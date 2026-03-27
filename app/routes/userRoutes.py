from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import product_service
from app.schemas.productsSchema import ProductCreate, ProductResponse

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
           current_user=Depends(get_current_user)):
    return UserService(db).Update(userID, data)

@router.delete("/{userID}")
def Delete(userID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return UserService(db).Delete(userID)