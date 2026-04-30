from sqlalchemy.orm import Session
from app.models.credits import Credits, CreditPayments

class CreditsRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(Credits).all()

    def GetByID(self, creditID: int):
        return self.db.query(Credits).filter(Credits.creditID == creditID).first()

    def GetByClient(self, clientID: int):
        return self.db.query(Credits).filter(Credits.clientID == clientID).all()

    def GetByStatus(self, status: str):
        # active, paid or overdue
        return self.db.query(Credits).filter(Credits.status == status).all()

    def GetOverdue(self, current_date):
        # Past due date and still active
        return self.db.query(Credits).filter(
            Credits.dueDate < current_date,
            Credits.status == "active"
        ).all()

    def Create(self, credit: Credits):
        self.db.add(credit)
        self.db.commit()
        self.db.refresh(credit)
        return credit

    def Update(self, creditID: int, data: dict):
        credit = self.GetByID(creditID)
        if credit:
            for key, value in data.items():
                setattr(credit, key, value)
            self.db.commit()
            self.db.refresh(credit)
        return credit

    def Delete(self, creditID: int):
        credit = self.GetByID(creditID)
        if credit:
            self.db.delete(credit)
            self.db.commit()
        return credit


class CreditPaymentsRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(CreditPayments).all()

    def GetByID(self, paymentID: int):
        return self.db.query(CreditPayments).filter(CreditPayments.paymentID == paymentID).first()

    def GetByCredit(self, creditID: int):
        return self.db.query(CreditPayments).filter(CreditPayments.creditID == creditID).all()

    def GetByMethod(self, method: str):
        return self.db.query(CreditPayments).filter(CreditPayments.paymentMethod == method).all()

    def Create(self, payment: CreditPayments):
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def Update(self, paymentID: int, data: dict):
        payment = self.GetByID(paymentID)
        if payment:
            for key, value in data.items():
                setattr(payment, key, value)
            self.db.commit()
            self.db.refresh(payment)
        return payment

    def Delete(self, paymentID: int):
        payment = self.GetByID(paymentID)
        if payment:
            self.db.delete(payment)
            self.db.commit()
        return payment
