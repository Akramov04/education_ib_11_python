n = int(input("Введите число: "))
a = 1
while n > 1:
    a *= n
    n -= 1
    if n == 0:
        print(1)
print(a)