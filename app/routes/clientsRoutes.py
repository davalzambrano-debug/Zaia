from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import GetDB
from schemas.clientsSchema import ClientCreate, ClientUpdate
from services.client_services import ClientService
from core.security import get_current_user

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.get("/")
def GetAll(db: Session = Depends(GetDB)):
    return ClientService(db).GetAll()

@router.get("/{clientID}")
def GetByID(clientID: int, db: Session = Depends(GetDB)):
    return ClientService(db).GetByID(clientID)

@router.post("/")
def Create(data: ClientCreate, db: Session = Depends(GetDB)):
    return ClientService(db).Create(data)

@router.put("/{clientID}")
def Update(clientID: int, data: ClientUpdate, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return ClientService(db).Update(clientID, data)

@router.delete("/{clientID}")
def Delete(clientID: int, db: Session = Depends(GetDB),
           current_user=Depends(get_current_user)):
    return ClientService(db).Delete(clientID)