# -*- coding: cp1252 -*-
from socket import *
from itertools import cycle
import struct

serverPort = 12000
#Cria o Socket UDP (SOCK_DGRAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Associa o Socket criado com a porta desejada
serverSocket.bind(('localhost', serverPort))
#Cria um iterador que alterna entre 1 e 0
iterator = cycle(range(2))
oldPort = ''


print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
    try:
            message, clientAddress = serverSocket.recvfrom(2048)
            
            currPort = str(clientAddress[1]) #recebe a porta atual
            
            #compara a porta atual com a anterior para definir se o arquivo o pacote recebido e de um arquivo novo ou nao
            if oldPort != currPort:
                oldPort = currPort
                iterator = cycle(range(2)) #reseta o iterador
            
            #Identificador que o servidor esta esperando
            currAck = str(next(iterator))
            ack = currAck.encode()

            #Aguarda receber dados do socket
            data = message[1:] #Recebe o dado, a mensagem
            indice = message[0:1]
            print ("Pacote " + str(indice[0:1]))
            print ("ACK " + currAck)

            if ack == indice:
                arquivoServer = open("arquivoServer.txt", "ab")
                arquivoServer.write(data)
                arquivoServer.close()
                
                ackResponse = currAck
                serverSocket.sendto(ackResponse.encode(), clientAddress) #envia o ack 
                
                print(clientAddress)
                print(message)
            else:
                lastAck = str(next(iterator)) #muda o ack para o anterior
                serverSocket.sendto(lastAck.encode(), clientAddress)

    except (KeyboardInterrupt, SystemExit):
            break
serverSocket.close()
