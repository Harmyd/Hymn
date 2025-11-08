from fastapi import FastAPI
from .database import Base,engine


Base.metadata.create_all(engine)
app = FastAPI()
app.get("/")
def index():
    return {"data":"Hymn api"}