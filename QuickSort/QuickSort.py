from random import shuffle

def partition(seq, left, right):
	currentIndex = left - 1
	pivotElement = seq[right]

	for index in range(left, right):
		if seq[index] <= pivotElement:
			currentIndex += 1
			seq[currentIndex], seq[index] = seq[index], seq[currentIndex]
	seq[currentIndex + 1], seq[right] = seq[right], seq[currentIndex + 1]

	return currentIndex + 1

def quickSort(seq, left, right):
	if left < right:
		midIndex = partition(seq, left, right)
		quickSort(seq, left, midIndex - 1)
		quickSort(seq, midIndex + 1, right)

randomSeq = list(range(1, 60001))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
quickSort(randomSeq, 0, 59999)
print('After sorted:\n', randomSeq)