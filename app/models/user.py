from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    userID      = Column(Integer, primary_key=True)
    rol         = Column(String(20), nullable=False, default="user")  # user or admin
    nameUser    = Column(String(255), nullable=False)
    phoneUser   = Column(String(16), nullable=False)
    rfcUser     = Column(String(13), nullable=False)
    addressUser = Column(String(255), nullable=False)
    password    = Column(String(255), nullable=False)  # stored as bcrypt hash
    userName    = Column(String(100), nullable=False)  # used for login
