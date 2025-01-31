from sqlalchemy import Column,Integer,String
from .databases import base


class Hymn(base):
    __tablename__="Hymn"
    id=Column(Integer,primary_key=True,index=True)
    Title = Column(String)
    Content=Column(String)
