from pydantic import BaseModel
from typing import Optional
from datetime import date

class CreditsBase(BaseModel):
    clientID: int
    salesID: int
    totalAmount: float
    balance: float
    amountPaid: float
    startDate: date
    dueDate: date
    installments: int
    status: str

class CreditsCreate(CreditsBase):
    pass

class CreditsUpdate(BaseModel):
    clientID: Optional[int] = None
    salesID: Optional[int] = None
    totalAmount: Optional[float] = None
    balance: Optional[float] = None
    amountPaid: Optional[float] = None
    startDate: Optional[date] = None
    dueDate: Optional[date] = None
    installments: Optional[int] = None
    status: Optional[str] = None

class CreditsResponse(CreditsBase):
    creditID: int

    class Config:
        from_attributes = True

# CreditPayments schemas

class CreditPaymentsBase(BaseModel):
    creditID: int
    amount: float
    paymentDate: float
    paymentMethod: str
    notes: str

class CreditPaymentsCreate(CreditPaymentsBase):
    pass

class CreditPaymentsUpdate(BaseModel):
    creditID: Optional[int] = None
    amount: Optional[float] = None
    paymentDate: Optional[float] = None
    paymentMethod: Optional[str] = None
    notes: Optional[str] = None

class CreditPaymentsResponse(CreditPaymentsBase):
    paymentID: int

    class Config:
        from_attributes = True