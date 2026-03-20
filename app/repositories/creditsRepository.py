from sqlalchemy.orm import Session
from app.models.credits import Credits, CreditsPayments

class CreditsRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create a new credit entry
    def CreateCredit(self, credit: Credits):
        self.db.add(credit)
        self.db.commit()
        self.db.refresh(credit)
        return credit

    # Get a credit entry by ID
    def GetCreditByID(self, creditID: int):
        return self.db.query(Credits).filter(Credits.creditID == creditID).first()
    # Get all credit entries
    def GetAllCredits(self):
        return self.db.query(Credits).all()
    # Get credit by client ID
    def GetCreditsByClientID(self, clientID: int):
        return self.db.query(Credits).filter(Credits.clientID == clientID).all()

    # Get Overdue credits
    def GetOverdueCredits(self, current_date):
        return self.db.query(Credits).filter(Credits.dueDate < current_date, Credits.status == 'active').all()

    # Update a credit entry    
    def UpdateCredit(self, creditID: int, data: dict):
        credit = self.GetCreditByID(creditID)
        if credit:
            for key, value in data.items():
                setattr(credit, key, value)
            self.db.commit()
            self.db.refresh(credit)
        return credit

    # Delete a credit entry
    def DeleteCredit(self, creditID: int):
        credit = self.GetCreditByID(creditID)
        if credit:
            self.db.delete(credit)
            self.db.commit()
        return credit

class CreditPaymentsRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create a new credit payment entry
    def CreateCreditPayment(self, payment: CreditsPayments):
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    # Get all
    def GetAllCreditPayments(self):
        return self.db.query(CreditsPayments).all()
    # Get credit payment by ID
    def GetCreditPaymentByID(self, paymentID: int):
        return self.db.query(CreditsPayments).filter(CreditsPayments.paymentID == paymentID).first()
    # Get credit payments by credit ID
    def GetCreditPaymentsByCreditID(self, creditID: int):
        return self.db.query(CreditsPayments).filter(CreditsPayments.creditID == creditID).all()

    # Update a credit payment 
    def UpdateCreditPayment(self, paymentID: int, data: dict):
        payment = self.GetCreditPaymentByID(paymentID)
        if payment:
            for key, value in data.items():
                setattr(payment, key, value)
            self.db.commit()
            self.db.refresh(payment)
        return payment

    # Delete a credit payment entry
    def DeleteCreditPayment(self, paymentID: int):
        payment = self.GetCreditPaymentByID(paymentID)
        if payment:
            self.db.delete(payment)
            self.db.commit()
        return payment