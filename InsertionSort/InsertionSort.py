#T(n) = O(n^2)
from random import shuffle

def insertionSort(seq):
	for currIndex in range(1, len(seq)):
		key = seq[currIndex]
		seek = currIndex - 1
		while seek >= 0 and seq[seek] > key:
			seek -= 1
		seq[seek + 2 : currIndex + 1] = seq[seek + 1 : currIndex]
		seq[seek + 1] = key
	return seq

randomSeq = list(range(1, 101))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
insertionSort(randomSeq)
print('After sorted:\n', randomSeq)