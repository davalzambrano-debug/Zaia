from sqlalchemy.orm import Session
from app.models.sales import Sales, SalesDetails

class SalesRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create new sale
    def CreateSale(self, sale: Sales):
        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)
        return sale

    # Get all sales
    def GetSales(self):
        return self.db.query(Sales).all()
    # Get sale by ID
    def GetSaleByID(self, saleID: int):
        return self.db.query(Sales).filter(Sales.saleID == saleID).first()
    # Get sales by user ID
    def GetSalesByUserID(self, userID: int):
        return self.db.query(Sales).filter(Sales.userID == userID).all()
    # Get sales by client
    def GetSalesByClientID(self, clientID: int):
        return self.db.query(Sales).filter(Sales.clientID == clientID).all()
    # Get sales by type
    def GetSalesByType(self, saleType: str):
        return self.db.query(Sales).filter(Sales.saleType == saleType).all()
    # Get sales by date range
    def GetSalesByDateRange(self, startDate: str, endDate: str):
        return self.db.query(Sales).filter(Sales.saleDate >= startDate, Sales.saleDate <= endDate).all()

    # Update sale
    def UpdateSale(self, saleID: int, data: dict):
        sale = self.GetSaleByID(saleID)
        if sale:
            for key, value in data.items():
                setattr(sale, key, value)
            self.db.commit()
            self.db.refresh(sale)
        return sale

    # Delete sale
    def DeleteSale(self, saleID: int):
        sale = self.GetSaleByID(saleID)
        if sale:
            self.db.delete(sale)
            self.db.commit()
        return sale

class SalesDetailsRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create new sale detail
    def CreateSaleDetail(self, saleDetail: SalesDetails):
        self.db.add(saleDetail)
        self.db.commit()
        self.db.refresh(saleDetail)
        return saleDetail

    # Get all sale details
    def GetSaleDetails(self):
        return self.db.query(SalesDetails).all()
    # Get sale details by sale ID
    def GetSaleDetailsBySaleID(self, saleID: int):
        return self.db.query(SalesDetails).filter(SalesDetails.saleID == saleID).all()
    # Get sale details by product ID
    def GetSaleDetailsByProductID(self, productID: int):
        return self.db.query(SalesDetails).filter(SalesDetails.productID == productID).all()
    
    # Update sale detail
    def UpdateSaleDetail(self, saleDetailID: int, data: dict):
        saleDetail = self.db.query(SalesDetails).filter(SalesDetails.saleDetailID == saleDetailID).first()
        if saleDetail:
            for key, value in data.items():
                setattr(saleDetail, key, value)
            self.db.commit()
            self.db.refresh(saleDetail)
        return saleDetail

    # Delete sale detail
    def DeleteSaleDetail(self, saleDetailID: int):
        saleDetail = self.db.query(SalesDetails).filter(SalesDetails.saleDetailID == saleDetailID).first()
        if saleDetail:
            self.db.delete(saleDetail)
            self.db.commit()
        return saleDetail