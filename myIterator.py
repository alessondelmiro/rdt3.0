from itertools import cycle
import struct

myIterator = cycle(range(2))
'''
for i in range(5):
	ack = next(myIterator)
	print (type(ack))
'''

arquivo = open('C:\Program Files (x86)\PuTTY\putty.exe', 'rb')
pacote = arquivo.read(1000)


i = 5
print (type(i))
#transforma p inteiro em byte e concatena com o pacote, que e um byte
p = i.to_bytes(1,byteorder='big')+pacote

print (p[0])

#transforma o p de volta pra inteiro
j=int.from_bytes(p[0:1],byteorder='big')
print(j)

arquivo.close()
