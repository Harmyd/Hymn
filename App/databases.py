from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql_alchemy_database_url ='sqlite:///blog.db'

engine = create_engine(sql_alchemy_database_url,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()