cat = False
dog = False
n = int(input())
num = 1
for _ in range(n):
    text = input()
    if "Кот" in text or "кот" in text:
        if not dog:
            cat = True
    elif "Пёс" in text or "пёс" in text:
        dog = True
    num += 1
if cat and not dog:
    print("МЯУ")
else:
    print("НЕТ")