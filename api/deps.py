import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DSN = os.getenv("POSTGRES_DSN","postgresql+psycopg://dg:dgpass@postgres:5432/deepgrocer")
engine = create_engine(DSN, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
