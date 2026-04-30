from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    productID   = Column(Integer, primary_key=True)
    supplierID  = Column(Integer, ForeignKey("suppliers.supplierID"), nullable=False)
    storeID     = Column(Integer, ForeignKey("stores.storeID"), nullable=False)
    code        = Column(String(50), nullable=False, unique=True)  # unique product code
    nameProduct = Column(String(255), nullable=False)
    stock       = Column(Integer, nullable=False)
    category    = Column(String(50), nullable=False)
