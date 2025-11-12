from fastapi import FastAPI
from .database import Base,engine
import os


Base.metadata.create_all(engine)
port=int(os.environ.get("PORT","8000"))

app = FastAPI()
app.get("/")
def index():
    return {"data":"Hymn api"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=port)