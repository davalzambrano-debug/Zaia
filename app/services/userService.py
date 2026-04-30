from sqlalchemy.orm import Session
from app.repositories.userRepository import UserRepository
from app.schemas.userSchema import UserCreate, UserUpdate
from app.models.user import User
from app.core.security import hash_password
from fastapi import HTTPException, status

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, userID: int):
        user = self.repo.GetByID(userID)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def Create(self, data: UserCreate):
        # Hash password before saving
        new_user = User(
            rol=data.rol,
            nameUser=data.nameUser,
            phoneUser=data.phoneUser,
            rfcUser=data.rfcUser,
            addressUser=data.addressUser,
            password=hash_password(data.password),
            userName=data.userName
        )
        return self.repo.Create(new_user)

    def Update(self, userID: int, data: UserUpdate):
        self.GetByID(userID)
        update_data = data.model_dump(exclude_unset=True)
        if "password" in update_data:
            # Hash new password if updated
            update_data["password"] = hash_password(update_data["password"])
        return self.repo.Update(userID, update_data)

    def Delete(self, userID: int):
        self.GetByID(userID)
        return self.repo.Delete(userID)
