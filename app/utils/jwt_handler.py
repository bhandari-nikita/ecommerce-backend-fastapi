from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"  # Secret key used to sign JWT tokens
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
        algorithm=ALGORITHM
    )

    return encoded_jwt
