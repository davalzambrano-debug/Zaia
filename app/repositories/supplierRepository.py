from sqlalchemy.orm import Session
from app.models.supplier import Supplier

class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(Supplier).all()

    def GetByID(self, supplierID: int):
        return self.db.query(Supplier).filter(Supplier.supplierID == supplierID).first()

    def GetByEmail(self, email: str):
        # Check for duplicate email
        return self.db.query(Supplier).filter(Supplier.emailSupplier == email).first()

    def Create(self, supplier: Supplier):
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        return supplier

    def Update(self, supplierID: int, data: dict):
        supplier = self.GetByID(supplierID)
        if supplier:
            for key, value in data.items():
                setattr(supplier, key, value)
            self.db.commit()
            self.db.refresh(supplier)
        return supplier

    def Delete(self, supplierID: int):
        supplier = self.GetByID(supplierID)
        if supplier:
            self.db.delete(supplier)
            self.db.commit()
        return supplier
