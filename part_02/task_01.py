import json

class Model:
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

m1 = Model()
m1.save()
