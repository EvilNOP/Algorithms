from sys import maxsize
from random import shuffle

class MinimumHeap(object):
	def __init__ (self):
		self.heapSize = 0

	def parentNode(self, index):
		return index // 2

	def leftChildNode(self, index):
		return index * 2 + 1

	def rightChildNode(self, index):
		return index * 2 + 2

	def minimumKey(self, seq):
		return seq[0]

	#T(n) = θ(lgn)
	def minHeapify(self, seq, index):
		leftChild = self.leftChildNode(index)
		rightChild = self.rightChildNode(index)

		if leftChild <= self.heapSize - 1 and seq[leftChild] < seq[index]:
			smallest = leftChild
		else:
			smallest = index
		if rightChild <= self.heapSize - 1 and seq[smallest] > seq[rightChild]:
			smallest = rightChild

		if smallest is not index:
			seq[index], seq[smallest] = seq[smallest], seq[index]
			self.minHeapify(seq, smallest)

	#T(n) = θ(lgn)
	def extractMinimum(self, seq):
		if self.heapSize < 1:
			print('Heap underflow!')

		minimum = seq[0]
		seq[0] = seq[self.heapSize - 1]
		del seq[self.heapSize - 1]
		self.heapSize -= 1
		self.minHeapify(seq, 0)

		return minimum

	#T(n) = O(lgn)
	def decreaseKey(self, seq, index, key):
		if key > seq[index]:
			print('New key is bigger than current key!')

		seq[index] = key
		while index > 0 and seq[self.parentNode(index)] > seq[index]:
			seq[self.parentNode(index)], seq[index] = seq[index], seq[self.parentNode(index)]
			index = self.parentNode(index)

	#T(n) = O(lgn)
	def insertKey(self, seq, key):
		seq.append(maxsize)
		self.heapSize += 1
		self.decreaseKey(seq, self.heapSize - 1, key)

	#T(n) = O(n)
	def buildMinHeap(self, seq):
		self.heapSize = len(seq)
		for index in range(self.heapSize // 2 - 1, -1, -1):
			self.minHeapify(seq, index)

	#T(n) = θ(nlgn)
	def heapSort(self, seq):
		length = len(seq)
		self.buildMinHeap(seq)

		for index in range(length - 1, 0, -1):
			seq[index], seq[0] = seq[0], seq[index]
			self.heapSize -= 1
			self.minHeapify(seq, 0)

MinimumHeap = MinimumHeap()
randomSeq = list(range(1, 101))
shuffle(randomSeq)

MinimumHeap.buildMinHeap(randomSeq)
print('Minimum Heap: \n', randomSeq)

MinimumHeap.heapSort(randomSeq)
print('Original Sequence: \n', randomSeq)