from sqlalchemy import Column, Integer, String, ForeignKey, Double, DateTime
from app.db.database import Base

# Credit agreement
class Credits(Base):
    __tablename__ = "credits"

    creditID     = Column(Integer, primary_key=True)
    clientID     = Column(Integer, ForeignKey("client.clientID"), nullable=False)
    salesID      = Column(Integer, ForeignKey("sales.salesID"), nullable=False)
    totalAmount  = Column(Double(10, 4), nullable=False)
    balance      = Column(Double(10, 4), nullable=False)   # remaining to pay
    amountPaid   = Column(Double(10, 4), nullable=False)
    startDate    = Column(DateTime, nullable=False)
    dueDate      = Column(DateTime, nullable=False)
    installments = Column(Integer, nullable=False)
    status       = Column(String(10), nullable=False)      # active, paid, overdue

# Individual payment against a credit
class CreditPayments(Base):
    __tablename__ = "credit_payments"

    paymentID     = Column(Integer, primary_key=True)
    creditID      = Column(Integer, ForeignKey("credits.creditID"), nullable=False)
    amount        = Column(Double(10, 4), nullable=False)
    paymentDate   = Column(DateTime, nullable=False)
    paymentMethod = Column(String(20), nullable=False)  # cash, card, transfer
    notes         = Column(String(255), nullable=True)
