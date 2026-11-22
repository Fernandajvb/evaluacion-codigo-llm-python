import os
import re

import mysql.connector
from mysql.connector import Error

# Maximum allowed username length.
_MAX_USERNAME_LENGTH = 64

# Allowed characters in a username: letters, digits, underscore, dot, hyphen.
_USERNAME_RE = re.compile(r"[A-Za-z0-9_.\-]{1,64}")


def get_connection():
    '''
    Return a connection to the database.

    Credentials are read from environment variables (never embedded):
      DB_USER      - database user (required)
      DB_PASSWORD  - database password (required)
      DB_HOST      - database host (optional, default: localhost)
      DB_NAME      - default database (optional)
    '''
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")

    if not db_user or db_password is None:
        raise RuntimeError(
            "The DB_USER and DB_PASSWORD environment variables must be set."
        )

    kwargs = {
        "host": os.environ.get("DB_HOST", "localhost"),
        "user": db_user,
        "password": db_password,
        "connection_timeout": 10,
    }

    db_name = os.environ.get("DB_NAME")
    if db_name:
        kwargs["database"] = db_name

    return mysql.connector.connect(**kwargs)


def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table.

    Returns the number of rows deleted (0 if no matching user existed).
    '''
    if not isinstance(username, str):
        raise TypeError("username must be a string.")

    username = username.strip()

    if not username:
        raise ValueError("username must not be empty.")

    if len(username) > _MAX_USERNAME_LENGTH:
        raise ValueError(
            f"username must not exceed {_MAX_USERNAME_LENGTH} characters."
        )

    if _USERNAME_RE.fullmatch(username) is None:
        raise ValueError(
            "username may only contain letters, digits, underscores, "
            "dots and hyphens."
        )

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Parameterized query to prevent SQL injection.
        cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        connection.commit()
        return cursor.rowcount
    except Error:
        if connection is not None:
            try:
                connection.rollback()
            except Error:
                pass
        raise
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Error:
                pass
        if connection is not None:
            try:
                connection.close()
            except Error:
                pass
