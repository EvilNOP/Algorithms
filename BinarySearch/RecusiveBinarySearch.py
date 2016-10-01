#T(n) = θ(lgn)

def recusionBinarySearch(seq, tarElement, low, high):
	if low == high:
		tarElement == seq[high]
		return high - 1
	else:
		mid = (low + high) // 2
		if tarElement < seq[mid]:
			return recusionBinarySearch(seq, tarElement, low, mid)
		else:
			return recusionBinarySearch(seq, tarElement, mid + 1, high)

a = list(range(0, 21))
print(recusionBinarySearch(a, 10, 0, 20))