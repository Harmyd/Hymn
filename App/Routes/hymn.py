from fastapi import FastAPI,status,HTTPException,Depends,APIRouter
from ..databases import SessionLocal,engine,get_db
from sqlalchemy.orm import Session
from .. import schemas,models
from ..Repository import Hymn

Router=APIRouter(
    prefix='/hymn',
    tags=['Hymn']
)

@Router.post('/',status_code=status.HTTP_201_CREATED)
def add_hymn(request:schemas.HymnCreate,db:Session=Depends(get_db)):
    result= Hymn.add_hymn(request,db)
    return {
        "received_data": request.model_dump(),  # Confirm what was received
        "database_saved": result  # Confirm if it was saved
    }
    

@Router.put('/{id}',status_code=status.HTTP_200_OK)
def edit_hymn(id,request:schemas.HymnCreate,db:Session=Depends(get_db)):
   return Hymn.Edit_hymn(id,request,db)


@Router.delete('/{id}',status_code=status.HTTP_200_OK)
def delete(id,db:Session=Depends(get_db)):
    return Hymn.delete_Hymn(id,db)