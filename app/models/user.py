# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String
from app.db.database import Base

# User model definition
class User(Base):
    """
    SQLAlchemy model for the users table.
    Attributes:
        userID (int): Primary key.
        rol (str): User role, default is 'user'.
        nameUser (str): User's full name.
        phoneUser (str): User's phone number.
        rfcUser (str): User's RFC (tax ID).
        addressUser (str): User's address.
        password (str): User's hashed password.
        userName (str): User's username.
    """
    __tablename__ = "users"

    userID      = Column(Integer, primary_key=True)
    rol         = Column(String(20), nullable=False, default='user')
    nameUser    = Column(String(255), nullable=False)
    phoneUser   = Column(String(16), nullable=False)
    rfcUser     = Column(String(13), nullable=False)
    addressUser = Column(String(255), nullable=False)
    password    = Column(String(50), nullable=False)
    userName    = Column(String(100), nullable=False)
    

# Client model definition
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