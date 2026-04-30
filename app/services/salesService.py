from sqlalchemy.orm import Session
from app.repositories.salesRepository import SalesRepository, SalesDetailsRepository
from app.schemas.salesSchema import SalesCreate, SalesUpdate, SalesDetailsCreate, SalesDetailsUpdate
from app.models.sales import Sales, SalesDetails
from fastapi import HTTPException, status
from datetime import date

class SalesService:
    def __init__(self, db: Session):
        self.repo = SalesRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, salesID: int):
        sale = self.repo.GetByID(salesID)
        if not sale:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
        return sale

    def GetByUser(self, userID: int):
        return self.repo.GetByUser(userID)

    def GetByClient(self, clientID: int):
        return self.repo.GetByClient(clientID)

    def GetByDateRange(self, start: date, end: date):
        if start > end:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Start date must be before end date")
        return self.repo.GetByDateRange(start, end)

    def Create(self, data: SalesCreate):
        return self.repo.Create(Sales(**data.model_dump()))

    def Update(self, salesID: int, data: SalesUpdate):
        self.GetByID(salesID)
        return self.repo.Update(salesID, data.model_dump(exclude_unset=True))

    def Delete(self, salesID: int):
        self.GetByID(salesID)
        return self.repo.Delete(salesID)


class SalesDetailsService:
    def __init__(self, db: Session):
        self.repo = SalesDetailsRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, salesDetailsID: int):
        detail = self.repo.GetByID(salesDetailsID)
        if not detail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sales detail not found")
        return detail

    def GetByProduct(self, productID: int):
        return self.repo.GetByProduct(productID)

    def Create(self, data: SalesDetailsCreate):
        # quantity and price must be positive
        if data.quantity <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantity must be greater than 0")
        if data.price <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Price must be greater than 0")
        return self.repo.Create(SalesDetails(**data.model_dump()))

    def Update(self, salesDetailsID: int, data: SalesDetailsUpdate):
        self.GetByID(salesDetailsID)
        return self.repo.Update(salesDetailsID, data.model_dump(exclude_unset=True))

    def Delete(self, salesDetailsID: int):
        self.GetByID(salesDetailsID)
        return self.repo.Delete(salesDetailsID)
