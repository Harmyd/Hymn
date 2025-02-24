from fastapi import FastAPI
from .databases import engine
from . import models
from .Routes import hymn
import os

app=FastAPI()

models.Base.metadata.create_all(engine)

port = int(os.environ.get("PORT", "8000"))


database_url=os.environ.get("DATABASE_URL",'sqlite:///blog.db')


@app.get("/")
def read_root():
    return {"message": "welcome"}

app.include_router(hymn.Router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)