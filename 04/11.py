n = int(input("Кол-во тестируемых людей: "))
iq_n = 0
for i in range(1, n + 1):
    iq = int(input())
    iq_n += iq
    factor = iq_n / i
    if factor == iq:
        print(0)
    elif factor > iq:
        print("<")
    else:
        print(">")