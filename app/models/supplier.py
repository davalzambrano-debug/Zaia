# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String
from app.db.database import Base

# Suppliers model definition
class Supplier(Base):
    """
    SQLAlchemy model for the suppliers table.
    Attributes:
        supplierID (int): Primary key.
        nameSupplier (str): Name of the supplier.
        emailSupplier (str): Email address of the supplier.
        rfcSupplier (str): RFC (tax ID) of the supplier.
        phoneSupplier (str): Phone number of the supplier.
        addressSupplier (str): Address of the supplier.
    """
    __tablename__ = "suppliers"

    supplierID      = Column(Integer, primary_key=True)
    contactTittle   = Column(String(100), nullable=False)
    nameSupplier    = Column(String(255), nullable=False)
    emailSupplier   = Column(String(100), nullable=False)
    rfcSupplier     = Column(String(13), nullable=False)
    phoneSupplier   = Column(String(16), nullable=False)
    addressSupplier = Column(String(255), nullable=False)