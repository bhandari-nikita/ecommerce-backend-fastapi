from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.cart import Cart
from app.models.product import Product

from app.schemas.cart_schema import CartCreate

from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix = "/cart",
    tags = ["Cart"]
)

#Add product to cart
@router.post("/")
def add_to_cart(
        cart: CartCreate,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user)
):
    
    #Check if product exists
    product = db.query(Product).filter(
        Product.id == cart.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    
    #Check if product is already in cart
    existing_cart_item = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == cart.product_id
    ).first()

    #If already exists, increase quantity
    if existing_cart_item:
        existing_cart_item.quantity += cart.quantity
        db.commit()
        db.refresh(existing_cart_item)
        return {
            "message": "Cart quantity updated",
            "cart_item": existing_cart_item
        }
    
    #Create new cart item
    new_cart_item = Cart(
        user_id = current_user.id,
        product_id = cart.product_id,
        quantity = cart.quantity
    )
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)
    return {
        "message": "Item added to cart",
        "cart_item": new_cart_item
    }