print("Ваш персонаж находится в комнате, из которой есть несколько ходов")
move_1 = input("Выберите в какой из ходов вы пойдёте - 1, 2 или 3 ")
if move_1 == "1":
    print("Вы вышли прямиком в лапы медведю и он вас растерзал")
elif move_1 == "2":
    move_2 = input('Вы находитесь в пещере на развилке. Вы можете пойти "налево", "направо" или "прямо". Введите одно из слов для выбора. ')
    if move_2 == "налево":
        move_3 = input('Вы направились налево. Через некоторое время вы дошли до двух дверей. Вы выберете "левая" или "правая"? ')
        if move_3 == "правая":
            print("Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком!")
        elif move_3 == "левая":
            print("Вы зашли в гости к крокодилу, который не был доброжелателен")
    elif move_2 == "направо":
        print("Поздравляем! Вы нашли верный выход и выбрались из лабиринта!")
    elif move_2 == "прямо":
        print("Вы пошли через реку и утонули")
elif move_1 == "3":
    print("Вы погибли в бою с скелетами")

else:
    print("Ошибка")