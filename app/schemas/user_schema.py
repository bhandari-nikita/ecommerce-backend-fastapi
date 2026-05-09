from pydantic import BaseModel, EmailStr

# Schema for user registration request
# Incoming data from client
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema for API response
# Outgoing data sent back to client
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        # Allows Pydantic to convert SQLAlchemy objects into JSON response
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str