def binary_search(data, value, low_index=0, high_index=0):
	""" Returns True if value is found in array else False. """

	if not data:
		return False

	if low_index > high_index:
		return False

	midpt_index = int((high_index + low_index) // 2)
	midpt_value = data[midpt_index]

	if value == midpt_value:
		return True
	elif value < midpt_value:
		high_index = midpt_index - 1
	elif value > midpt_value:
		low_index = midpt_index + 1

	return binary_search(data, value, low_index, high_index)


data = []
print binary_search(data, 9)

data= [9]
print binary_search(data, 9, 0, len(data)-1)

data= [8, 8]
print binary_search(data, 9, 0, len(data)-1)

data = [1, 3, 3, 5, 6, 7]
print binary_search(data, 9, 0, len(data)-1)

data = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print binary_search(data, 9, 0,len(data)-1)