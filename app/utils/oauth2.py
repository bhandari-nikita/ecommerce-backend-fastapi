from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.utils.jwt_handler import verify_access_token
from app.models.user import User

# Extract brearer token from request
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)

# Get currently authenticated user
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    # Verify JWT token
    email = verify_access_token(token)

    # If token in valid or expired
    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    # Find user in database
    user = db.query(User).filter(
        User.email == email
    ).first()

    # If user not found
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return user


# Check if current user is admin
def admin_only(
        current_user = Depends(get_current_user)
):
    #If user is not admin
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return current_user























#OAuth2 is an authorization framework
#Bearer means: "whoever possesses this token can use it"