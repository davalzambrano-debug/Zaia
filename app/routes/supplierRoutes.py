from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import GetDB
from schemas.supplierSchema import SupplierCreate, SupplierUpdate
from services.supplier_services import SupplierService
from core.security import get_current_user

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return SupplierService(db).GetAll()

@router.get("/{supplierID}")
def GetByID(supplierID: int, db: Session = Depends(GetDB)):
    return SupplierService(db).GetByID(supplierID)

@router.post("/")
def Create(data: SupplierCreate, db: Session = Depends(GetDB)):
    return SupplierService(db).Create(data)

@router.put("/{supplierID}")
def Update(supplierID: int, data: SupplierUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return SupplierService(db).Update(supplierID, data)

@router.delete("/{supplierID}")
def Delete(supplierID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return SupplierService(db).Delete(supplierID)