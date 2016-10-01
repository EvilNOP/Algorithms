#T(n) = O(n^2)
from random import shuffle

def insertionSort(seq, currIndex):
	key = seq[currIndex]
	seek = currIndex - 1
	while seek >= 0 and seq[seek] > key:
			seek -= 1
	seq[seek + 2 : currIndex + 1] = seq[seek + 1 : currIndex]
	seq[seek + 1] = key
	return seq

def recusionInsertionSort(seq, currIndex):
	if currIndex >= 1:
		recusionInsertionSort(seq, currIndex - 1)
		insertionSort(seq, currIndex)

randomSeq = list(range(1, 21))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
recusionInsertionSort(randomSeq, 19)
print('After sorted:\n', randomSeq)