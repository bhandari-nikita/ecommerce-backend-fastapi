# Import required SQLAlchemy tools
from sqlalchemy import Column, Integer, String, Float

# Import base class for models
from sqlalchemy.orm import declarative_base


# Create base class
Base = declarative_base()

# Product table model
class Product(Base):

    # Table name in PostgreSQL
    __tablename__ = "products"

    # Table columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)