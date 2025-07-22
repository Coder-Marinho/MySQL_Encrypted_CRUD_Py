from cryptography.fernet import Fernet

#Credentials dictionary
credentials = {"host": "",
               "user": "",
               "password": "",
               "database": ""
               }

#Main loop for collect credentials data
def credentialsCollect():
    for key in credentials:
        credentials[key] = input(f"Insert the {key}: ")
    encryptCredentials()

#Loop for encrypt and save credentials
def encryptCredentials():
    with open("fertnet.key", "rb") as keyFile:
        key = keyFile.read()

    cipher = Fernet(key)


    with open ("db_safeCredentials.txt", "wb") as safeCredentials:
        for field in credentials:
            encrypted =  cipher.encrypt(credentials[field].encode())
            safeCredentials.write(encrypted + b"\n")


    print("Safe credentials are created!")