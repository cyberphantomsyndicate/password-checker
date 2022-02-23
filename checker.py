import time #line:3
from colorama import Fore ,Back ,Style ,init #line:4
init (autoreset =True )#line:5
def startMessage ():#line:7
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")#line:8
    OOOO0OO000OO0OOOO ="iloveu"#line:9
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

from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint





clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"]    
import requests
import hashlib
import sys



def request_api_data(query_char):
  '''requests our data and gives us a response'''
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:    #check our response if the status is 200
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  '''loop through all the hashes for checking the parameter 'hash_to_check' and returns the count '''
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  '''check password if it exists in API'''
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()   #hashing the password using SHA-1 algorithm and returning query char
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  '''recieves the arguments that we give in command line'''
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should  change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return '!!!-----Thannks For using----!!!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))    #exiting out of the file 
