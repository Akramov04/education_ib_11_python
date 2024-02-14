question_1 = input("Любите ли вы котиков? ")
question_2 = input("Умеете ли вы программировать? ")
if question_1 == "да" and question_2 == "да":
    print("Вы обладаете незаурядным умом")
elif question_1 == "да" and question_2 == "нет":
    print("Вы любите котиков и желаете стать программистом")
elif question_1 == "нет" and question_2 == "да":
    print("Вы программист, который не любит котиков")
elif question_1 == "нет" and question_2 == "нет":
    print("Вы не программист и не любите котиков, но это можно исправить")
else:
    print("Ошибка")