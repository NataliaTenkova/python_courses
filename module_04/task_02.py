mass = [5, 7, 11, 1, 4, 8, 6, 0, 3, 36, 3, 9]
sort_mass = [mass[0]]

for elem in mass[1:]:

	index = 0
	insert_elem = 0

	while index < len(sort_mass):
		if elem < sort_mass[index]:
			if index == 0:
				sort_mass.insert(0, elem)
			else:
				sort_mass.insert(index, elem)
			insert_elem = 1
			break
		else:
			index += 1

	if insert_elem == 0:
		sort_mass.append(elem)

print(sort_mass)