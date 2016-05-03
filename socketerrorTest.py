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

arquivo = open('arquivo.txt', 'r')
arquivo2 = open('arquivo.txt', 'r')

#Le o arquivo a cada 1000 bytes e para quando o arquivo termina.
while arquivo2.read(1000) != "":
	texto = arquivo.read(1000)
	indice = str(next(iterator))
	pacote = indice + texto
	s.sendWithError(pacote)

	try:
                data = s.recvWithError(1024)
                print(data)

        except socket.timeout:
                print("Timeout")

arquivo.close()
s.close()
