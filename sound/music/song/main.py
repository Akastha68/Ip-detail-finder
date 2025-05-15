#!/usr/bin/python3
# -*- coding: utf-8 -*-
import music as m
import Internet as Astha
import data as krishika
import banner as b
from colorama import Fore as F
import requests
import time


# WARNIMG !!!! WARNNING!!!! #
def menu():
  try:
     time.sleep(0.5)
     m.Ladies()
     b.banner()
     print(F.RED,'[0] TRACK ANY IP')
     print(F.GREEN,'[1] SHOW MY DETAILS IP')
     print(F.CYAN,'[€] Press ctrl+c for exit')
     var = int(input('\n==>'))
     if var == 0:
            m.Granted()
            b.Bbanner()
            krishika.krish()
     elif var == 1:
            m.Granted()
            b.Cbanner()
            krishika.ast()
     else:
            print(F.RED,'\n[#] Error option try again.')
            time.sleep(2)
            menu()
  except KeyboardInterrupt:
     print(F.CYAN,"_"*30)
     print(F.RED,"Thankyou for using") 
     print(F.BLUE,"//Author:- Akash Patel")
     print(F.CYAN,"_"*30)
     time.sleep(1)
     m.Denied()


Astha.CheckConnection()

try:
   if requests.get('https://google.com').status_code == 200:
         menu()
   else:
        quit()
except:
   quit()
