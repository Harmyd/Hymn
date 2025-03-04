from fastapi import FastAPI
from .databases import engine
from . import models
from .Routes import hymn
import os

app=FastAPI()

models.Base.metadata.create_all(engine)

port = int(os.environ.get("PORT", "8000"))


@app.get("/")
def read_root():
    return {"message": "welcome"}

app.include_router(hymn.Router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)