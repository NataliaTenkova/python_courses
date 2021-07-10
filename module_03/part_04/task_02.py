import json

def register(login, passwrd):
	data = {}

	with open('db_login.json', 'r') as f:
		data = json.load(f)

	if login in data.keys():
		print("exist")
	else:
		with open('db_login.json', 'w') as f:
			data[login] = passwrd
			json.dump(data, f)

login = input()
passwrd = input()
register(login, passwrd)