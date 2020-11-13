import requests
email=input('email: ')
Pass=input('pass: ')
mail=requests.get('https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login='+email+'&Password='+Pass, headers={'User-Agent': 'MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0'}).text
if ("Ok=0") in mail:
	print('failed')
else:
	print('OK')
