import os

from dotenv import load_dotenv

from jose import jwt, JWTError
from datetime import datetime, timedelta

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")  # Secret key used to sign JWT tokens
ALGORITHM = "HS256"  # Algorithm used for token signing
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiry time in minutes

# Create JWT access token
def create_access_token(data:dict):
    to_encode = data.copy()  #Copy incoming data

    # Create token expiration time
    expire = datetime.utcnow() + timedelta(  
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Add expiry into token payload
    to_encode.update({
        "exp": expire
    })

    #Generate JWT token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM    # single algorithm string -> "HS256"
    )

    return encoded_jwt

# Verify and decode JWT token
def verify_access_token(token: str):
    try:
        #Decode token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]   # expects LIST of allowed algorithms -> algorithms=["HS256", "RS256"]  -> but here backend says: "Only trust HS256 signed tokens" 
            # present containing one item but for future flexibility
        )

        # Extract user identity from token payload
        email = payload.get("sub")

        # If email missing
        if email is None:
            return None
        
        return email
    
    except JWTError:
        return None


# payload = the data stored inside the JWT token
# Example payload:
"""
{
    "sub": "nikita@example.com",
    "exp": 1750000000
}
"""