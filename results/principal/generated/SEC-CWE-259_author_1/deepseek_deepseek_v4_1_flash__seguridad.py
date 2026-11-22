import os
import hmac
import hashlib

def checkAdminPassword(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8 or len(password) > 128:
        return False
    salt_hex = os.environ.get('ADMIN_PASSWORD_SALT')
    hash_hex = os.environ.get('ADMIN_PASSWORD_HASH')
    if not salt_hex or not hash_hex:
        return False
    try:
        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)
    except ValueError:
        return False
    if len(salt) < 16 or len(expected_hash) != 32:
        return False
    derived_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hmac.compare_digest(derived_hash, expected_hash)
