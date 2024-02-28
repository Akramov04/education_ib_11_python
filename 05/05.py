cat = False
count = 0
text = ""
while True:
    text = input()
    count += 1
    if ('кот' in text) or ('Кот' in text):
        cat = True
        print(count)
        break
    if text == 'СТОП':
        print(-1)
        break