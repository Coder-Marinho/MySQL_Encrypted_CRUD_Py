from cryptography.fernet import Fernet

with open("fertnet.key", "rb") as keyFile:
    key = keyFile.read()

cipher = Fernet(key)

dbHost = cipher.encrypt(b"localhost")
dbUser = cipher.encrypt(b"use")
dbPass = cipher.encrypt(b"password")
dbName = cipher.encrypt(b"database")

with open ("db_safeCredentials.txt", "wb") as safeCredentials:
    safeCredentials.write(dbHost + b"\n")
    safeCredentials.write(dbUser + b"\n")
    safeCredentials.write(dbPass + b"\n")
    safeCredentials.write(dbName + b"\n")

print("Safe credentials are created!")