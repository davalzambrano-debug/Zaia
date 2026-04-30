from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Client(Base):
    __tablename__ = "client"

    clientID      = Column(Integer, primary_key=True)
    contactTittle = Column(String(100), nullable=False)
    nameClient    = Column(String(255), nullable=False)
    emailClient   = Column(String(100), nullable=False)
    rfcClient     = Column(String(13), nullable=False)
    phoneClient   = Column(String(16), nullable=False)
    addressClient = Column(String(255), nullable=False)
