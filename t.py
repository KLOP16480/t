import requests
import threading
import os,sys,time
import pyfiglet
os.system ("clear")
os.system ("figlet autofacebook")
print ("")

a = pyfiglet.figlet_format(" Facebook")
print(f'\033[1;92m{a}')

print("\33[0m-----------------------------------------------")
print("\33[1;93mFACEBOOK : \33[1;93mphuwanai chuchid")
print("\33[1;94mFACEBOOK ครูผู้สอน : \33[1;92mเคร ครับ")
print("\33[0m-----------------------------------------------")
print("\33[1;94mFACEBOOK เก่าบินแล้ว : \33[1;92mมน ผู้กำเนิดพระเจ้า")
print("\33[0m-----------------------------------------------")
cookie = input("\033[1;96mcookie : \033[1;95m")
da = input("data : \033[1;97m")
nam = int(input("\033[1;96mnumber : \033[1;98m"))
spx = int(input("sleep : "))
print("\33[0m-----------------------------------------------")

def flood1():
	head = {
	    "Host": "mbasic.facebook.com",
	    "content-length": "263",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://mbasic.facebook.com",
	    "content-type": "application/x-www-form-urlencoded",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "navigate",
	    "sec-fetch-user": "?1",
	    "sec-fetch-dest": "document",
	    "referer": "https://m.facebook.com",
	    "cookie": f"{cookie}"
	    }
	requests.post("https://mbasic.facebook.com/messages/send/?icm=1&refid=12",headers=head,data=f"{da}")
	print("ส่งข้อความสำเร็จแล้ว")
	
try:
    for i in range(nam):
                        time.sleep(spx)
                        threading.Thread(target=flood1()).start
except KeyboardInterrupt:
                         print ("EXIT....")

