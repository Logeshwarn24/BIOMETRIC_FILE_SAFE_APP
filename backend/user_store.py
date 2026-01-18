import os
import pickle

USER_FILE = "backend/user.dat"

def save_user(hashed_pin):
    with open(USER_FILE, "wb") as f:
        pickle.dump(hashed_pin, f)

def load_user():
    if not os.path.exists(USER_FILE):
        return None
    with open(USER_FILE, "rb") as f:
        return pickle.load(f)
