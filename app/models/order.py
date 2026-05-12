from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Link order to user
    user_id = Column (
        Integer,
        ForeignKey("users.id")
    )

    # Link order to product
    product_id = Column (
        Integer,
        ForeignKey("products.id")
    )

    #Relationships
    user = relationship("User")   # here user is variable name, "User" is the class name in user.py
    product = relationship("Product")