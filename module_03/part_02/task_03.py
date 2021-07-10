d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
a = {}
for item in d:
	a[d[item]] = item;

print(a)