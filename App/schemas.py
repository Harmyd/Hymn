from pydantic import BaseModel

class HymnCreate(BaseModel):
    title:str
    content:str


