#T(n) = O(n^2)
from random import shuffle

def selectionSort(seq):
	length = len(seq)
	for top in range(0, length - 1):
		for seek in range(top + 1, length):
			if seq[seek] < seq[top]:
				seq[seek], seq[top] = seq[top], seq[seek]
	return seq

randomSeq = list(range(1, 21))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq) 
selectionSort(randomSeq)
print('After sorted:\n', randomSeq)