from sqlalchemy.orm import Session
from app.models.products import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(Product).all()

    def GetByID(self, productID: int):
        return self.db.query(Product).filter(Product.productID == productID).first()

    def GetBySupplier(self, supplierID: int):
        return self.db.query(Product).filter(Product.supplierID == supplierID).all()

    def GetByStore(self, storeID: int):
        return self.db.query(Product).filter(Product.storeID == storeID).all()

    def GetLowStock(self, threshold: int = 10):
        # Products below stock threshold
        return self.db.query(Product).filter(Product.stock < threshold).all()

    def GetByCode(self, code: str):
        # Check for duplicate code
        return self.db.query(Product).filter(Product.code == code).first()

    def Create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def Update(self, productID: int, data: dict):
        product = self.GetByID(productID)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product

    def Delete(self, productID: int):
        product = self.GetByID(productID)
        if product:
            self.db.delete(product)
            self.db.commit()
        return product
