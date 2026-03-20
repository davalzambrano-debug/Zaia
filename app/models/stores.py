# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String
from app.db.database import Base

# Store model definition
class Store(Base):
    """
    SQLAlchemy model for the stores table.
    Attributes:
        storeID (int): Primary key.
        nameStore (str): Name of the store.
        addressStore (str): Address of the store.
        phoneStore (str): Phone number of the store.
        emailStore (str): Email address of the store.
    """
    __tablename__ = "stores"

    storeID      = Column(Integer, primary_key=True)
    nameStore    = Column(String(255), nullable=False)
    addressStore = Column(String(255), nullable=False)
    phoneStore   = Column(String(16), nullable=False)
    emailStore   = Column(String(255), nullable=False)