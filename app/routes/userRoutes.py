
# Import FastAPI and dependencies for routing and authentication
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import auth_service
from app.core.security import create_token

# Create an API router with prefix /auth
router = APIRouter(prefix="/auth")

# Dependency to get a database session
def get_db():
    """
    Provides a database session for request lifecycle.
    Yields:
        Session: SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register endpoint
@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    """
    Registers a new user.
    Args:
        email (str): User's email.
        password (str): User's password.
        db (Session): Database session.
    Returns:
        User: The created user object.
    """
    return auth_service.register(db, email, password)

# Login endpoint
@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    """
    Authenticates a user and returns a JWT token if successful.
    Args:
        email (str): User's email.
        password (str): User's password.
        db (Session): Database session.
    Returns:
        dict: Access token if authentication is successful.
    Raises:
        HTTPException: If credentials are invalid.
    """
    user = auth_service.login(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.email})
    return {"access_token": token}
