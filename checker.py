import time
from colorama import Fore ,Back ,Style ,init
init (autoreset =True )
def startMessage ():
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")
    OOOO0OO000OO0OOOO ="iloveu"
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :
        print (Fore .RED +'[X] Wrong Code')
        print (Fore .BLUE +''' 
   1. Go to Insta and massage 
   2. Insta ID: cyberphantomsyndicate
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')
        startMessage ()
    else :
        print (Fore .GREEN +"Successfully Unlocked Tool!")
        pass 
if __name__ =="__main__":
    startMessage ()

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
  if res.status_code != 200:    
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
