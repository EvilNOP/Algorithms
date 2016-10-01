#T(n) = O(n)
from random import randint

def randomizeInPlace(seq):
	length = len(seq)
	for index in range(0, length):
		randomIndex = randint(index, length - 1)
		seq[index], seq[randomIndex] = seq[randomIndex], seq[index]

randomSeq = list(range(1, 1001))
print('Oringinal Sequence: \n', randomSeq)

randomizeInPlace(randomSeq)
print('After shuffled: \n', randomSeq)