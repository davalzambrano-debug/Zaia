from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientBase(BaseModel):
    contactTittle: str
    nameClient: str
    emailClient: EmailStr
    rfcClient: str
    phoneClient: str
    addressClient: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    contactTittle: Optional[str] = None
    nameClient: Optional[str] = None
    emailClient: Optional[EmailStr] = None
    rfcClient: Optional[str] = None
    phoneClient: Optional[str] = None
    addressClient: Optional[str] = None

class ClientResponse(ClientBase):
    clientID: int

    class Config:
        from_attributes = True