import json

class BookModel:
	title = "First letter"
	text = "New book"
	author = "Ivanov"

	def save(self):
		attr = list(filter(lambda x: not x.startswith("__") and x != "save", dir(self)))
		d = {}
		for item in attr:
			d[item] = getattr(self, item)

		with open('attributes.json', 'w') as f:
				json.dump(d, f)

class Journal(BookModel):
	tirage = 3000


m1 = Journal()
m1.save()
