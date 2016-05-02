import socket,socketerror

HOST = 'localhost'
PORT = 12000
s = socketerror.socketError(socket.AF_INET, socket.SOCK_DGRAM)
s.setErrorProb(0.0)
s.settimeout(2.0)
s.connect((HOST, PORT))

arquivo = open('teste.txt', 'r')
arquivo2 = open('teste.txt', 'r')

#Lê o arquivo a cada 1000 bytes e pára quando o arquivo termina.
while arquivo2.read(1000) != "":
	pacote = arquivo.read(1000)
	s.sendWithError(pacote)

try:
    data = s.recvWithError(1024)
    print(data)
except socket.timeout:
    print("Timeout")

try:
    data = s.recvWithError(1024)
    print(data)
except socket.timeout:
    print("Timeout")

arquivo.close()
s.close()
