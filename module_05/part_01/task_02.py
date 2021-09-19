class Point:
	def __init__ (self, x, y):
		self.__x = x
		self.__y = y

	def __add__(self, other):
		return Point(self.__x + other.__x, self.__y + other.__y)

	def __sub__(self, other):
		return Point(self.__x - other.__x, self.__y - other.__y)

	def __mul__(self, m):
		try:
			m = int(m)
			return Point(self.__x * m, self.__y * m)
		except ValueError:
			return "is not int value"

	def __str__(self):
		return f'{self.__x}, {(self.__y)}'

p1 = Point(3, 5)
p2 = Point(2, 1)

print(p1 - p2)
print(p1 + p2)
print(p1 * 4)