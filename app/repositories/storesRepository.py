from sqlalchemy.orm import Session
from app.models.stores import Store

class StoreRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create Store
    def CreateStore(self, nameStore: str, addressStore: str, phoneStore: str):
        store = Store(nameStore=nameStore, addressStore=addressStore, phoneStore=phoneStore)
        self.db.add(store)
        self.db.commit()
        self.db.refresh(store)
        return store

    # Get all Stores
    def GetStores(self):
        return self.db.query(Store).all()
    
    # Get Store by ID
    def GetStoreByID(self, storeID: int):
        return self.db.query(Store).filter(Store.storeID == storeID).first()

    # Update Store
    def UpdateStore(self, storeID: int, data: dict):
        store = self.GetStoreByID(storeID)
        if store:
            for key, value in data.items():
                setattr(store, key, value)
            self.db.commit()
            self.db.refresh(store)
        return store

    # Delete Store
    def DeleteStore(self, storeID: int):
        store = self.GetStoreByID(storeID)
        if store:
            self.db.delete(store)
            self.db.commit()
        return store