from sqlalchemy.orm import declarative_base,sessionmaker,Session
from sqlalchemy import create_engine
import os

Database_url=os.getenv("DATABASE_URL")
engine= create_engine(Database_url)
sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()