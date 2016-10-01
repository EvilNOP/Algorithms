from random import shuffle

def countingSort(seqA, seqB, maxKey):
	seqC = []
	for index in range(maxKey + 1):
		seqC.append(0)

	length = len(seqA)

	for index in range(length):
		seqC[seqA[index]] += 1
	
	seqC[0] -= 1
	for index in range(1, maxKey + 1):
		seqC[index] = seqC[index] + seqC[index - 1]

	for index in range(length - 1, -1, -1):
		seqB[seqC[seqA[index]]] = seqA[index]
		seqC[seqA[index]] -= 1

	return seqB

randomSeqA = list(range(1, 101))
shuffle(randomSeqA)

sequenceB = []
for i in range(100):
	sequenceB.append(0)

print('Before sorted: \n', randomSeqA)
countingSort(randomSeqA, sequenceB, 100)
print('After sorted:\n', sequenceB)