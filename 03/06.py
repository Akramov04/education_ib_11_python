parol_1 = input("Введите пароль: ")
parol_2 = input("Подтвердите пароль: ")
while True:
    if len(parol_1) < 8:
        print("Короткий!")
        parol_1 = input("Введите пароль: ")
        parol_2 = input("Подтвердите пароль: ")
    elif len(parol_1) > 8 and "123" in parol_1:
        print("Простой!")
        parol_1 = input("Введите пароль: ")
        parol_2 = input("Подтвердите пароль: ")
    elif parol_1 != parol_2:
        print("Различаются.")
        parol_1 = input("Введите пароль: ")
        parol_2 = input("Подтвердите пароль: ")
    else:
        print("OK")
        break