def find_max(numbers_list):
	largest = numbers_list[0]

	for item in numbers_list:
		if item > largest:
			largest = item
	return largest
