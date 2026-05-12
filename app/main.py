import app.models

from fastapi import FastAPI

from app.db.database import Base, engine

from app.routes.product_routes import router as product_router
from app.routes.user_routes import router as user_router
from app.routes.order_routes import router as order_router
from app.routes.cart_routes import router as cart_router

# Create all tables from models
Base.metadata.create_all(bind=engine)  

app = FastAPI()

app.include_router(product_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(cart_router)

@app.get("/")
def home():
    return {"message": "Ecommerce Backend API Running"}

#router file = blueprint
#include_router = connect blueprint to app