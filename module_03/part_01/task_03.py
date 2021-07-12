ch = int(input("Введите число:"))
sum = 0 

while ch > 0 :
	sum += ch % 10
	ch //= 10

print(sum)
