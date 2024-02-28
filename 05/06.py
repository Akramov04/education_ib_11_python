count = 0
sum = 0
n = 0
num = int(input())
while num != 0:
    if num == 0:
        break
    count += 1
    sum += num
    if sum == 10:
        n += count
    num = int(input())
print(n)
