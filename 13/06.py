slovar = {}
answer = list()
for i in input().split():
    if i in list(slovar.keys()):
        slovar[i] += 1
    else:
        slovar[i] = 1
    answer.append(slovar[i])
for i in answer:
    print(i, end=' ')