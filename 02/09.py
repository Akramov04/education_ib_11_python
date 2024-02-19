rost_1 = int(input())
rost_2 = int(input())
rost_3 = int(input())
if rost_1 > rost_2 > rost_3:
    print(rost_1)
    print(rost_2)
    print(rost_3)
elif rost_1 > rost_3 > rost_2:
    print(rost_1)
    print(rost_3)
    print(rost_2)
elif rost_2 > rost_1 > rost_3:
    print(rost_2)
    print(rost_1)
    print(rost_3)
elif rost_2 > rost_3 > rost_1:
    print(rost_2)
    print(rost_3)
    print(rost_1)
elif rost_3 > rost_2 > rost_1:
    print(rost_3)
    print(rost_2)
    print(rost_1)
elif rost_3 > rost_1 > rost_2:
    print(rost_3)
    print(rost_1)
    print(rost_2)
else:
    print(rost_1)
    print(rost_2)
    print(rost_3)