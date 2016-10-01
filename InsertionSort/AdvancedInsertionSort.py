#T(n) = θ(nlgn)
from random import shuffle

def binarySearch(seq, key, low, high):
	while low <= high:
		seek = (low + high) // 2
		value = seq[seek]

		if value < key:
			low = seek + 1
		elif value > key:
			high = seek - 1
		else:
			return seek
	return seek

def advancedInsertionSort(seq):
	for currIndex in range(1, len(seq)):
		key = seq[currIndex]
		insertPoint = binarySearch(seq, key, 0, currIndex - 1)

		if seq[insertPoint] > key:
			seq[insertPoint + 1 : currIndex + 1] = seq[insertPoint : currIndex]
			seq[insertPoint] = key
		else:
			seq[insertPoint + 2 : currIndex + 1] = seq[insertPoint + 1 : currIndex]
			seq[insertPoint + 1] = key

randomSeq = list(range(1, 101))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
advancedInsertionSort(randomSeq)
print('After sorted:\n', randomSeq)