from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    rol: str
    nameUser: str
    phoneUser: str
    rfcUser: str
    addressUser: str
    email: EmailStr
    userName: str

class UserCreate(UserBase):
    password: str
    
class UserUpdate(BaseModel):
    rol: Optional[str] = None
    nameUser: Optional[str] = None
    phoneUser: Optional[str] = None
    rfcUser: Optional[str] = None
    addressUser: Optional[str] = None
    userName: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    userID: int

    class Config:
        from_attributes = True