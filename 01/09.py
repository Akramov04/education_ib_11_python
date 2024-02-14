login_1 = input("Введите ваш логин: ")
mail_1 = input("Введите резервный адрес электронной почты: ")
if "@" in login_1:
    print("Некорректный логин")
elif "@" not in mail_1:
    print("Некорректный адрес")
else:
    print("OK")