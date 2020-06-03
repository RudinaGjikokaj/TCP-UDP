import socket
import sys

serverName = 'localhost'
klientPort = 1501
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName , 12000))
print('Fiek Klienti:')

while True:
    print('FIEK-TCP klienti')
    print('\nOpsionet:')
    print('IPADRESA; NUMRIPORTIT; BASHTINGELLORE; PRINTIMI; EMRIIKOMPJUTERIT; KOHA; LOJA; FIBONACCI; KONVERTIMI; REVERSE; ')
    var = input('\nShkruaj kërkesën apo shtyp 2 për ndërprerje: ')
    mesazhi = var.upper()

    if mesazhi == 'IPADRESA':
        s.sendall(str.encode(mesazhi))
        data = s.recv(128).decode('utf-8')
        print('IP e juaj: ' + data)

    elif mesazhi == 'NUMRIPORTIT':
        s.sendall(str.encode(mesazhi))
        porti = str(klientPort)
        s.sendall(str.encode(porti))
        data = s.recv(128).decode('utf-8')
        print('Porti juaj është: '+str(data))

    elif mesazhi == 'BASHTINGELLORE':
        s.sendall(str.encode(mesazhi))
        Fjalia = input('Shtyp një fjali: ')
        s.sendall(str.encode(Fjalia))
        data = s.recv(128).decode('utf-8')
        print('Numri i bashtingelloreve është: '+data)

    elif mesazhi == 'PRINTIMI':
        s.sendall(str.encode(mesazhi))
        fjalia = input('Shkruaj një fjali: ')
        s.sendall(str.encode(fjalia))
        data = s.recv(128).decode('utf-8')
        print('Fjalia e dhënë është: ' +data)

    elif mesazhi == 'EMRIIKOMPJUTERIT':
        s.sendall(str.encode(mesazhi))
        data = s.recv(128).decode('utf-8')
        print('Emri i kompjuterit tuaj është: '+data)

    elif mesazhi == 'KOHA':
        s.sendall(str.encode(mesazhi))
        data = s.recv(128).decode('utf-8')
        print('Koha është: '+data)   

    elif mesazhi == 'LOJA':
        s.sendall(str.encode(mesazhi))
        data = s.recv(128).decode('utf-8')
        print('Nr random të gjeneruar: '+data)

    elif mesazhi == 'FIBONACCI':
        s.sendall(str.encode(mesazhi)) 
        numri = input('Jep një nr: ')
        s.sendall(str.encode(numri))
        data = s.recv(128).decode('utf-8')
        print('Fibonacci i nr të dhënë: ' +data)

    elif mesazhi == 'KONVERTIMI': 
        s.sendall(str.encode(mesazhi))
        print('Lejohen këto konvertime: \nKilowattToHorsepower \nHorsePowerToKilowatt \nDegreesToRadians \nRadiansToDegrees \nGallonsToLiters \nLitersToGallons')
        zgjedhja = input('Zgjedhni nje opsion: ')
        s.sendall(str.encode(zgjedhja))
        sasia = input('Nr që do konvertoni është: ')
        s.sendall(str.encode(sasia))
        data = s.recv(128).decode('utf-8')
        print('Numri i konvertuar është: '+data)

    elif mesazhi == 'REVERSE':
        s.sendall(str.encode(mesazhi))
        fjala = input('Fjala që do ktheni mbrapsht: ')
        s.sendall(str.encode(fjala))
        data = s.recv(128).decode('utf-8')
        print('Fjala e kthyer: '+data)
 

s.close()



