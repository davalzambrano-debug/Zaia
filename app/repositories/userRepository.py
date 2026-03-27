from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:  
    def __init__(self, db: Session):
        self.db = db

    # Get user by email
    def GetUserByEmail(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    # Create a new user
    def CreateUser(self, email: str, password: str):
        user = User(email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    # Get all users
    def GetUsers(self):
        return self.db.query(User).all()

    # Get user by ID
    def GetUserByID(self, userID: int):
        return self.db.query(User).filter(User.id == userID).first()
    
    # Get by username
    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.userName == username).first()

    # Update user information
    def UpdateUser(self, userID: int, password: str = None):
        user = self.GetUserByID(userID)
        if not user:
            return None
        elif password:
            user.password = password
        self.db.commit()
        self.db.refresh(user)
        return user

    # Delete user
    def DeleteUser(self, userID: int):
        user = self.GetUserByID(userID)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user