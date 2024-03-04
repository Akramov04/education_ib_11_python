list_1 = set()
list_2 = set()
for i in range(3):
    num = int(input())
    list_1.add(num)
print()
for i in range(4):
    num = int(input())
    list_2.add(num)
list_3 = list_1 & list_2
if list_3:
    print(list_3)
else:
    print("EMPTY")