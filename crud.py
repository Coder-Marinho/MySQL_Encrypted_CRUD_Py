from tkinter.constants import INSERT

from cryptography.fernet import Fernet

#Call others files for they function
import Credentials
import Key_import

#Open the file contain the key for read
with open("fernet.key", "rb") as keyFile:
   key = keyFile.read()

#Atributte the key for "cipher" variable
cipher = Fernet(key)

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
    sql = INSERT INTO

