from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
max_value = m[0][0]
for row in m:
	for elem in row:
		max_value = max(max_value, elem)

print(m)
print(max_value)
