l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
dbl = []

for i in l:
	if l.count(i) > 1 and i not in dbl:
		dbl.append(i)

print(dbl)