from passlib.context import CryptContext

# Configure the password hashing settings
pwd_context = CryptContext(
    schemes=["bcrypt"],  # Use bcrypt algorithm for hashing
    deprecated="auto"   # Automatically mark older algorithms as deprecated It helps phase out old/weak hashing methods safely. Works like updating the bcrypt version.
)

# Convert normal password to hashed version
def hash_password(password: str):
    return pwd_context.hash(password)

# verify entered password against hashed password stored in database
def verify_password(
        plain_password: str,
        hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password 
    )