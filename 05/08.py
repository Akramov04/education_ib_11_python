count = 0
text = ""
cat = -1
a = 1
while text != "СТОП":
    text = input()
    if "Кот" in text or "кот" in text:
        count += 1
    if ("Кот" in text or "кот" in text) and  cat == -1:
        cat = a
    a += 1
print(count, cat)