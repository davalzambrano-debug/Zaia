# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

# Products model definition
class Product(Base):
    """
    SQLAlchemy model for the products table.
    Attributes:
        productID (int): Primary key.
        supplierID (int): Foreign key referencing suppliers table.
        storeID (int): Foreign key referencing stores table.
        code (str): Unique product code.    
        nameProduct (str): Name of the product.
        stock (int): Available stock of the product.
        category (str): Category of the product.        
    """
    __tablename__ = "products"

    productID = Column(Integer, primary_key=True)
    supplierID = Column(Integer, ForeignKey("suppliers.supplierID"), nullable=False)
    storeID = Column(Integer, ForeignKey("stores.storeID"), nullable=False)
    code = Column(String(50), nullable=False, unique=True)
    nameProduct = Column(String(255), nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)