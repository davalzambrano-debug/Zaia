from sqlalchemy.orm import Session
from app.repositories.creditsRepository import CreditsRepository, CreditPaymentsRepository
from app.schemas.creditsSchema import CreditsCreate, CreditsUpdate, CreditPaymentsCreate, CreditPaymentsUpdate
from app.models.credits import Credits, CreditPayments
from fastapi import HTTPException, status
from datetime import date

class CreditsService:
    def __init__(self, db: Session):
        self.repo = CreditsRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, creditID: int):
        credit = self.repo.GetByID(creditID)
        if not credit:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Credit not found")
        return credit

    def GetByClient(self, clientID: int):
        return self.repo.GetByClient(clientID)

    def GetByStatus(self, status_filter: str):
        valid = ["active", "paid", "overdue"]
        if status_filter not in valid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Status must be one of: {valid}")
        return self.repo.GetByStatus(status_filter)

    def GetOverdue(self, current_date: date):
        return self.repo.GetOverdue(current_date)

    def Create(self, data: CreditsCreate):
        if data.startDate > data.dueDate:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Start date must be before due date")
        if data.installments <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Installments must be greater than 0")
        return self.repo.Create(Credits(**data.model_dump()))

    def Update(self, creditID: int, data: CreditsUpdate):
        self.GetByID(creditID)
        return self.repo.Update(creditID, data.model_dump(exclude_unset=True))

    def Delete(self, creditID: int):
        self.GetByID(creditID)
        return self.repo.Delete(creditID)


class CreditPaymentsService:
    def __init__(self, db: Session):
        self.repo = CreditPaymentsRepository(db)
        self.credits_repo = CreditsRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, paymentID: int):
        payment = self.repo.GetByID(paymentID)
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        return payment

    def GetByCredit(self, creditID: int):
        return self.repo.GetByCredit(creditID)

    def GetByMethod(self, method: str):
        valid = ["cash", "card", "transfer"]
        if method not in valid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Method must be one of: {valid}")
        return self.repo.GetByMethod(method)

    def Create(self, data: CreditPaymentsCreate):
        credit = self.credits_repo.GetByID(data.creditID)
        if not credit:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Credit not found")
        if data.amount <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount must be greater than 0")
        if data.amount > credit.balance:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Amount exceeds remaining balance: {credit.balance}")

        payment = self.repo.Create(CreditPayments(**data.model_dump()))

        # Update credit balance after payment
        new_balance = credit.balance - data.amount
        self.credits_repo.Update(data.creditID, {
            "balance": max(new_balance, 0),
            "amountPaid": credit.amountPaid + data.amount,
            "status": "paid" if new_balance <= 0 else "active"
        })
        return payment

    def Update(self, paymentID: int, data: CreditPaymentsUpdate):
        self.GetByID(paymentID)
        return self.repo.Update(paymentID, data.model_dump(exclude_unset=True))

    def Delete(self, paymentID: int):
        self.GetByID(paymentID)
        return self.repo.Delete(paymentID)
