from fastapi import FastAPI
from app.db.database import engine, Base
from app.routes import (
    userRoutes,
    productRoutes,
    clientRoutes,
    supplierRoutes,
    salesRoutes,
    creditsRoutes,
    authRoutes
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(userRoutes.router)
app.include_router(productRoutes.router)
app.include_router(clientRoutes.router)
app.include_router(supplierRoutes.router)
app.include_router(salesRoutes.router)
app.include_router(creditsRoutes.router)
app.include_router(authRoutes.router)

@app.get("/")
def root():
    """
    Root endpoint to verify the microservice is running.
    Returns:
        dict: A message indicating the service is running.
    """
    return {"message": "Microservicio corriendo 🚀"}