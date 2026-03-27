from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import GetDB
from schemas.productsSchema import ProductCreate, ProductUpdate
from services.product_services import ProductService
from core.security import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def get_all(db: Session = Depends(GetDB)):
    return ProductService(db).get_all()

@router.get("/{productID}")
def get_by_id(productID: int, db: Session = Depends(GetDB)):
    return ProductService(db).get_by_id(productID)

@router.get("/supplier/{supplier_id}")
def get_by_supplier(supplier_id: int, db: Session = Depends(GetDB)):
    return ProductService(db).get_by_supplier(supplier_id)

@router.get("/store/{store_id}")
def get_by_store(store_id: int, db: Session = Depends(GetDB)):
    return ProductService(db).get_by_store(store_id)

@router.get("/low-stock/")
def get_low_stock(threshold: int = 10, db: Session = Depends(GetDB)):
    return ProductService(db).get_low_stock(threshold)

@router.post("/")
def create(data: ProductCreate, db: Session = Depends(GetDB)):
    return ProductService(db).create(data)

@router.put("/{productID}")
def update(productID: int, data: ProductUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return ProductService(db).update(productID, data)

@router.delete("/{productID}")
def delete(productID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return ProductService(db).delete(productID)