import re

while True:
	passwrd = input()
	low_c = 0
	up_c = 0

	for c in passwrd:
		if re.match(r'[a-z]', c):
			low_c += 1
		if re.match(r'[A-Z]', c):
			up_c += 1

	if len(passwrd) > 8 and low_c > 0 and up_c > 0:
		print("passwrd is correct")
		break
	else:
		print("passwrd not correct. try again")

