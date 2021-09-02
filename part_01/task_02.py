class Point:
	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return Point(self.x * other.x, self.y * other.y)

	def multp(self, m):
		return Point(self.x * m, self.y * m)

	def __str__(self):
		return str(self.x) + ", " + str(self.y)

p1 = Point(3, 5)
p2 = Point(2, 1)

print(p1 - p2)
print(p1 + p2)
print(p1.multp(2))
