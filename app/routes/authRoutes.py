from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import GetDB
from app.repositories.userRepository import UserRepository
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(GetDB)):
    # Validate credentials and return JWT token
    user = UserRepository(db).get_by_username(form.username)
    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    token = create_access_token(data={"sub": str(user.userID), "rol": user.rol})
    return {"access_token": token, "token_type": "bearer"}
