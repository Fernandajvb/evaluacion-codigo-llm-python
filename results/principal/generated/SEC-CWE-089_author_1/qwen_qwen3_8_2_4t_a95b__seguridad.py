import os
import mysql.connector
from mysql.connector import Error

_DELETE_USER_STATEMENT = "DELETE FROM users WHERE username = %s"
_MAX_USERNAME_LENGTH = 255


def get_connection():
    """
    Return a connection to the database
    """
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    if not host:
        raise ValueError("DB_HOST must not be empty.")
    if not user:
        raise ValueError("DB_USER must be set.")
    if password is None:
        raise ValueError("DB_PASSWORD must be set.")
    if not database:
        raise ValueError("DB_NAME must be set.")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        connect_timeout=10,
    )


def remove_user(username):
    """
    Remove the user with the "username" specified from the "users" table
    """
    if not isinstance(username, str):
        raise TypeError("username must be a string.")
    if not username:
        raise ValueError("username must not be empty.")
    if len(username) > _MAX_USERNAME_LENGTH:
        raise ValueError("username is too long.")
    if "\x00" in username:
        raise ValueError("username contains an invalid null character.")

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(_DELETE_USER_STATEMENT, (username,))
        connection.commit()
    except Error:
        if connection is not None and connection.is_connected():
            connection.rollback()
        raise
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
