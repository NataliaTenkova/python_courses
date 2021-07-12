x = int(input("Введите начальный взнос:"))
y = int(input("Введите желаемую сумму:"))
p = int(input("Введите процент:"))

sum = x
year = 0 

if y <= sum :
	print("У вас уже есть такая сумма")
else :
	while sum < y :
		sum += int(sum * 0.01 * p)
		year += 1

print(year)
