from pydantic import BaseModel
from typing import Optional
from datetime import date

class SalesBase(BaseModel):
    productID: int
    userID: int
    clientID: int
    typeSale: str
    totalSale: float
    dateSale: date

class SalesCreate(SalesBase):
    pass

class SalesUpdate(BaseModel):
    productID: Optional[int] = None
    userID: Optional[int] = None
    clientID: Optional[int] = None
    typeSale: Optional[str] = None
    totalSale: Optional[float] = None
    dateSale: Optional[date] = None

class SalesResponse(SalesBase):
    salesID: int

    class Config:
        from_attributes = True


# SalesDetails schemas

class SalesDetailsBase(BaseModel):
    productID: int
    quantity: int
    size: str
    price: float
    subtotal: float

class SalesDetailsCreate(SalesDetailsBase):
    pass

class SalesDetailsUpdate(BaseModel):
    productID: Optional[int] = None
    quantity: Optional[int] = None
    size: Optional[str] = None
    price: Optional[float] = None
    subtotal: Optional[float] = None

class SalesDetailsResponse(SalesDetailsBase):
    salesDetailsID: int

    class Config:
        from_attributes = True