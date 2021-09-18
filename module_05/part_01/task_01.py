class StringVar:

	def __init__ (self, our_str):
		self.__our_str = our_str

	def set(self, new_str):
		self._StringVar__our_str = new_str

	def get(self):
		return self._StringVar__our_str


str1 = StringVar("hello")
print(str1.get())
str1.set("hello world")
print(str1.get())
