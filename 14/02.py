def space_game(text):
    if text.count(" ") % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")


text = input()
space_game(text)