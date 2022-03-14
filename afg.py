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
	os.system("git pull")
	os.system("cd aarch64 && chmod 777 mking.so && chmod 777 pro.so && python2 afg.py") 
elif bit == '32bit':
	os.system("git pull")
	os.system("cd aarch32 && chmod 777 mking.so && chmod 777 pro.so && python2 afg.py") 
