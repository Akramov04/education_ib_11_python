print("Загадайте в уме число от 1 до 1000")
min_num = 1
max_num = 1000
a = 0
while a < 10:
    mid_num = (min_num + max_num) // 2
    print("Попробую угадать! Это число: ", mid_num)
    otvet = input('Введите символ ">", если число больше; введите символ "<", если число меньше; введите "=", если число верное: ')
    if otvet == ">":
        min_num = mid_num + 1
    elif otvet == "<":
        max_num = mid_num - 1
    elif otvet == "=":
        print("Число совпало с вашим! Это здорово!")
        break
    else:
        print("Ошибка!")

    a+=1
    if min_num > max_num:
        print("Потрачены все попытки угадать число. Неудача.")
        break