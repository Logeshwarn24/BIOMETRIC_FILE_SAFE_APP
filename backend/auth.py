from backend.biometric import windows_hello_auth
from backend.crypto import verify_pin
from backend.user_store import load_user

def authenticate(method, pin=None):
    if method == "biometric":
        return windows_hello_auth()

    if method == "pin":
        stored_pin = load_user()
        if stored_pin and pin:
            return verify_pin(pin, stored_pin)
        return False

    return False
