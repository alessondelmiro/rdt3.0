# -*- coding: cp1252 -*-
from socket import *
from itertools import cycle

serverPort = 12000
#Cria o Socket UDP (SOCK_DGRAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Associa o Socket criado com a porta desejada
serverSocket.bind(('localhost', serverPort))
#Cria um iterador que alterna entre 1 e 0
iterator = cycle(range(2))

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")


while 1:
    try:
            #Aguarda receber dados do socket
            message, clientAddress = serverSocket.recvfrom(2048)
            data = message[1:]
            
            print(clientAddress)
            print(message[0:1])
            print(message)
            
            arquivoServer = open("arquivoServer.txt", "ab")
            arquivoServer.write(data)
            arquivoServer.close()

            ack = str(next(iterator))
            modifiedMessage = "ACK " + ack
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except (KeyboardInterrupt, SystemExit):
            break
serverSocket.close()
