import threading
from threading import Thread
import os
import requests
import time
import sys
import pyfiglet
os.system('clear')

try:
	import requests
except ImportError:
	print('[!] Not module in data')
	
a = pyfiglet.figlet_format(" Facebook")
print(f'\033[1;95m{a}')

print("\33[0m-----------------------------------------------")
print("\33[1;93mFACEBOOK : \33[1;93mphuwanai chuchid")
print("\33[1;94mFACEBOOK ครูผู้สอน : \33[1;92mเคร ครับ")
print("\33[0m-----------------------------------------------")
print("\33[1;94mFACEBOOK ฟังชั่น : \33[1;92mฟลัดเม้น")
print("\33[0m-----------------------------------------------")

token = input("\033[1;96mtoken facebook : \033[1;95m")
d = input("ไอดีโพสต์ : \033[1;97m")
msg = input("messages : \033[1;92m")
no = int(input("\033[1;96mnumber : \033[1;98m"))
t = int(input("time : "))
print('')
def comments():
	requests.get(f'https://graph.facebook.com/{d}/comments?method=POST&message={msg}&access_token={token}')
	print("comments send")
for i in range(no):
	time.sleep(t)
	threading.Thread(target=comments).start()