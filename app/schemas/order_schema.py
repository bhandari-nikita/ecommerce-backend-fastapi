from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id: int
    #do NOT include "user_id" because authenticated user identity comes from JWT