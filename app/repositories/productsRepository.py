from sqalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create new product
    def CreateProduct(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    # Get all products
    def GetProducts(self):
        return self.db.query(Product).all()
    # Get product by ID
    def GetProductByID(self, productID: int):
        return self.db.query(Product).filter(Product.productID == productID).first()
    # Get product by supplier ID
    def GetProductsBySupplierID(self, supplierID: int):
        return self.db.query(Product).filter(Product.supplierID == supplierID).all()
    # Get product by store ID
    def GetProductsByStoreID(self, storeID: int):
        return self.db.query(Product).filter(Product.storeID == storeID).all()
    
    # Get low stock products
    def GetLowStockProducts(self, threshold: int = 10):
        return self.db.query(Product).filter(Product.stock < threshold).all()
    
    # Update product
    def UpdateProduct(self, productID: int, data: dict):
        product = self.GetProductByID(productID)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product
    
    # Delete product
    def DeleteProduct(self, productID: int):
        product = self.GetProductByID(productID)
        if product:
            self.db.delete(product)
            self.db.commit()
        return product