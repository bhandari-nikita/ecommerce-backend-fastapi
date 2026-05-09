from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.user_schema import (
    UserCreate, 
    UserResponse, 
    UserLogin
    )
from app.utils.security import (
    hash_password, 
    verify_password
    )

router = APIRouter(
    prefix="/users",
    tags=["Users"] # Grouping routes in Swagger documentation. Folders/categories for APIs in docs
)

# User registration endpoint
@router.post("/register", response_model=UserResponse)
def register_user(
        user: UserCreate,
        db: Session = Depends(get_db)
):
    # Check if email already exists
    existing_username = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )
    
    # Hash raw password before saving
    hashed_pw = hash_password(user.password)

    #Create new user object
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


#User Login route
@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    
    #Find user by email
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()
    
    # IF email not found
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    #Verify entered password
    password_correct = verify_password(
        user.password,
        existing_user.hashed_password
    )

    # If password incorrect
    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful"
    }

