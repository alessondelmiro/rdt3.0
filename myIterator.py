import itertools
import struct
import socket



myIterator = cycle()

ack = next(myIterator)
myIterator.seek(0)
ack = next(myIterator)

print myIterator
'''
currAck = next(myIterator)
print ("Ack atual: " + str(currAck))

oldAck = next(myIterator)
currAck = next(myIterator)
currAck = next(myIterator)
print ("Ack velho: " + str(oldAck))
print ("Ack atual: " + str(currAck))



for i in range(5):
	ack = next(myIterator)
	print (ack)


arquivo = open('arquivo.txt', 'rb')
pacote = arquivo.read(1000)


i = 5
print (type(i))
#transforma p inteiro em byte e concatena com o pacote, que e um byte
p = i.to_bytes(1,byteorder='big')

print (p[0])

#transforma o p de volta pra inteiro
j=int.from_bytes(p[0:1],byteorder='big')
print(j)

arquivo.close()
'''