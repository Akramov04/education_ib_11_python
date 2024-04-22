phones = {}
for i in range(int(input())):
    number, name = input().split()
    if name not in phones:
        phones[name] = []
    phones[name].append(number)
for i in range(int(input())):
    name = input()
    if name not in phones:
        print("Нет в телефонной книге")
    else:
        print(" ".join(str(x) for x in phones[name]))