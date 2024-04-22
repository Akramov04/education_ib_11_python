slovar = {}
for i in range(int(input())):
    s = input()
    word = s.split()
    slovar[word[0]] = s[len(word[0]) + 1:]
for i in range(int(input())):
    word = input()
    if word not in slovar:
        print('Нет в словаре')
    else:
        print(slovar[word])