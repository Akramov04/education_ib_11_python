num_1 = float(input("Введите первое число "))
num_2 = float(input("Введите второе число "))
str = input("Введите математическую операцию ")
if str == "/" and num_2 != 0:
    print(num_1 / num_2)
if str == "+":
    print(num_1 + num_2)
if str == "-":
    print(num_1 - num_2)
if str == "*":
    print(num_1 * num_2)
else:
    print(888888)