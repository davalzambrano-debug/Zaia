from fastapi import FastAPI
from app.db.database import engine, Base

# Import all models before create_all to resolve foreign keys
from app.models.user import User
from app.models.clients import Client
from app.models.supplier import Supplier
from app.models.stores import Store
from app.models.products import Product
from app.models.sales import Sales, SalesDetails
from app.models.credits import Credits, CreditPayments

from app.routes import (
    userRoutes, productsRoutes, clientRoutes,
    supplierRoutes, authRoutes, storeRoutes
)
from app.routes.salesRoutes import router as salesRouter, routerSalesDetails
from app.routes.creditsRoutes import router as creditsRouter, routerCreditPayments

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sales Point API")

# Register all routers
app.include_router(authRoutes.router)
app.include_router(userRoutes.router)
app.include_router(productsRoutes.router)
app.include_router(clientRoutes.router)
app.include_router(supplierRoutes.router)
app.include_router(storeRoutes.router)
app.include_router(salesRouter)
app.include_router(routerSalesDetails)
app.include_router(creditsRouter)
app.include_router(routerCreditPayments)

@app.get("/")
def root():
    return {"message": "Microservicio corriendo"}
