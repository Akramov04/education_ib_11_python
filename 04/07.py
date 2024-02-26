num = int(input("Введите число: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()
if num == 1:
    print("НЕТ")
elif num == 2:
    print("ПРОСТОЕ")
else:
    print("НЕТ")