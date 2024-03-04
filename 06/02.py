n = int(input())
goroda = set()
a = 0
for i in range(n):
    gorod = input()
    if gorod in goroda:
        continue
    else:
        goroda.add(gorod)
        a += 1

new_gorod = input()
if new_gorod in goroda:
   print("TRY ANOTHER")
else:
   goroda.add(new_gorod)
   a += 1
if a == n + 1:
    print("OK")