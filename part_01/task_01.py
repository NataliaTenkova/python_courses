class StringVar:

	def __init__ (self, str):
		self.str = str

	def set(self, new_str):
		self.str = new_str

	def get(self):
		print(self.str)


str1 = StringVar("hello")
str1.get()
str1.set("hello world")
str1.get()
