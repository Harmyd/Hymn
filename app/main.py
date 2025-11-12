from fastapi import FastAPI
from app.database import Base,engine
import os

print("Creating tables...")
Base.metadata.create_all(engine)
print("Database Created")
port=int(os.environ.get("PORT","8000"))

app = FastAPI()
app.get("/")
def index():
    return {"data":"Hymn api"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=port)