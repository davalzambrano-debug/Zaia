from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import GetDB
from app.schemas.productsSchema import ProductCreate, ProductUpdate
from app.services.productsService import ProductService
from app.core.security import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return ProductService(db).GetAll()

# Specific routes before /{productID} to avoid routing conflicts
@router.get("/low-stock/")
def GetLowStock(threshold: int = 10, db: Session = Depends(GetDB)):
    return ProductService(db).GetLowStock(threshold)

@router.get("/supplier/{supplierID}")
def GetBySupplier(supplierID: int, db: Session = Depends(GetDB)):
    return ProductService(db).GetBySupplier(supplierID)

@router.get("/store/{storeID}")
def GetByStore(storeID: int, db: Session = Depends(GetDB)):
    return ProductService(db).GetByStore(storeID)

@router.get("/{productID}")
def GetByID(productID: int, db: Session = Depends(GetDB)):
    return ProductService(db).GetByID(productID)

@router.post("/")
def Create(data: ProductCreate, db: Session = Depends(GetDB)):
    return ProductService(db).Create(data)

@router.put("/{productID}")
def Update(productID: int, data: ProductUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return ProductService(db).Update(productID, data)

@router.delete("/{productID}")
def Delete(productID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return ProductService(db).Delete(productID)
