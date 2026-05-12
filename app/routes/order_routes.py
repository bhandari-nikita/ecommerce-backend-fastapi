from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.order import Order
from app.models.product import Product

from app.schemas.order_schema import OrderCreate

from app.utils.oauth2 import get_current_user


router = APIRouter(
    prefix = "/orders",
    tags = ["Orders"]
)

@router.post("/")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    #Check if product exists
    product = db.query(Product).filter(
        Product.id == order.product_id   #here order.product_id is the product_id from OrderCreate schema, Product.id is the id column in products table
    ).first()

    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    
    #Create new order
    new_order = Order(
        user_id = current_user.id,   #current_user is the user object returned by get_current_user function, current_user.id is the id of the authenticated user
        product_id = order.product_id
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "Order created successfully",
        "order_id": new_order.id,
        "product_id": new_order.product_id,
        "user_id": new_order.user_id
    }