from pydantic import BaseModel
from typing import Optional,List

class LyricsCreate(BaseModel):
    stanzas_number:Optional[int]=None
    content:str

class Hymn(BaseModel):
    title:str
    composer:str
    chorus:Optional[str]=None
    lyrics:List[LyricsCreate]

class Admin(BaseModel):
    pass