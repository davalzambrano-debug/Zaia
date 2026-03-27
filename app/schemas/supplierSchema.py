from pydantic import BaseModel, EmailStr
from typing import Optional

class SupplierBase(BaseModel):
    contactTittle: str
    nameSupplier: str
    emailSupplier: EmailStr
    rfcSupplier: str
    phoneSupplier: str
    addressSupplier: str

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    contactTittle: Optional[str] = None
    nameSupplier: Optional[str] = None
    emailSupplier: Optional[EmailStr] = None
    rfcSupplier: Optional[str] = None
    phoneSupplier: Optional[str] = None
    addressSupplier: Optional[str] = None

class SupplierResponse(SupplierBase):
    supplierID: int

    class Config:
        from_attributes = True