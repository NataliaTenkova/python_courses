class Point:
	def __init__ (self, x, y):
		self.__x = x
		self.__y = y

	def __add__(self, other):
		return Point(self._Point__x + other._Point__x, self._Point__y + other._Point__y)

	def __sub__(self, other):
		return Point(self._Point__x - other._Point__x, self._Point__y - other._Point__y)

	def __mul__(self, m):
		try:
			m = int(m)
			return Point(self._Point__x * m, self._Point__y * m)
		except ValueError:
			return "is not int value"

	def __str__(self):
		return f'{self._Point__x}, {(self._Point__y)}'

p1 = Point(3, 5)
p2 = Point(2, 1)

print(p1 - p2)
print(p1 + p2)
print(p1 * 4)