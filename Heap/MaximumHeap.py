from sys import maxsize
from random import shuffle
 
class MaximumHeap(object):
	def __init__ (self):
		self.heapSize = 0

	def parentNode(self, index):
		return index // 2

	def leftChildNode(self, index):
		return index * 2 + 1

	def rightChildNode(self, index):
		return index * 2 + 2

	def maximumKey(self, seq):
		return seq[0]

	#T(n) = θ(lgn)
	def maxHeapify(self, seq, index):
		leftChild = self.leftChildNode(index)
		rightChild = self.rightChildNode(index)

		if leftChild <= self.heapSize - 1 and seq[leftChild] > seq[index]:
			largest = leftChild
		else:
			largest = index
		if rightChild <= self.heapSize - 1 and seq[largest] < seq[rightChild]:
			largest = rightChild

		if largest is not index:
			seq[index], seq[largest] = seq[largest], seq[index]
			self.maxHeapify(seq, largest)

	#T(n) = θ(lgn)
	def extractMaximum(self, seq):
		if self.heapSize < 1:
			print('Heap underflow!')

		maximum = seq[0]
		seq[0] = seq[self.heapSize - 1]
		del seq[self.heapSize - 1]
		self.heapSize -= 1
		self.maxHeapify(seq, 0)

		return maximum

	#T(n) = O(lgn)
	def increaseKey(self, seq, index, key):
		if key < seq[index]:
			print('New key is smaller than current key!')

		seq[index] = key
		while index > 0 and seq[self.parentNode(index)] < seq[index]:
			seq[self.parentNode(index)], seq[index] = seq[index], seq[self.parentNode(index)]
			index = self.parentNode(index)

	#T(n) = O(lgn)
	def insertKey(self, seq, key):
		seq.append(-maxsize)
		self.heapSize += 1
		self.increaseKey(seq, self.heapSize - 1, key)

	#T(n) = O(n)
	def buildMaxHeap(self, seq):
		self.heapSize = len(seq)
		for index in range(self.heapSize // 2 - 1, -1, -1):
			self.maxHeapify(seq, index)

	#T(n) = θ(nlgn)
	def heapSort(self, seq):
		length = len(seq)
		self.buildMaxHeap(seq)

		for index in range(length - 1, 0, -1):
			seq[index], seq[0] = seq[0], seq[index]
			self.heapSize -= 1
			self.maxHeapify(seq, 0)

MaximumHeap = MaximumHeap()
randomSeq = list(range(1, 101))
shuffle(randomSeq)

MaximumHeap.buildMaxHeap(randomSeq)
print('Maximum Heap: \n', randomSeq)

MaximumHeap.heapSort(randomSeq)
print('Original Sequence: \n', randomSeq)