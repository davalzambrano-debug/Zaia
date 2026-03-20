# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String, ForeignKey, Double, DateTime
from app.db.database import Base

# Sales model definition
class Sales(Base):
    """
    SQLAlchemy model for the sales table.
    Attributes:
        saleID (int): Primary key.
        productID (int): Foreign key referencing products table.
        clientID (int): Foreign key referencing client table.
        userID (int): Foreign key referencing users table.
        typeSale (str): Type of sale (e.g., 'cash', 'credit').
        totalSale (float): Total amount of the sale.
        dateSale (datetime): Date and time of the sale.
    """
    __tablename__ = "sales"

    salesID   = Column(Integer, primary_key=True)
    productID = Column(Integer, ForeignKey("products.productID"), nullable=False)
    clientID  = Column(Integer, ForeignKey("client.clientID"), nullable=False)
    userID    = Column(Integer, ForeignKey("users.userID"), nullable=False)
    typeSale  = Column(String(20), nullable=False)
    totalSale = Column(Double(10, 4), nullable=False)
    dateSale  = Column(DateTime, nullable=False)

# SalesDetails model definition
class SalesDetails(Base):
    """
    SQLAlchemy model for the sales_details table.
    Attributes:
        detailsID (int): Primary key.
        saleID (int): Foreign key referencing sales table.
        productID (int): Foreign key referencing products table.
        quantity (int): Quantity of the product sold.
        price (float): Price of the product at the time of sale.
    """
    __tablename__ = "sales_details"
    
    salesDetailsID = Column(Integer, primary_key=True)
    productID      = Column(Integer, ForeignKey("products.productID"), nullable=False)
    quantity       = Column(Integer, nullable=False)
    size           = Column(String(20), nullable=False)
    price          = Column(Double(10, 4), nullable=False)
    subtotal       = Column(Double(10, 4), nullable=False)