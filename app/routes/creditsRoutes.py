from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.db.database import GetDB
from app.schemas.creditsSchema import CreditsCreate, CreditsUpdate, CreditPaymentsCreate, CreditPaymentsUpdate
from app.services.creditsService import CreditsService, CreditPaymentsService
from app.core.security import get_current_user

router = APIRouter(prefix="/credits", tags=["Credits"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return CreditsService(db).GetAll()

# Specific routes before /{creditID} to avoid routing conflicts
@router.get("/filter/status")
def GetByStatus(status: str, db: Session = Depends(GetDB)):
    return CreditsService(db).GetByStatus(status)

@router.get("/filter/overdue")
def GetOverdue(current_date: date, db: Session = Depends(GetDB)):
    return CreditsService(db).GetOverdue(current_date)

@router.get("/client/{clientID}")
def GetByClient(clientID: int, db: Session = Depends(GetDB)):
    return CreditsService(db).GetByClient(clientID)

@router.get("/{creditID}")
def GetByID(creditID: int, db: Session = Depends(GetDB)):
    return CreditsService(db).GetByID(creditID)

@router.post("/")
def Create(data: CreditsCreate, db: Session = Depends(GetDB)):
    return CreditsService(db).Create(data)

@router.put("/{creditID}")
def Update(creditID: int, data: CreditsUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return CreditsService(db).Update(creditID, data)

@router.delete("/{creditID}")
def Delete(creditID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):  # JWT required
    return CreditsService(db).Delete(creditID)


# Credit payments router registered separately in main.py
routerCreditPayments = APIRouter(prefix="/credit-payments", tags=["Credit Payments"])

@routerCreditPayments.get("/")
def GetAllPayments(db: Session = Depends(GetDB)):
    return CreditPaymentsService(db).GetAll()

@routerCreditPayments.get("/credit/{creditID}")
def GetByCredit(creditID: int, db: Session = Depends(GetDB)):
    return CreditPaymentsService(db).GetByCredit(creditID)

@routerCreditPayments.get("/{paymentID}")
def GetPaymentByID(paymentID: int, db: Session = Depends(GetDB)):
    return CreditPaymentsService(db).GetByID(paymentID)

@routerCreditPayments.post("/")
def CreatePayment(data: CreditPaymentsCreate, db: Session = Depends(GetDB)):
    return CreditPaymentsService(db).Create(data)

@routerCreditPayments.put("/{paymentID}")
def UpdatePayment(paymentID: int, data: CreditPaymentsUpdate, db: Session = Depends(GetDB),
                  current_user=Depends(get_current_user)):  # JWT required
    return CreditPaymentsService(db).Update(paymentID, data)

@routerCreditPayments.delete("/{paymentID}")
def DeletePayment(paymentID: int, db: Session = Depends(GetDB),
                  current_user=Depends(get_current_user)):  # JWT required
    return CreditPaymentsService(db).Delete(paymentID)
