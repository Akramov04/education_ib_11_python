money = int(input())
den_1 = money / 8
while (money // 8) != 0:
    money //= 8
    print("Итог ", money)
