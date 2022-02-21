#Author Mohammad sultani
import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
os.system("git pull") 
bit = platform.architecture()[0]
if bit == '64bit':
    from mking import mohammad
    mohammad()
elif bit == '32bit':
    from mking import mohammad
    mohammad()
