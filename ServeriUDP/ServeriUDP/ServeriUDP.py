from socket import * 
import sys 
from _thread import * 
import datetime
import random 

host = 'localhost'
port = 12000
serverSocket= socket(AF_INET , SOCK_DGRAM)

try: 
    serverSocket.bind((host,port))
except: 
    print('Lidhja nuk u arrit!')
    sys.exit()

print('Serveri u startua ne localhost:'+str(port))
print('Serveri i gatshëm të pranojë kërkesë')


def BASHTINGELLORE(x):
   bashtingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','Z']
   numeratori=0
   for shkronja in x:
        if(shkronja in bashtingellore ):
            numeratori=numeratori+1
   return numeratori

def FIBONACCI(number):
     x=1
     y=1
     for numeruesi in range(2,number):
            fibonaccia = x + y
            x = y
            y = fibonaccia
     return fibonaccia

def IPADRESA():
    return gethostbyname(gethostname())

def EMRIIKOMPJUTERIT(): 
    return gethostname()

def KOHA():
    K=datetime.datetime.now()
    K = K.strftime('%H:%M:%S')
    return K

def KONVERTIMI(zgjedh, vlera):
   if zgjedh=="KilowattToHorsepower":
        rezultati=vlera*1.341 

   elif zgjedh=="HorsepowerToKilowatt":
        rezultati=vlera/1.341 

   elif zgjedh=="DegreesToRadians":
        rezultati = vlera*pi/180

   elif zgjedh=="RadiansToDegrees":
       rezultati = vlera*180/pi 

   elif zgjedh=="GallonsToLiters":
         rezultati = vlera*3.785 
     
   elif zgjedh=="LitersToGallons":
         rezultati = vlera/3.785 
   else:

        rezultati = "Gabim"
   return rezultati


def LOJA():
    nums = random.sample(range(1,49),7)
    
    numrat = str(nums)
    return numrat

def clientthread (input , address):
    try:
        data = input.decode('utf-8')
    except IOError:
        print('Ka ndodhur nje gabim')
    komanda=str(data).rsplit(' ')
    fjalia=''
    i=len(komanda)
    for fjala in range(1,i):
        fjalia=fjalia+komanda[fjala]
        if(fjala!=i):
            fjalia+=' '
    fund=str(fjalia)
    
    if komanda[0]=='BASHTINGELLORE':
        serverSocket.sendto(str(BASHTINGELLORE(fund)).encode('utf-8') , address)
    elif komanda[0]=='EMRIIKOMPJUTERIT':
        serverSocket.sendto(str(EMRIIKOMPJUTERIT()).encode('utf-8'), address)
    elif komanda[0]=='FIBONACCI':
        nr=int(komanda[1])
        serverSocket.sendto(str(FIBONACCI(nr)).encode('utf-8'),address)
    elif komanda[0] == 'REVERSE':
         fjala = komanda[1]
         fjala = fjala[::-1]
         print(fjala)
         serverSocket.sendto(str(fjala).encode('utf-8') , address)
    elif komanda[0]== 'IPADRESA':
        serverSocket.sendto(str(IP()).encode('utf-8') , address)
    elif komanda[0]=='NUMRIPORTIT':
        serverSocket.sendto(str(port).encode('utf-8') , address)
    elif komanda[0] == 'PRINTIMI':
        serverSocket.sendto(str(fund).encode('utf-8') , address)
    elif komanda[0]== 'KOHA':
        serverSocket.sendto(str(KOHA()).encode('utf-8') , address)
    elif komanda[0] == 'LOJA':
        serverSocket.sendto(str(LOJA()).encode('utf-8') , address)
    elif komanda[0] == 'KONVERTIMI':
        print('Klienti ka zgjedhur te konvertoj' + komanda[1])
        nr=int(komanda[2])
        serverSocket.sendto(str(KONVERTIMI(komanda[1], nr)).encode('utf-8'),address)
    else:
        serverSocket.sendto(str('GABIM!').encode('utf-8'))
while True:
    data , address=serverSocket.recvfrom(128)
    print('Serveri tani eshte lidhur me' + str(address))
    start_new_thread(clientthread , (data,address,))
serverSocket.close()



