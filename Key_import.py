from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("fertnet.key", "wb") as keyFile:
    keyFile.write(key)

print("Your key was been saved")