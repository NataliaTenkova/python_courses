d = {'name1': 'id1', 'name2': 'id1', 'name3': 'id3'}
a = {}
for item in d:
	list_value = [item]
	if d[item] in a:
		list_value.extend(a[d[item]])

	a[d[item]] = list_value

print(a)
