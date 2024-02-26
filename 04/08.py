n = int(input("Введите кол-во секунд: "))
if n>= 0:
    print("Осталось секунд: ", n)
    for i in range(n):
        n-=1
        print("Осталось секунд: ", n)
    print("Пуск")
elif n < 0:
    print("Пуск")