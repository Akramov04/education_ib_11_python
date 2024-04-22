slov = {}
for i in range(int(input())):
    s = input().split()
    if s[2] in slov:
        slov[s[2]] += ' ' + str(s[0])
    else:
        slov[s[2]] = s[0]
for i in range(int(input())):
    s = input()
    print(slov.get(s, ''))