import requests
import random
import time
import os

os.system('cls')

cookie = input("Cookie: ")
text = input("Text: ")

session = requests.session()
session.cookies['.ROBLOSECURITY'] = cookie

os.system("cls")

def random_gen(len):
        return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for x in range(len))

def grabCSRF(): #GrabCSRF not mine
   r = session.post("https://auth.roblox.com/v2/user/passwords/change")
   csrf = r.headers['x-csrf-token']
   return csrf

try:
    grabCSRF()
except KeyError:
    print("Cookie is invalid!")
    input()

os.system("cls")

csrf = grabCSRF()

def changeStatus(text):
    sfo = {
    "description":text
    }
    s = session.post(url = "https://accountinformation.roblox.com/v1/description",headers ={"X-CSRF-Token": csrf},data=sfo)
    if "403" in str(s.status_code):
        print("Cooldown Detected! | Status Code: " + str(s.status_code))
    else:
        print("Changed!")

changeStatus(text)
input()

input()