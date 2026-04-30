from sqlalchemy.orm import Session
from app.repositories.clientRepository import ClientRepository
from app.schemas.clientsSchema import ClientCreate, ClientUpdate
from app.models.clients import Client
from fastapi import HTTPException, status

class ClientService:
    def __init__(self, db: Session):
        self.repo = ClientRepository(db)

    def GetAll(self):
        return self.repo.GetAll()

    def GetByID(self, clientID: int):
        client = self.repo.GetByID(clientID)
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        return client

    def Create(self, data: ClientCreate):
        # Reject duplicate email
        if self.repo.GetByEmail(data.emailClient):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        return self.repo.Create(Client(**data.model_dump()))

    def Update(self, clientID: int, data: ClientUpdate):
        self.GetByID(clientID)
        return self.repo.Update(clientID, data.model_dump(exclude_unset=True))

    def Delete(self, clientID: int):
        self.GetByID(clientID)
        return self.repo.Delete(clientID)
