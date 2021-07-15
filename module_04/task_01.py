def merge_sort(a):
	if len(a) < 2:
		return a
	else:
		left = merge_sort(a[:int(len(a)/2)])
		right = merge_sort(a[int(len(a)/2):])
		return merge(left, right)

def merge(a, b):
	i, j = 0, 0
	sort_mass = []

	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			sort_mass.append(a[i])
			i += 1
		else:
			sort_mass.append(b[j])
			j += 1

	while i < len(a):
		sort_mass.append(a[i])
		i += 1

	while j < len(b):
		sort_mass.append(b[j])
		j += 1

	return sort_mass

def find_ch(number, mass):
	
	while len(mass) > 0:
		center = int(len(mass)/2)
		
		if number < mass[center]:
			mass = mass[:center]
		elif number == mass[center]:
			return "find"
		else:
			mass = mass[center:]

		if center == 0:
			return "not exist"			

mass = [5, 7, 11, 1, 4, 8, 6, 0, 3]

ch = int(input())

mass = merge_sort(mass)

if ch >= mass[0] and ch <= mass[len(mass)-1]:
	print(find_ch(ch, mass))
else:
	print("not exist")




