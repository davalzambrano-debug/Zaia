from sqlalchemy.orm import Session
from app.models.user import User


# Get user by email
def GetUserByEmail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Create a new user
def CreateUser(db: Session, email: str, password: str):
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Get all users
def GetUsers(db: Session):
    return db.query(User).all()

# Get user by ID
def GetUserByID(db: Session, userID: int):
    return db.query(User).filter(User.id == userID).first()

# Update user information
def UpdateUser(db: Session, userID: int, password: str = None):
    user = GetUserByID(db, userID)
    if not user:
        return None
    elif password:
        user.password = password
    db.commit()
    db.refresh(user)
    return user

# Delete user
def DeleteUser(db: Session, userID: int):
    user = GetUserByID(db, userID)
    if user:
        db.delete(user)
        db.commit()
    return user