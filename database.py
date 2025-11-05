from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

engine= create_engine()
sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()