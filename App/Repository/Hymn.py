from fastapi import HTTPException,status
from .. import models
from .. import schemas

from sqlalchemy.orm import Session

 
def add_hymn(request,db:Session):
    createHymn=models.Hymn(Title=request.title)
    db.add(createHymn)
    db.commit() 
    db.refresh(createHymn)

    for lyrics in request.lyrics:
        new_lyrics=models.Lyrics(
            hymn_id=createHymn.id,
            type = lyrics.type,
            text=lyrics.text,
            Position=lyrics.position
        )
        db.add(new_lyrics)
    
    db.commit()

    return createHymn

def Edit_hymn(id:int,request,db:Session):
    #check if the id is available
    Edit_Hymn=db.query(models.Hymn).filter(models.Hymn.id==id).first()
    if not Edit_Hymn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The hymn with the id {id} is not found")
    #check if the Title was given 
    if Edit_hymn.Title:
        Edit_Hymn.Title = request.title
    #loop through the lyrics list 
    for lyrics in request.lyrics:
        #check if the lyrics is already existing in the database
        get_lyrics=db.query(models.Lyrics).filter(models.Lyrics.Position==lyrics.position).first()
        if get_lyrics:
            get_lyrics.text=lyrics.Text
            get_lyrics.position=lyrics.position
        else:
            add_lyrics=models.Lyrics(
                hymn_id=Edit_Hymn.id
                
            )



        
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