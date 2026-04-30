from pydantic import BaseModel, EmailStr
from typing import Optional

class StoreBase(BaseModel):
    nameStore: str
    addressStore: str
    phoneStore: str
    emailStore: EmailStr

class StoreCreate(StoreBase):
    pass

class StoreUpdate(BaseModel):
    nameStore: Optional[str] = None
    addressStore: Optional[str] = None
    phoneStore: Optional[str] = None
    emailStore: Optional[EmailStr] = None

class StoreResponse(StoreBase):
    storeID: int

    class Config:
        from_attributes = True