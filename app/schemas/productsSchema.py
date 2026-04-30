from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    supplierID: int
    storeID: int
    code: str
    nameProduct: str
    stock: int
    category: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    supplierID: Optional[int] = None
    storeID: Optional[int] = None
    code: Optional[str] = None
    nameProduct: Optional[str] = None
    stock: Optional[int] = None
    category: Optional[str] = None

class ProductResponse(ProductBase):
    productID: int
    class Config:
        from_attributes = True
