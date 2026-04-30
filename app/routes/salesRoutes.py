from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.db.database import GetDB
from app.schemas.salesSchema import SalesCreate, SalesUpdate, SalesDetailsCreate, SalesDetailsUpdate
from app.services.salesService import SalesService, SalesDetailsService
from app.core.security import get_current_user

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return SalesService(db).GetAll()

# Specific routes before /{salesID} to avoid routing conflicts
@router.get("/filter/date-range")
def GetByDateRange(start: date, end: date, db: Session = Depends(GetDB)):
    return SalesService(db).GetByDateRange(start, end)

@router.get("/user/{userID}")
def GetByUser(userID: int, db: Session = Depends(GetDB)):
    return SalesService(db).GetByUser(userID)

@router.get("/client/{clientID}")
def GetByClient(clientID: int, db: Session = Depends(GetDB)):
    return SalesService(db).GetByClient(clientID)

@router.get("/{salesID}")
def GetByID(salesID: int, db: Session = Depends(GetDB)):
    return SalesService(db).GetByID(salesID)

@router.post("/")
def Create(data: SalesCreate, db: Session = Depends(GetDB)):
    return SalesService(db).Create(data)

@router.put("/{salesID}")
def Update(salesID: int, data: SalesUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return SalesService(db).Update(salesID, data)

@router.delete("/{salesID}")
def Delete(salesID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return SalesService(db).Delete(salesID)


# Sales details router registered separately in main.py
routerSalesDetails = APIRouter(prefix="/sales-details", tags=["Sales Details"])

@routerSalesDetails.get("/")
def GetAllDetails(db: Session = Depends(GetDB)):
    return SalesDetailsService(db).GetAll()

@routerSalesDetails.get("/product/{productID}")
def GetByProduct(productID: int, db: Session = Depends(GetDB)):
    return SalesDetailsService(db).GetByProduct(productID)

@routerSalesDetails.get("/{salesDetailsID}")
def GetDetailByID(salesDetailsID: int, db: Session = Depends(GetDB)):
    return SalesDetailsService(db).GetByID(salesDetailsID)

@routerSalesDetails.post("/")
def CreateDetail(data: SalesDetailsCreate, db: Session = Depends(GetDB)):
    return SalesDetailsService(db).Create(data)

@routerSalesDetails.put("/{salesDetailsID}")
def UpdateDetail(salesDetailsID: int, data: SalesDetailsUpdate, db: Session = Depends(GetDB),
                 current_user=Depends(get_current_user)):  # JWT required
    return SalesDetailsService(db).Update(salesDetailsID, data)

@routerSalesDetails.delete("/{salesDetailsID}")
def DeleteDetail(salesDetailsID: int, db: Session = Depends(GetDB),
                 current_user=Depends(get_current_user)):  # JWT required
    return SalesDetailsService(db).Delete(salesDetailsID)
