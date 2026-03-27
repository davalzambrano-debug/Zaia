from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from db.database import GetDB
from schemas.salesSchema import SalesCreate, SalesUpdate
from services.sales_services import SalesService
from core.security import get_current_user

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.get("/")
def get_all(db: Session = Depends(GetDB)):
    return SalesService(db).get_all()

@router.get("/{salesID}")
def get_by_id(salesID: int, db: Session = Depends(GetDB)):
    return SalesService(db).get_by_id(salesID)

@router.get("/user/{user_id}")
def get_by_user(user_id: int, db: Session = Depends(GetDB)):
    return SalesService(db).get_by_user(user_id)

@router.get("/client/{client_id}")
def get_by_client(client_id: int, db: Session = Depends(GetDB)):
    return SalesService(db).get_by_client(client_id)

@router.get("/filter/date-range")
def get_by_date_range(start: date, end: date, db: Session = Depends(GetDB)):
    return SalesService(db).get_by_date_range(start, end)

@router.post("/")
def create(data: SalesCreate, db: Session = Depends(GetDB)):
    return SalesService(db).create(data)

@router.put("/{salesID}")
def update(salesID: int, data: SalesUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return SalesService(db).update(salesID, data)

@router.delete("/{salesID}")
def delete(salesID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return SalesService(db).delete(salesID)


# Sales Details
routerSalesDetails = APIRouter(prefix="/sales-details", tags=["Sales Details"])

@router.get("/")
def GetAllSalesDetails(db: Session = Depends(GetDB)):
    return SalesDetailsService(db).GetAllSalesDetails()

@router.get("/{detail_id}")
def GetByIDSalesDetails(detail_id: int, db: Session = Depends(GetDB)):
    return SalesDetailsService(db).GetByIDSalesDetails(detail_id)

@router.get("/product/{product_id}")
def GetByProductSalesDetails(product_id: int, db: Session = Depends(GetDB)):
    return SalesDetailsService(db).GetByProductSalesDetails(product_id)

@router.post("/")
def CreateSalesDetails(data: SalesDetailsCreate, db: Session = Depends(GetDB)):
    return SalesDetailsService(db).CreateSalesDetails(data)

@router.put("/{detail_id}")
def UpdateSalesDetails(detail_id: int, data: SalesDetailsUpdate, db: Session = Depends(GetDB),
                       current_user=Depends(get_current_user)):
    return SalesDetailsService(db).UpdateSalesDetails(detail_id, data)

@router.delete("/{detail_id}")
def DeleteSalesDetails(detail_id: int, db: Session = Depends(GetDB),
                       current_user=Depends(get_current_user)):
    return SalesDetailsService(db).DeleteSalesDetails(detail_id)