#T(n) = θ(lgn)

def binarySearch(seq, targetElement):
	low = 0
	high = len(seq) - 1

	while low <= high:
		mid = (low + high) // 2
		midVal = seq[mid]

		if midVal < targetElement:
			low = mid + 1
		elif midVal > targetElement:
			high = mid - 1
		else:
			return mid
	return False

a = list(range(0, 20))
print(binarySearch(a, 2))