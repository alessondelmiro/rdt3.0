import socket,socketerror
from itertools import cycle
import struct

HOST = 'localhost'
PORT = 12000
s = socketerror.socketError(socket.AF_INET, socket.SOCK_DGRAM)
s.setErrorProb(0.1)
s.settimeout(2.0)
s.connect((HOST, PORT))

#cria um iterador que sera usado para o registro de sequencia
iterator = cycle(range(2))
ack = ''


arquivo = open('arquivo.txt', 'r')
arquivo2 = open('arquivo.txt', 'r')

while arquivo2.read(2) != "":
	texto = arquivo.read(2)
	indice = str(next(iterator))#sequencia do pacote, muda para o proximo a cada iteracao
	pacote = indice + texto #monta o pacote
	s.sendWithError(pacote) #envia para o servidor

        #estado que espera o ack correto
	while 1:
		try:
			ack = s.recvWithError(1024)
			if ack == indice:
				print (ack)
				break
		except socket.timeout:
			print ("Timeout, reenviando pacote " + indice)
			s.sendWithError(pacote)
	

arquivo.close()
s.close()
