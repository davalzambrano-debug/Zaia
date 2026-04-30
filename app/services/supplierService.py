from sqlalchemy.orm import Session
from app.repositories.supplierRepository import SupplierRepository
from app.schemas.supplierSchema import SupplierCreate, SupplierUpdate
from app.models.supplier import Supplier
from fastapi import HTTPException, status

class SupplierService:
    def __init__(self, db: Session):
        self.repo = SupplierRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, supplierID: int):
        supplier = self.repo.GetByID(supplierID)
        if not supplier:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
        return supplier

    def Create(self, data: SupplierCreate):
        # Reject duplicate email
        if self.repo.GetByEmail(data.emailSupplier):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        return self.repo.Create(Supplier(**data.model_dump()))

    def Update(self, supplierID: int, data: SupplierUpdate):
        self.GetByID(supplierID)
        return self.repo.Update(supplierID, data.model_dump(exclude_unset=True))

    def Delete(self, supplierID: int):
        self.GetByID(supplierID)
        return self.repo.Delete(supplierID)
