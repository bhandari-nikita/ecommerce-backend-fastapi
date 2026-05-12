from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:niky1859@localhost:5432/ecommerce"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)

""" This is the parent class for ALL models.
Example: Product(Base), User(Base)
Without this SQLAlchemy cannot recognize models. """
Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



