from fastapi import FastAPI
from .databases import engine
from . import models
from .Routes import hymn

app=FastAPI()

models.base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hymn API"}

app.include_router(hymn.Router)