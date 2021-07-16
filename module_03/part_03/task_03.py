mass = [5, 6, 901, 91, 1, 0, 66, 661, 2, 8]

res_ch = ""

max_elem = mass[0]

for iteration in range(1, len(mass)):
	for i in range(1, len(mass)):
		cur_elem_str = str(mass[i])
		max_elem_str = str(max_elem)
		j = 0

		while j < len(cur_elem_str) and j < len(max_elem_str):
			if int(cur_elem_str[j]) > int(max_elem_str[j]):
				max_elem = mass[i]
				max_elem_str = str(max_elem)
				break
			elif int(cur_elem_str[j]) < int(max_elem_str[j]):
				break
			else:
				j += 1

	res_ch += max_elem_str
	mass.remove(max_elem)
	max_elem = mass[0]

print(res_ch + str(mass[0]))
