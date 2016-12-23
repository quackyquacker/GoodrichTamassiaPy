import math

def binary_search(data, value, high_index=0, low_index=0):
	""" Returns True if value is found in array. """

	if not data:
		return False

	midpt_index = int(math.floor((high_index + low_index) / 2))
	midpt_value = data[midpt_index]

	if high_index == low_index:
		if value == midpt_value:
			return True
		else:
			return False


	if value == midpt_value:
		return True
	elif value < midpt_value:
		high_index = midpt_index - 1
	elif value > midpt_value:
		low_index = midpt_index + 1

	return binary_search(data, value, high_index, low_index)


data = []
print binary_search(data, 9)
data= [9]
print binary_search(data, 9, len(data)-1, 0)
data= [8, 8]
print binary_search(data, 9, len(data)-1, 0)
data = [1, 3, 3, 5, 6, 9]
print binary_search(data, 9, len(data)-1, 0)
data = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print binary_search(data, 9, len(data)-1, 0)


