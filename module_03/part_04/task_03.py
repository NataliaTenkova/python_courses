import json

def register(login, passwrd):
	data = {}

	with open('db_login.json', 'r') as f:
		data = json.load(f)

	if login in data.keys():
		if data[login] == passwrd:
			print("sucsess")
		else:
			print("password is incorrect. try again")
			passwrd = input()
			register(login,passwrd)
	else:
		print("login not exist. register? (y/n)")
		ans = input()
		if ans == 'y':
			with open('db_login.json', 'w') as f:
				data[login] = passwrd
				json.dump(data, f)

login = input()
passwrd = input()
register(login, passwrd)