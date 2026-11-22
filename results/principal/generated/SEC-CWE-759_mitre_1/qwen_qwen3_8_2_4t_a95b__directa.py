import hashlib

def storePassword(userName, Password):
    hashedPassword = hashlib.sha256(Password.encode('utf-8')).hexdigest()
    updateUserLogin(userName, hashedPassword)
