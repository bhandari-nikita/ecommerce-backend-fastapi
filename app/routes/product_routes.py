from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.db.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.utils.oauth2 import (
    get_current_user,
    admin_only
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_only)
):
    # Create new product instance here product.name, product.price, product.stock represents the data sent in the request body and validated by the ProductCreate schema
    # while name, price, stock are the columns in the products table in the database
    new_product = Product(
        name = product.name,
        price = product.price,
        stock = product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/", response_model=list[ProductResponse], summary="Get All Products")
def get_products(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):  
    #Fetch all products
    products = db.query(Product).all()

    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_single_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    # Find product by ID
    product = db.query(Product).filter(Product.id == product_id).first()

    # If product not found
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    updated_product: ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_only)
):
    
    # Find existing product
    product = db.query(Product).filter(Product.id == product_id).first()

    #If not found
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    #Update fields
    product.name = updated_product.name
    product.price = updated_product.price
    product.stock = updated_product.stock

    db.commit()
    db.refresh(product)

    return product

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_only)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}