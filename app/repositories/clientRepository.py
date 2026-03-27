from sqlalchemy.orm import Session
from models.clients import Client

class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, client: Client):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def GetAll(self):
        return self.db.query(Client).all()

    def GetByID(self, clientID: int):
        return self.db.query(Client).filter(Client.clientID == clientID).first()

    def GetByEmail(self, email: str):
        return self.db.query(Client).filter(Client.emailClient == email).first()

    def GetByRFC(self, rfc: str):
        return self.db.query(Client).filter(Client.rfcClient == rfc).first()

    def Update(self, clientID: int, data: dict):
        client = self.GetByID(clientID)
        if client:
            for key, value in data.items():
                setattr(client, key, value)
            self.db.commit()
            self.db.refresh(client)
        return client

    def Delete(self, clientID: int):
        client = self.GetByID(clientID)
        if client:
            self.db.delete(client)
            self.db.commit()
        return client