res = 0
a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1 == a2:
	res += 1

if a1 == a3:
	res += 1

if a2 == a3:
	res += 1

print(2 if res == 1 else res)
