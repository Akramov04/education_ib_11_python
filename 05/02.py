n = int(input("Введите кол-во строк: "))
a = False
for i in range(n):
    text = input()
    if "Кот" in text or "кот" in text:
        print("МЯУ")
else:
    print("НЕТ")