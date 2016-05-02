from itertools import cycle

myIterator = cycle(range(2))

for i in range(5):
	ack = str(myIterator.next())
	print ack