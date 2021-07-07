x = float(input("Введите 1 число:"))
y = float(input("Введите 2 число:"))
s = (x > y) * x + (x <= y) * y
print(s)