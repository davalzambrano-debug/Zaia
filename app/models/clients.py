# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Client(Base):
    """
    SQLAlchemy model for the clients table.
    Attributes:
        clientID (int): Primary key.
        contactTittle (str): Contact title for the client.
        nameClient (str): Client's name.
        emailClient (str): Client's email address.
        rfcClient (str): Client's RFC (tax ID).
        phoneClient (str): Client's phone number.
        addressClient (str): Client's address.
    """
    __tablename__ = "client"

    clientID      = Column(Integer, primary_key=True)
    contactTittle = Column(String(100), nullable=False)
    nameClient    = Column(String(255), nullable=False)
    emailClient   = Column(String(100), nullable=False)    
    rfcClient     = Column(String(13), nullable=False)
    phoneClient   = Column(String(16), nullable=False)
    addressClient = Column(String(255), nullable=False)