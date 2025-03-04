from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql_alchemy_database_url ='postgresql://hymn:Mgp8soPw9WsAwWVGW2EFHjxKO7gXy4wb@dpg-cv3m1qvnoe9s738mm5sg-a.oregon-postgres.render.com/hymn_db'

engine = create_engine(sql_alchemy_database_url)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base= declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()