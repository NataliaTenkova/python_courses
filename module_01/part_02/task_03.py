while 1 == 1:
	passwrd = input()
	low_c = 0
	up_c = 0

	for c in passwrd:
		if c.islower():
			low_c += 1
		else:
			up_c += 1

	if len(passwrd) > 8 and low_c > 0 and up_c > 0:
		print("passwrd is correct")
		break
	else:
		print("passwrd not correct. try again")

