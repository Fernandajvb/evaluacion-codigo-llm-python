import hashlib

def get_password_hash(password: str, salt: str):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
