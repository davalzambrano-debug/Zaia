
# Import necessary modules for user services
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password

# Register a new user in the database
def register(db: Session, email: str, password: str):
    """
    Registers a new user with hashed password.
    Args:
        db (Session): Database session.
        email (str): User's email.
        password (str): User's plain password.
    Returns:
        User: The created user object.
    """
    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Authenticate a user by email and password
def login(db: Session, email: str, password: str):
    """
    Authenticates a user by verifying email and password.
    Args:
        db (Session): Database session.
        email (str): User's email.
        password (str): User's plain password.
    Returns:
        User or None: The user object if authentication is successful, otherwise None.
    """
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user