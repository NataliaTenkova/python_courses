ch = int(input("Введите число:"))
sum = 0 

while ch >= 1 :
	sum = sum + ch % 10
	ch = ch // 10

print(sum)