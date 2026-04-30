from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Store(Base):
    __tablename__ = "stores"

    storeID      = Column(Integer, primary_key=True)
    nameStore    = Column(String(255), nullable=False)
    addressStore = Column(String(255), nullable=False)
    phoneStore   = Column(String(16), nullable=False)
    emailStore   = Column(String(255), nullable=False)
