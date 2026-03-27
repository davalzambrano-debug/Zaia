from sqlalchemy.orm import Session
from app.models.supplier import Supplier

class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    # Get supplier by ID
    def GetSupplierByID(self, supplierID: int):
        return self.db.query(Supplier).filter(Supplier.supplierID == supplierID).first()

    # Create a new supplier
    def CreateSupplier(self, contactTittle: str, nameSupplier: str, emailSupplier: str, rfcSupplier: str, phoneSupplier: str, addressSupplier: str):
        supplier = Supplier(
            contactTittle=contactTittle,
            nameSupplier=nameSupplier,
            emailSupplier=emailSupplier,
            rfcSupplier=rfcSupplier,
            phoneSupplier=phoneSupplier,
            addressSupplier=addressSupplier
        )
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        return supplier

    # Get all suppliers
    def GetSuppliers(self):
        return self.db.query(Supplier).all()

    # Update supplier
    def UpdateSupplier(self, supplierID: int, data: dict):
        supplier = self.GetSupplierByID(supplierID)
        if supplier:
            for key, value in data.items():
                setattr(supplier, key, value)
            self.db.commit()
            self.db.refresh(supplier)
        return supplier

    # Delete supplier
    def DeleteSupplier(self, supplierID: int):
        supplier = self.GetSupplierByID(supplierID)
        if supplier:
            self.db.delete(supplier)
            self.db.commit()
        return supplier

