from sqlalchemy.orm import declarative_base,sessionmaker,Session
from sqlalchemy import create_engine

engine= create_engine("postgresql://hymn_db_ka5j_user:2ksXOMXL2N6aH27GWbSJzVBuBx1RmVA0@dpg-d45s4okhg0os73e68n90-a.oregon-postgres.render.com/hymn_db_ka5j")
sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()