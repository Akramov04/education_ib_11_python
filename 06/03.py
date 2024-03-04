english_lang = int(input())
german_lang = int(input())
a = set()
b = set()
c = 0
for i in range(english_lang):
    fam_1 = input()
    a.add(fam_1)
print()
for i in range(german_lang):
    fam_2 = input()
    b.add(fam_2)
count = len(a ^ b)
if count > 0:
    print(count)
else:
    print("NO")