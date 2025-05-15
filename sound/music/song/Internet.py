import requests
import time
import music as m
from colorama import Fore as F


def CheckConnection():
     try:
        requests.get('https://google.com/')
     except:
         print(F.GREEN,"-"*30)
         print(F.RED,"| Please connect with internet|")
         print(F.BLUE,"|Internet Commection Required |")
         print(F.YELLOW,"|Thank you for using us       |")
         print(" |Author:- Superficial AK      |")
         print(F.GREEN,"-"*30)
         time.sleep(1)
         m.Welcome()
