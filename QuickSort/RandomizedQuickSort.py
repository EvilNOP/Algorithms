from random import (randint, shuffle)

def partition(seq, left, right):
	currentIndex = left - 1
	pivotElement = seq[right]

	for index in range(left, right):
		if seq[index] <= pivotElement:
			currentIndex += 1
			seq[currentIndex], seq[index] = seq[index], seq[currentIndex]
	seq[currentIndex + 1], seq[right] = seq[right], seq[currentIndex + 1]

	return currentIndex + 1

def randomizedPartition(seq, left, right):
	randomIndex = randint(left, right)
	seq[right], seq[randomIndex] = seq[randomIndex], seq[right]
	
	return partition(seq, left, right)

def randomizedQuickSort(seq, left, right):
	if left < right:
		midIndex = partition(seq, left, right)
		randomizedQuickSort(seq, left, midIndex - 1)
		randomizedQuickSort(seq, midIndex + 1, right)

randomSeq = list(range(1, 1000))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
randomizedQuickSort(randomSeq, 0, 999)
print('After sorted:\n', randomSeq)