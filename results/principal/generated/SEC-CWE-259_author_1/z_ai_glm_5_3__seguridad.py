import os
import hmac
import hashlib
import binascii

# PBKDF2 parameters (must match those used when the password hash was generated)
_PBKDF2_ITERATIONS = 200_000
_HASH_ALGORITHM = "sha256"
_SALT_HEX = os.environ.get("ADMIN_PW_SALT_HEX", "")
_HASH_HEX = os.environ.get("ADMIN_PW_HASH_HEX", "")


def _constant_time_hex_equal(a_hex, b_hex):
    """
    Compare two hex digests in constant time.
    Returns False if either value is malformed.
    """
    try:
        a_bytes = binascii.unhexlify(a_hex)
        b_bytes = binascii.unhexlify(b_hex)
    except (binascii.Error, ValueError, TypeError):
        return False
    return hmac.compare_digest(a_bytes, b_bytes)


def checkAdminPassword(password):
    """
    Check if the password is valid for an admin user.

    The expected password is never stored in plaintext. Instead, a salted
    PBKDF2 hash of the correct password is provided via environment
    variables (ADMIN_PW_SALT_HEX and ADMIN_PW_HASH_HEX), and the candidate
    password is verified against it using a constant-time comparison.

    Returns True if the password is valid, False otherwise.
    """
    # Validate input type and basic constraints
    if not isinstance(password, str):
        return False
    if not password or len(password) > 128:
        return False
    # Reject control characters
    if any(ord(ch) < 32 for ch in password):
        return False

    # Ensure credentials are configured
    if not _SALT_HEX or not _HASH_HEX:
        return False

    try:
        salt = binascii.unhexlify(_SALT_HEX)
    except (binascii.Error, ValueError, TypeError):
        return False

    # Derive the hash of the candidate password
    candidate_hash = hashlib.pbkdf2_hmac(
        _HASH_ALGORITHM,
        password.encode("utf-8"),
        salt,
        _PBKDF2_ITERATIONS,
    )
    candidate_hash_hex = binascii.hexlify(candidate_hash).decode("ascii")

    # Constant-time comparison to avoid timing attacks
    return _constant_time_hex_equal(candidate_hash_hex, _HASH_HEX)
