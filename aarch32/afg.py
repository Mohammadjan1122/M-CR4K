#Author Mohammad sultani
import os
os.system("git pull")
try:
   import requests
except:
   os.system('pip2 install requests')

from mking import start_mking 
start_mking()
