from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(User).all()

    def GetByID(self, userID: int):
        return self.db.query(User).filter(User.userID == userID).first()

    def GetByEmail(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, userID: int):
        # Alias used by security.py
        return self.GetByID(userID)

    def get_by_username(self, username: str):
        # Used on login
        return self.db.query(User).filter(User.userName == username).first()

    def Create(self, user: User):
        # Save new user
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def Update(self, userID: int, data: dict):
        user = self.GetByID(userID)
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def Delete(self, userID: int):
        user = self.GetByID(userID)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user
