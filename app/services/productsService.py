from sqlalchemy.orm import Session
from app.repositories.productsRepository import ProductRepository
from app.schemas.productsSchema import ProductCreate, ProductUpdate
from app.models.products import Product
from fastapi import HTTPException, status

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, productID: int):
        product = self.repo.GetByID(productID)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return product

    def GetBySupplier(self, supplierID: int):
        return self.repo.GetBySupplier(supplierID)

    def GetByStore(self, storeID: int):
        return self.repo.GetByStore(storeID)

    def GetLowStock(self, threshold: int = 10):
        return self.repo.GetLowStock(threshold)

    def Create(self, data: ProductCreate):
        # Reject duplicate product code
        if self.repo.GetByCode(data.code):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product code already exists")
        return self.repo.Create(Product(**data.model_dump()))

    def Update(self, productID: int, data: ProductUpdate):
        self.GetByID(productID)
        return self.repo.Update(productID, data.model_dump(exclude_unset=True))

    def Delete(self, productID: int):
        self.GetByID(productID)
        return self.repo.Delete(productID)
