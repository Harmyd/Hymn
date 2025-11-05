from sqlalchemy import ForeignKey,Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
from .database import Base


class Hymn(Base):
    __tablename__="hymns"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    composer=Column(String)
    chorus=Column(String)
    lyrics=relationship("lyrics",back_populates="hymns")

class Lyrics(Base):
    __tablename__="lyrics"
    id=Column(Integer,primary_key=True,index=True)
    hymn_id=Column(Integer,ForeignKey("Hymn.id"))
    stanza_number=Column(Integer)
    content=Column(String)
    hymns=relationship(Hymn,back_populates="lyrics")

class Admin(Base):
    __tablename__="admin"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    password=Column(Integer)

