from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import GetDB
from app.schemas.storeSchema import StoreCreate, StoreUpdate
from app.services.storeService import StoreService
from app.core.security import get_current_user

router = APIRouter(prefix="/stores", tags=["Stores"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return StoreService(db).GetAll()

@router.get("/{storeID}")
def GetByID(storeID: int, db: Session = Depends(GetDB)):
    return StoreService(db).GetByID(storeID)

@router.post("/")
def Create(data: StoreCreate, db: Session = Depends(GetDB)):
    return StoreService(db).Create(data)

@router.put("/{storeID}")
def Update(storeID: int, data: StoreUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return StoreService(db).Update(storeID, data)

@router.delete("/{storeID}")
def Delete(storeID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return StoreService(db).Delete(storeID)
