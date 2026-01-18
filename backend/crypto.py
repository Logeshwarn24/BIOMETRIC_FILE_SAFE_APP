import bcrypt
from cryptography.fernet import Fernet

# -------- PIN SECURITY --------
def hash_pin(pin: str) -> bytes:
    return bcrypt.hashpw(pin.encode(), bcrypt.gensalt())

def verify_pin(pin: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(pin.encode(), hashed)

# -------- FILE ENCRYPTION (OPTIONAL EXTENSION) --------
def generate_key():
    return Fernet.generate_key()

def encrypt_bytes(data: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(data)
