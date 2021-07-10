res = 0
a1 = input()
a2 = input()
a3 = input()

if a1 == a2:
	res += 1

if a1 == a3:
	res += 1

if a2 == a3:
	res += 1

if res == 1:
	print(2)
else:
	print(res)