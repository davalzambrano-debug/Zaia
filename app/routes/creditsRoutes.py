from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from db.database import GetDB
from schemas.creditsSchema import CreditsCreate, CreditsUpdate
from services.credits_services import CreditsService
from core.security import get_current_user

router = APIRouter(prefix="/credits", tags=["Credits"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return CreditsService(db).GetAll()

@router.get("/{credit_id}")
def GetById(credit_id: int, db: Session = Depends(GetDB)):
    return CreditsService(db).GetById(credit_id)

@router.get("/client/{clientID}")
def GetByClient(clientID: int, db: Session = Depends(GetDB)):
    return CreditsService(db).GetByClient(clientID)

@router.get("/filter/status")
def GetByStatus(status: str, db: Session = Depends(GetDB)):
    return CreditsService(db).GetByStatus(status)

@router.get("/filter/overdue")
def GetOverdue(current_date: date, db: Session = Depends(GetDB)):
    return CreditsService(db).GetOverdue(current_date)

@router.post("/")
def Create(data: CreditsCreate, db: Session = Depends(GetDB)):
    return CreditsService(db).Create(data)

@router.put("/{credit_id}")
def Update(credit_id: int, data: CreditsUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return CreditsService(db).Update(credit_id, data)

@router.delete("/{credit_id}")
def Delete(credit_id: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return CreditsService(db).Delete(credit_id)


# Credit Payments
routerCreditPayments = APIRouter(prefix="/credit-payments", tags=["Credit Payments"])

@routerCreditPayments.get("/")
def GetAllCreditPayments(db: Session = Depends(GetDB)):
    return CreditsService(db).GetAllCreditPayments()

@routerCreditPayments.get("/{payment_id}")
def GetById(payment_id: int, db: Session = Depends(GetDB)):
    return CreditsService(db).GetCreditPaymentById(payment_id)

@routerCreditPayments.get("/credit/{credit_id}")
def GetByCredit(credit_id: int, db: Session = Depends(GetDB)):
    return CreditsService(db).GetCreditPaymentsByCredit(credit_id)

@routerCreditPayments.post("/")
def CreateCreditPayment(data: CreditPaymentCreate, db: Session = Depends(GetDB)):
    return CreditsService(db).CreateCreditPayment(data)

@routerCreditPayments.put("/{payment_id}")
def UpdateCreditPayment(payment_id: int, data: CreditPaymentUpdate, db: Session = Depends(GetDB),
                        current_user=Depends(get_current_user)):
    return CreditsService(db).UpdateCreditPayment(payment_id, data)

@routerCreditPayments.delete("/{payment_id}")
def DeleteCreditPayment(payment_id: int, db: Session = Depends(GetDB),
                        current_user=Depends(get_current_user)):
    return CreditsService(db).DeleteCreditPayment(payment_id)

