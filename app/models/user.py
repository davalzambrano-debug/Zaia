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