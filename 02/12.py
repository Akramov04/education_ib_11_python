str = input()
kop = (len(str) * 40)
rub_1 = kop % 100
kop = kop // 100
rub_2 = kop
print(rub_2, "р.", rub_1, "коп.")