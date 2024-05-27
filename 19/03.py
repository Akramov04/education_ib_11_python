filter_num = filter(lambda x: x % 9 == 0, range(10, 100))
square = map(lambda x: x ** 2, filter_num)
res = sum(square)
print(res)