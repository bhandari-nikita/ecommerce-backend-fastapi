from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.models.product import Product
from app.db.database import get_db

from app.schemas.product_schema import ProductCreate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server running"}

@app.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
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

    return {
        "message": "Product created",
        "product": {
            "id": new_product.id,
            "name": new_product.name,
            "price": new_product.price,
            "stock": new_product.stock
        }
    }

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    
    #Fetch all products
    products = db.query(Product).all()

    return products

@app.get("/products/{product_id}")
def get_single_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    # Find product by ID
    product = db.query(Product).filter(Product.id == product_id).first()

    # If product not found
    if not product:
        return {"message": "Product not found"}
    
    return product

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    updated_product: ProductCreate,
    db: Session = Depends(get_db)
):
    
    # Find existing product
    product = db.query(Product).filter(Product.id == product_id).first()

    #If not found
    if not product:
        return {"message": "Product not found"}
    
    #Update fields
    product.name = updated_product.name
    product.price = updated_product.price
    product.stock = updated_product.stock

    db.commit()
    db.refresh(product)

    return {
        "message": "Product updated",
        "product": product
    }

@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"message": "Product not found"}
    
    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}