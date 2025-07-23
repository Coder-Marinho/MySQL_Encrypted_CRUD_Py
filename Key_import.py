#Fernet criptography library
from cryptography.fernet import Fernet

#Variable to receive the Fernet key
key = Fernet.generate_key()

#Write the key in key archive
with open("fernet.key", "wb") as keyFile:
    keyFile.write(key)

print("Your key was been saved")