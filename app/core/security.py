
# Import necessary libraries for password hashing and JWT handling
from passlib.context import CryptContext  # For password hashing
from jose import jwt  # For JWT encoding
from datetime import datetime, timedelta  # For handling expiration times
import os  # For accessing environment variables

# Retrieve the secret key from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
# Define the algorithm used for JWT encoding
ALGORITHM = "HS256"

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a plain password using bcrypt
def hash_password(password):
    """
    Hashes a plain password using bcrypt algorithm.
    Args:
        password (str): The plain password to hash.
    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

# Verify a plain password against a hashed password
def verify_password(plain, hashed):
    """
    Verifies a plain password against its hashed version.
    Args:
        plain (str): The plain password to verify.
        hashed (str): The hashed password to compare against.
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain, hashed)

# Create a JWT token with expiration
def create_token(data: dict):
    """
    Creates a JWT token with the provided data and a 2-hour expiration.
    Args:
        data (dict): The data to encode in the token.
    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)