from sqlalchemy.orm import Session
from app.models.sales import Sales, SalesDetails

class SalesRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(Sales).all()

    def GetByID(self, salesID: int):
        return self.db.query(Sales).filter(Sales.salesID == salesID).first()

    def GetByUser(self, userID: int):
        return self.db.query(Sales).filter(Sales.userID == userID).all()

    def GetByClient(self, clientID: int):
        return self.db.query(Sales).filter(Sales.clientID == clientID).all()

    def GetByType(self, typeSale: str):
        return self.db.query(Sales).filter(Sales.typeSale == typeSale).all()

    def GetByDateRange(self, startDate, endDate):
        # Filter sales between two dates
        return self.db.query(Sales).filter(
            Sales.dateSale >= startDate,
            Sales.dateSale <= endDate
        ).all()

    def Create(self, sale: Sales):
        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)
        return sale

    def Update(self, salesID: int, data: dict):
        sale = self.GetByID(salesID)
        if sale:
            for key, value in data.items():
                setattr(sale, key, value)
            self.db.commit()
            self.db.refresh(sale)
        return sale

    def Delete(self, salesID: int):
        sale = self.GetByID(salesID)
        if sale:
            self.db.delete(sale)
            self.db.commit()
        return sale


class SalesDetailsRepository:
    def __init__(self, db: Session):
        self.db = db

    def GetAll(self):
        return self.db.query(SalesDetails).all()

    def GetByID(self, salesDetailsID: int):
        return self.db.query(SalesDetails).filter(SalesDetails.salesDetailsID == salesDetailsID).first()

    def GetByProduct(self, productID: int):
        return self.db.query(SalesDetails).filter(SalesDetails.productID == productID).all()

    def Create(self, detail: SalesDetails):
        self.db.add(detail)
        self.db.commit()
        self.db.refresh(detail)
        return detail

    def Update(self, salesDetailsID: int, data: dict):
        detail = self.GetByID(salesDetailsID)
        if detail:
            for key, value in data.items():
                setattr(detail, key, value)
            self.db.commit()
            self.db.refresh(detail)
        return detail

    def Delete(self, salesDetailsID: int):
        detail = self.GetByID(salesDetailsID)
        if detail:
            self.db.delete(detail)
            self.db.commit()
        return detail
