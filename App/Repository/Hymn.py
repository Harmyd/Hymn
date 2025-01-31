from fastapi import HTTPException,status
from .. import models
from .. import schemas

from sqlalchemy.orm import Session

 
def add_hymn(request,db:Session):
    createHymn=models.Hymn(Title=request.title,Content=request.content)
    db.add(createHymn)
    db.commit() 
    db.refresh(createHymn)
    return createHymn

def Edit_hymn(id:int,request,db:Session):
    Edit_Hymn=db.query(models.Hymn).filter(models.Hymn.id==id).first()
    if not Edit_Hymn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The hymn with the id {id} is not found")
    Edit_Hymn.Title = request.title
    Edit_Hymn.Content=request.content
    db.commit()
    db.refresh(Edit_Hymn)
    return "Updated"


def delete_Hymn(id,db:Session):
    Delete_hymn=db.query(models.Hymn).filter(models.Hymn.id==id).first()
    if not Delete_hymn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The hymn with {id} does not exist")
    Delete_hymn.delete(synchronize_session=False)
    db.commit()
    return "Done"