import socket,socketerror
from itertools import cycle
import struct

HOST = 'localhost'
PORT = 12000
s = socketerror.socketError(socket.AF_INET, socket.SOCK_DGRAM)
s.setErrorProb(0.1)
s.settimeout(2.0)
s.connect((HOST, PORT))

iterator = cycle(range(2))
iterator2 = cycle(range(2))
ack = ''

arquivo = open('arquivo.txt', 'r')
arquivo2 = open('arquivo.txt', 'r')

#Le o arquivo a cada 1000 bytes e para quando o arquivo termina.
while arquivo2.read(2) != "":
	texto = arquivo.read(2)
	indice = str(next(iterator))
	pacote = indice + texto
	s.sendWithError(pacote)

	while 1:
		try:
			ack = s.recvWithError(1024)
			if ack == indice:
				print (ack)
				break
		except socket.timeout:
			print ("Timeout, reenviando arquivo " + indice)
			s.sendWithError(pacote)
	

arquivo.close()
s.close()
