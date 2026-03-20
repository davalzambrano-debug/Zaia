from fastapi import FastAPI
from app.db.database import engine, Base
from app.routes import auth_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)

@app.get("/")
def root():
    """
    Root endpoint to verify the microservice is running.
    Returns:
        dict: A message indicating the service is running.
    """
    return {"message": "Microservicio corriendo 🚀"}