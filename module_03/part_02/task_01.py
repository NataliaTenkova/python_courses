input_list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
duplicates = []

for elem in input_list:
	if elem not in duplicates and input_list.count(elem) > 1:
		duplicates.append(elem)

print(duplicates)