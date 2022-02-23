#!/usr/bin/env python3
import time #line:3
from colorama import Fore ,Back ,Style ,init #line:4
init (autoreset =True )#line:5
def startMessage ():#line:7
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")#line:8
    OOOO0OO000OO0OOOO ="qadirahmad"#line:9
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :#line:10
        print (Fore .RED +'[X] Wrong Code')#line:11
        print (Fore .BLUE +''' 
   1. Go to Insta and massage 
   2. Insta ID: qadirahmad6291
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')#line:18
        startMessage ()#line:19
    else :#line:20
        print (Fore .GREEN +"Successfully Unlocked Tool!")#line:21
        pass #line:22
if __name__ =="__main__":#line:24
    startMessage ()#line:25
    


import smtplib
import socket
import os
import socket


from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint


try:
    import socks
except ModuleNotFoundError:
    os.system("pip install spcks")



clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"]

import sys

try:
    from InstagramAPI import InstagramAPI
    import requests
    import json
    import random
    import getpass

    while True:
        nostop = 0

        while True:
            accounts = input("Put your Instagram accounts list here (if there is no file just press ENTER): ")
            if not accounts:
                username = input("Put your  Username then press ENTER: ")
                try:
                    password = getpass.getpass(prompt="Put your ID Password then press ENTER: ")
                except Exception as error:
                    print("Error:", error)
                else:
                    print("Got Password. Attempting to login.")
                api = InstagramAPI(username, password)
                api.login()
                break

            else:
                try:
                    line = random.choice(open(accounts).readlines())
                    username, password = line.split(':')
                    print("Username found: ", username)
                    print("Password found: ", password)
                    api = InstagramAPI(username, password)
                    api.login()
                    break

                except:
                    print("Wrong file")

        while True:
            print("Would you prefer enter the user ID or the username (bêta)")
            if input("UserID = i, Username = o: ") == "o":
                user = input("Enter the victim's  Username: ")
                try:
                    response = requests.get("https://www.instagram.com/" + user + "/?__a=1")
                    respJSON = response.json()
                    user_id = str(respJSON['graphql'].get("user").get("id"))
                except:
                    print("Unknown victim's username")
                    print("Either Instagram API is not corrected or you entered a false username")
                    exit(0)
            else:
                while True:
                    user_id = input("Enter the victim's  UserID (or press i to get more info about UserID): ")

                    if isinstance(int(user_id), int) == True:
                        break
                    elif user_id == 'i':
                        print("""To found a IG UserID you have to search https://www.instagram.com/{USERNAME}/?__a=1' and to go to graphql=>user=>id.
The correct id is named id, not fbid.""")
                        input("Press enter to continue")
                    else:
                        print("This  UserID is unknown.")

            while True:
                nostop = 0
                message = input("Put the message you want the software send and press ENTER: ")
                while True:
                    try:
                        times = int(input("How many messages do you want to send? "))
                        break
                    except:
                        print("Wrong number")

                proxylist = input("Proxy list (TXT): (If you don't have proxy list press ENTER): ")
                if accounts:
                    proxy = random.choice(open(proxylist).readlines())
                    api.setProxy(proxy)
                while times > nostop:
                    nostop = nostop + 1
                    api.sendMessage(user_id, message)
                    print(nostop, ">> Sent to", user_id, ": ", message)

except:
    sys.exit(
        '\nA critical error happened. Please make sure that you executed all commands properly and relaunch the program.')
                    
cont = ""
while cont not in no:
    cracker()
    ch = input(f"{ran}Continue? {y}(y/n): "+r).lower()

    if ch in no:
        clear
        banner2()

    else:
        banner2()


