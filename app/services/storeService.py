from sqlalchemy.orm import Session
from app.repositories.storesRepository import StoreRepository
from app.schemas.storeSchema import StoreCreate, StoreUpdate
from app.models.stores import Store
from fastapi import HTTPException, status

class StoreService:
    def __init__(self, db: Session):
        self.repo = StoreRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, storeID: int):
        store = self.repo.GetByID(storeID)
        if not store:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Store not found")
        return store

    def Create(self, data: StoreCreate):
        return self.repo.Create(Store(**data.model_dump()))

    def Update(self, storeID: int, data: StoreUpdate):
        self.GetByID(storeID)
        return self.repo.Update(storeID, data.model_dump(exclude_unset=True))

    def Delete(self, storeID: int):
        self.GetByID(storeID)
        return self.repo.Delete(storeID)
