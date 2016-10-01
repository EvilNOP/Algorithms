#T(n) = θ(nlgn)
from sys import maxsize
from random import shuffle

def merge(seq, left, mid, right):
	inversions = 0
	leftSeq = seq[left : mid + 1]
	rightSeq = seq[mid + 1 : right + 1]

	leftSeq.append(maxsize)
	rightSeq.append(maxsize)
	leftSeqLen = len(leftSeq) - 1

	i, j = (0, 0)

	for k in range(left, right + 1):
		if leftSeq[i] > rightSeq[j]:
			seq[k] = rightSeq[j]
			j += 1
			inversions += (leftSeqLen - i)
		else:
			seq[k] = leftSeq[i]
			i += 1

	return inversions

def countInversions(seq, left, right):
	inversions = 0
	if left < right:
		mid = (left + right) // 2
		inversions += countInversions(seq, left, mid)
		inversions += countInversions(seq, mid + 1, right)
		inversions += merge(seq, left, mid, right)
	return inversions

randomSeq = list(range(1, 101))
shuffle(randomSeq)

print('Before sorted: \n', randomSeq)
inversions = countInversions(randomSeq, 0, 99)
print('After sorted:\n', randomSeq)
print('Invetions:', inversions)