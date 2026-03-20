
# Import Pydantic BaseModel for schema definitions
from pydantic import BaseModel

# Schema for user creation
class UserCreate(BaseModel):
    """
    Schema for creating a new user.
    Attributes:
        email (str): User's email.
        password (str): User's password.
    """
    email: str
    password: str

# Schema for user response
class UserResponse(BaseModel):
    """
    Schema for returning user data in responses.
    Attributes:
        id (int): User's ID.
        email (str): User's email.
    """
    id: int
    email: str

    class Config:
        orm_mode = True  # Enable ORM mode for SQLAlchemy compatibility