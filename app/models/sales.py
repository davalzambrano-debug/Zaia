from sqlalchemy import Column, Integer, String, ForeignKey, Double, DateTime
from app.db.database import Base

# Sale header
class Sales(Base):
    __tablename__ = "sales"

    salesID   = Column(Integer, primary_key=True)
    productID = Column(Integer, ForeignKey("products.productID"), nullable=False)
    clientID  = Column(Integer, ForeignKey("client.clientID"), nullable=False)
    userID    = Column(Integer, ForeignKey("users.userID"), nullable=False)
    typeSale  = Column(String(20), nullable=False)   # cash or credit
    totalSale = Column(Double(10, 4), nullable=False)
    dateSale  = Column(DateTime, nullable=False)

# Sale line items
class SalesDetails(Base):
    __tablename__ = "sales_details"

    salesDetailsID = Column(Integer, primary_key=True)
    productID      = Column(Integer, ForeignKey("products.productID"), nullable=False)
    quantity       = Column(Integer, nullable=False)
    size           = Column(String(20), nullable=False)
    price          = Column(Double(10, 4), nullable=False)
    subtotal       = Column(Double(10, 4), nullable=False)  # quantity * price
