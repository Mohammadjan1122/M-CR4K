#Author Mohammad sultani

import os, platform

try:

   import requests

except:

   os.system('pip2 install requests')

import requests

from pro import mking_menu

bit = platform.architecture()[0]

if bit == '64bit':

	mking_menu()elif bit == '32bit':

	mking_menu()
