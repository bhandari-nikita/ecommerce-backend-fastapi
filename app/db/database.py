from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.product import Base

DATABASE_URL = "postgresql://postgres:niky1859@localhost:5432/ecommerce"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create all tables from models
Base.metadata.create_all(bind=engine)