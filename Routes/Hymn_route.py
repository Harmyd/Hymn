from fastapi import APIRouter,status,Depends
from schemas import Hymn,LyricsCreate
from ..Services.Hymn import add_hymn
from ..database import Session,get_db

HymnRouter=APIRouter(prefix="Hymn")
@HymnRouter.post("/add_hymn",status_code=status.HTTP_200_OK)
def add_Hymn(request:Hymn,db:Session=Depends(get_db)):
    pass