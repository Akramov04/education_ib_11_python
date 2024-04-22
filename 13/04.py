point = {}
for i in range(int(input())):
    coordinate = input().split()
    a = (coordinate[0][:len(coordinate[0]) - 1], coordinate[-1][:len(coordinate[-1]) -1])
    if a in point:
        point[a] += 1
    else:
        point[a] = 1
print(max(point.values()))