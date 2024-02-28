n = int(input())
evrasia = "Евразия"
ostasia = "Остазия"
for i in range(n):
    country = input()
    if country == 'С кем война?':
        print(evrasia)
    if country == 'С кем мир?':
        print(ostasia)
    if country == 'Меняем':
        evrasia, ostasia = ostasia, evrasia