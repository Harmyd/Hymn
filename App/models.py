from sqlalchemy import Column,Integer,String,ForeignKey
from .databases import base
from sqlalchemy.orm import relationship


class Hymn(base):
    __tablename__="Hymn"
    id=Column(Integer,primary_key=True,index=True)
    Title = Column(String)

    lyrics = relationship("Lyrics",back_populates="Hymn")



class Lyrics(base):
    __tablename__="Lyrics"
    id=Column(Integer,primary_key=True,index=True)
    hymn_id=Column(Integer,ForeignKey("Hymn.id"))
    type=Column(String)
    text=Column(String,nullable=False)
    Position=Column(Integer,nullable=False)

    Hymn=relationship("Hymn",back_populates="Lyrics")


