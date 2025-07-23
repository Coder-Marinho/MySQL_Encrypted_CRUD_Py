from tkinter.constants import INSERT
from cryptography.fernet import Fernet

#Call others files for they function
import Credentials
from Key_import import generateKey
import os

#Open the file contain the key for read
def openKey():
    with open("fernet.key", "rb") as keyFile:
        key = keyFile.read()
    print("Key was founded.")
    return key

if os.path.exists("fernet.key"):
    openKey()
else:
    print("Key file was not founded\n")
    print("Creating a new key file\n")
    generateKey()

#Atributte the key for "cipher" variable
cipher = Fernet(key)

Credentials.credentialsCollect()

connectionDb = mysql.connector.connect(**encripted)

#Function for data encryption
def encryptData(data):
    return cipher.encrypt(data.encode()).decode()

#Function for data dencryption
def decryptData(token):
    return cipher.decrypt(token.encode()).decode()

#Convert the plain text to a cipher text
def safeData():
    safeName = encryptData(input("Insert the name of user"))
    safeEmail = encryptData(input("Insert the email of user: "))
    return safeName, safeEmail

def createUser():
    name, email = safeData()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (name, email))

