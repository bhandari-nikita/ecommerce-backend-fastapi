# Import required SQLAlchemy tools
from sqlalchemy import Column, Integer, String, Float

from app.db.database import Base

# Product table model
class Product(Base):

    # Table name in PostgreSQL
    __tablename__ = "products"

    # Table columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)