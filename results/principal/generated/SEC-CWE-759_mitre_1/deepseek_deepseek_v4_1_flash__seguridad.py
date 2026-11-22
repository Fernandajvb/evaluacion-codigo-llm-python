import hashlib
import os

def storePassword(userName, Password):
    if not isinstance(userName, str) or not userName or len(userName) > 150:
        raise ValueError("Invalid userName")
    if not isinstance(Password, str) or not Password or len(Password) > 1024:
        raise ValueError("Invalid Password")
    if "\x00" in userName or "\x00" in Password:
        raise ValueError("Invalid input")

    salt = os.urandom(16)
    iterations = 100_000
    password_bytes = Password.encode("utf-8")
    hashed = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, iterations)
    hashed_password = f"pbkdf2_sha256${iterations}${salt.hex()}${hashed.hex()}"
    return updateUserLogin(userName, hashed_password)
