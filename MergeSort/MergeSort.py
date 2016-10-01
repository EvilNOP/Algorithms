#T(n) = θ(nlgn)
from sys import maxsize
from random import shuffle

def merge(seq, left, mid, right):
	leftSeq = seq[left : mid + 1]
	rigthSeq = seq[mid + 1 : right + 1]

	leftSeq.append(maxsize)
	rigthSeq.append(maxsize)

	i, j = (0, 0)

	for k in range(left, right + 1):
		if leftSeq[i] <= rigthSeq[j]:
			seq[k] = leftSeq[i]
			i += 1
		else:
			seq[k] = rigthSeq[j]
			j += 1

def mergeSort(seq, left, right):
	if left < right:
		mid = (left + right) // 2
		mergeSort(seq, left, mid)
		mergeSort(seq, mid + 1, right)
		merge(seq, left, mid, right)

randomSeq = list(range(1, 101))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
mergeSort(randomSeq, 0, 99)
print('After sorted:\n', randomSeq)
