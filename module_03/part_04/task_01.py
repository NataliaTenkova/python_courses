import json

def registr(login, passwrd):
	data = {login: passwrd}
	with open('db_login.json', 'a') as f:
		json.dump(data, f)

login = input()
passwrd = input()
registr(login, passwrd)