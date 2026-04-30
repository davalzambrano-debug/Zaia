from sqlalchemy.orm import Session
from app.models.stores import Store

class StoreRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(Store).all()

    def GetByID(self, storeID: int):
        return self.db.query(Store).filter(Store.storeID == storeID).first()

    def Create(self, store: Store):
        self.db.add(store)
        self.db.commit()
        self.db.refresh(store)
        return store

    def Update(self, storeID: int, data: dict):
        store = self.GetByID(storeID)
        if store:
            for key, value in data.items():
                setattr(store, key, value)
            self.db.commit()
            self.db.refresh(store)
        return store

    def Delete(self, storeID: int):
        store = self.GetByID(storeID)
        if store:
            self.db.delete(store)
            self.db.commit()
        return store
