from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    supplierID: int
    storeID: int
    code: str
    nameProduct: str
    stock: int
    type: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    supplierID: Optional[int] = None
    storeID: Optional[int] = None
    code: Optional[str] = None
    nameProduct: Optional[str] = None
    stock: Optional[int] = None
    type: Optional[str] = None

class ProductResponse(ProductBase):
    productID: int

    class Config:
        from_attributes = True