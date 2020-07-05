#Write a binary search function. It should take a sorted sequence and
#the item it is looking for. It should return the index of the item if found.
#It should return -1 if the item is not found.

def search(a, x):
	low = 0
	high = len(a) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		if a[mid] < x:
			low = mid + 1

		elif a[mid] > x:
			high = mid - 1

		else:
			return mid
	return -1


list = [ 1,7,11,55,99,101,123 ]
x = 99


result = search(list, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
