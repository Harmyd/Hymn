from pydantic import BaseModel
from typing import List

class LyricsCreate(BaseModel):
    position:str
    text:str
    type:str
    
class HymnCreate(BaseModel):
    title:str
    lyrics:List[LyricsCreate]


