from socket import *
import sys

host='localhost'
port=12000
klientSocket=socket(AF_INET, SOCK_DGRAM)
print('Fiek Klienti:')
print('Opsionet:')
print('IPADRESA; NUMRIPORTIT; BASHTINGELLORE; PRINTIMI; EMRIIKOMPJUTERIT; KOHA; LOJA; FIBONACCI; KONVERTIMI; REVERSE;{hapsire} Numri \nKONVERTIMI {hapsire} Opsioni {hapsire} vlera \nOpsionet:KilowattToHorsepower<-->HorsePowerToKilowatt\n\t DegreesToRadians<-->RadiansToDegrees\n\t GallonsToLiters<-->LitersToGallons  ')
mesazhi=input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')                 
    
address = (host,port)

while(mesazhi!='' and mesazhi!='b'):
    data=''

    if 'BASHTINGELLORE' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Nr i bashtingelloreve: '+str(data))
        mesazhi=input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'REVERSE' in mesazhi:
        klientSocket.sendto(mesazhi.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Fjala e kthyer: '+str(data))
        mesazhi=input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'EMRIIKOMPJUTERIT' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Emri i kompjuterit tuaj eshte: '+ str(data))
        mesazhi=input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'FIBONACCI' in mesazhi:
        klientSocket.sendto(mesazhi.encode() , (host , port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Fibonacci i nr të dhënë: '+str(data))
        mesazhi=input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'IPADRESA' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data = klientSocket.recv(128).decode('utf-8')
        print('IP e juaj: '+data)
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'NUMRIPORTIT' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data = klientSocket.recv(128).decode('utf-8')
        print('Porti juaj: ' +str(data))
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'PRINTIMI' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data = klientSocket.recv(128).decode('utf-8')
        print('Fjalia e dhënë: ' +data)
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'KOHA' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data = klientSocket.recv(128).decode('utf-8')
        print('Ora: ' +data)
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'LOJA' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data = str(klientSocket.recv(128))
        print('Nr random të gjeneruar: '+data)
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    elif 'KONVERTIMI' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data = klientSocket.recv(128).decode('utf-8')
        print('Nr i konvertuar: ' +str(data))
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

    else:
        print('Shtyp një kërkesë valide')
        mesazhi = input('Shkruaj kërkesën apo shtyp b për ndërprerje: ')

klientSocket.close()


