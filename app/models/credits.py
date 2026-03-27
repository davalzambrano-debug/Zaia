# Import SQLAlchemy components for model definition
from sqlalchemy import Column, Integer, String, ForeignKey, Double, DateTime
from app.db.database import Base

# Credits model definition
class Credits(Base):
    """
    SQLAlchemy model for the credits table.
    Attributes:
        creditID (int): Primary key.
        saleID (int): Foreign key referencing sales table.
        clientID (int): Foreign key referencing client table.
        userID (int): Foreign key referencing users table.
        totalCredit (float): Total amount of the credit.
        dateCredit (datetime): Date and time of the credit.
    """
    __tablename__ = "credits"

    creditID     = Column(Integer, primary_key=True)
    clientID     = Column(Integer, ForeignKey("client.clientID"), nullable=False)
    salesID       = Column(Integer, ForeignKey("sales.salesID"), nullable=False)
    totalAmount  = Column(Double(10, 4), nullable=False)
    balance      = Column(Double(10, 4), nullable=False)
    amountPaid   = Column(Double(10, 4), nullable=False)
    startDate    = Column(DateTime, nullable=False)
    dueDate      = Column(DateTime, nullable=False)
    installments = Column(Integer, nullable=False)
    status       = Column(String(10), nullable=False)


# CreditPayments model definition
class CreditPayments(Base):
    """
    SQLAlchemy model for the credit_payments table.
    Attributes:
        paymentID (int): Primary key.
        creditID (int): Foreign key referencing credits table.
        amount (float): Amount of the payment.
        paymentDate (datetime): Date and time of the payment.
        paymentMethod (str): Method of payment (e.g., 'cash', 'card').
    """
    __tablename__ = "credit_payments"

    paymentID     = Column(Integer, primary_key=True)
    creditID      = Column(Integer, ForeignKey("credits.creditID"), nullable=False)
    amount        = Column(Double(10, 4), nullable=False)
    paymentDate   = Column(DateTime, nullable=False)
    paymentMethod = Column(String(20), nullable=False)
    notes         = Column(String(255), nullable=True)