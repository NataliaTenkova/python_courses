from random import randint
n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
max = -35000
for row in m:
	for elem in row:
		if elem > max:
			max = elem
print(m)
print(max)