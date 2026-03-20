from sqlalchemy.orm import Session
from app.models.supplier import Supplier

# Get supplier by ID
def GetSupplierByID(db: Session, supplierID: int):
    return db.query(Supplier).filter(Supplier.supplierID == supplierID).first()

# Create a new supplier
def CreateSupplier(db: Session, contactTittle: str, nameSupplier: str, emailSupplier: str, rfcSupplier: str, phoneSupplier: str, addressSupplier: str):
    supplier = Supplier(
        contactTittle=contactTittle,
        nameSupplier=nameSupplier,
        emailSupplier=emailSupplier,
        rfcSupplier=rfcSupplier,
        phoneSupplier=phoneSupplier,
        addressSupplier=addressSupplier
    )
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

# Get all suppliers
def GetSuppliers(db: Session):
    return db.query(Supplier).all()

# Update supplier information
def UpdateSupplier(db: Session, supplierID: int, contactTittle: str = None, nameSupplier: str = None, emailSupplier: str = None, rfcSupplier: str = None, phoneSupplier: str = None, addressSupplier: str = None):
    supplier = GetSupplierByID(db, supplierID)
    if not supplier:
        return None
    if contactTittle:
        supplier.contactTittle = contactTittle
    if nameSupplier:
        supplier.nameSupplier = nameSupplier
    if emailSupplier:
        supplier.emailSupplier = emailSupplier
    if rfcSupplier:
        supplier.rfcSupplier = rfcSupplier
    if phoneSupplier:
        supplier.phoneSupplier = phoneSupplier
    if addressSupplier:
        supplier.addressSupplier = addressSupplier
    db.commit()
    db.refresh(supplier)
    return supplier

# Delete supplier
def DeleteSupplier(db: Session, supplierID: int):
    supplier = GetSupplierByID(db, supplierID)
    if supplier:
        db.delete(supplier)
        db.commit()
    return supplier

