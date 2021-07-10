def area(a, b, c):
	p = (a + b + c)/2
	s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

	return s

a = int(input())
b = int(input())
c = int(input())

print(area(a, b, c))