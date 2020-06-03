from socket import *
import sys
from _thread import *
import datetime
import random
import os
host = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

try :
    serverSocket.bind(('',serverPort))
except IOError:
    print("Klienti nuk mund të lidhet!")
    sys.exit()


print ('Serveri u startua në localhost: '+str(serverPort))
serverSocket.listen(10)
print('Serveri i gatshëm të pranojë kërkesë')


def FIBONACCI(number):
     x=1
     y=1
     for numeruesi in range(2,number):
            fibonaccin = x + y;
            x = y;
            y = fibonaccin;
     return fibonaccin


def EMRIIKOMPJUTERIT(): 
    return gethostname()

def IPADRESA():
    return gethostbyname(gethostname())

def BASHTINGELLORE(x):
    bashtingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','Z' ]
    numeratori=0
    for shkronja in x:
        if(shkronja in bashtingellore ):
            numeratori = numeratori+1
    return numeratori

def KOHA():
    K = datetime.datetime.now()
    K = K.strftime('%H:%M:%S')
    return K

def LOJA():
    nums = random.sample(range(1,49),7)
    numrat = str(nums)
    return numrat


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


def clientthread(connectionSocket):
    while True:
        try:
            fjalia = connectionSocket.recv(128).decode('utf-8')
            if not fjalia:
                break;
        except IOError:
            print('Ka ndodhur një problem!')
            break

        komanda = str(fjalia)

        if komanda == 'NUMRIPORTIT':
            data = connectionSocket.recv(128).decode('utf-8')
            connectionSocket.send(str(data).encode('utf-8'))

        elif komanda == 'PRINTIMI':
            mesazhi = connectionSocket.recv(128)
            connectionSocket.send(mesazhi)

        elif komanda == 'EMRIIKOMPJUTERIT':
            connectionSocket.send(str(EMRIIKOMPJUTERIT()).encode('utf-8'))

        elif komanda == 'IPADRESA':
            connectionSocket.send(str(IPADRESA()).encode('utf-8'))

        elif komanda == 'BASHTINGELLORE':
            fjaliaB = connectionSocket.recv(128).decode('utf-8')
            print('Fjalia e dhënë: "'+fjaliaB+'"')
            connectionSocket.send(str(BASHTINGELLORE(fjaliaB)).encode('utf-8'))
        
        elif komanda == 'KOHA':
            connectionSocket.send((KOHA().encode('utf-8'))) 


        elif komanda == 'LOJA':
            connectionSocket.send((LOJA().encode('utf-8')))

        elif komanda == 'FIBONACCI':
            numri = connectionSocket.recv(128).decode('utf-8')
            print('Nr i dhënë: ' + numri)
            nr = int(numri)
            connectionSocket.send(str(FIBONACCI(nr)).encode('utf-8'))

        elif komanda == 'REVERSE':
            fjala = connectionSocket.recv(128).decode('utf-8')
            fjala = fjala[::-1]
            print(fjala)
            connectionSocket.send(str(fjala).encode('utf-8'))

        elif komanda == 'KONVERTIMI':
            zgjedhja = connectionSocket.recv(128).decode('utf-8')
            numri = connectionSocket.recv(128).decode('utf-8')
            nr = int (numri)
            print('Zgjodhët të konvertoni: ' + str(zgjedhja))
            connectionSocket.send(str(KONVERTIMI(zgjedhja, nr)).encode('utf-8'))
    connectionSocket.close()

while 1:
    connection, address = serverSocket.accept()
    print("Serveri tani është lidhur në: " + str(address))
    start_new_thread(clientthread,(connection,))

serverSocket.close()
