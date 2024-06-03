import random

def make_bingo():
    numbers = list(range(1, 76))
    random.shuffle(numbers)
    bingo_card = []
    for i in range(5):
        row = []
        for j in range(5):
            if i == 2 and j == 2:
                row.append(0)
            else:
                row.append(numbers.pop())
        bingo_card.append(tuple(row))
    return tuple(bingo_card)

res = make_bingo()
print(*res, sep="\n")