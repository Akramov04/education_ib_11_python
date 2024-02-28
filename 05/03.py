cat = False
count = 0
text = ''
while text != 'СТОП':
    text = input()
    count += 1
    while not(cat):
        if ('Кот' in text) or ('кот' in text):
            cat = True
            num = count
        break
if cat:
    print(num)
else:
    print(-1)