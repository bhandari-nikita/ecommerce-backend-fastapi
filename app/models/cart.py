from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

class Cart(Base):
    __tablename__ = "carts"

    id = Column (
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column (
        Integer,
        ForeignKey("users.id")
    )

    product_id = Column (
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column (
        Integer,
        default=1
    )

    user = relationship("User") # this creates a relationship between the Cart and User models, allowing us to access the user associated with a cart item using cart.user
    product = relationship("Product")