import hashlib
import secrets


def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    # --- Input validation ---
    if not isinstance(userName, str):
        raise TypeError("userName must be a string")
    if not isinstance(Password, str):
        raise TypeError("Password must be a string")

    userName = userName.strip()
    if not userName:
        raise ValueError("userName must not be empty")
    if len(userName) > 64:
        raise ValueError("userName exceeds the maximum allowed length")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in userName):
        raise ValueError("userName must not contain control characters")

    if not Password:
        raise ValueError("Password must not be empty")
    if len(Password) > 1024:
        raise ValueError("Password exceeds the maximum allowed length")

    try:
        password_bytes = Password.encode("utf-8")
    except UnicodeEncodeError:
        raise ValueError("Password contains invalid Unicode characters")

    # --- Secure hashing: PBKDF2-HMAC-SHA256 with a unique, cryptographically secure per-user salt ---
    algorithm = "pbkdf2_sha256"
    iterations = 600_000
    salt = secrets.token_bytes(16)

    derived_key = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, iterations)

    # Format: algorithm$iterations$salt$hash (salt and hash in hexadecimal)
    hashed_password = "$".join(
        [algorithm, str(iterations), salt.hex(), derived_key.hex()]
    )

    # --- Update the database with the username and the hashed password ---
    updateUserLogin(userName, hashed_password)
