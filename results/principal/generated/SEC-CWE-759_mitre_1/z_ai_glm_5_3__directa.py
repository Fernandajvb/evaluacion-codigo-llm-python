import hashlib
import os


def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    salt = os.urandom(32)
    hashed_password = hashlib.sha256(salt + Password.encode('utf-8')).hexdigest()
    updateUserLogin(userName, salt.hex() + hashed_password)
