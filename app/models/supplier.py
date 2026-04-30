from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    supplierID      = Column(Integer, primary_key=True)
    contactTittle   = Column(String(100), nullable=False)
    nameSupplier    = Column(String(255), nullable=False)
    emailSupplier   = Column(String(100), nullable=False)
    rfcSupplier     = Column(String(13), nullable=False)
    phoneSupplier   = Column(String(16), nullable=False)
    addressSupplier = Column(String(255), nullable=False)
