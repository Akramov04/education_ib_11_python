parol_1 = input()
parol_2 = input()
if len(parol_2) <= 8 and len(parol_1) <= 8:
    print(parol_1, "и", parol_2, "Короткие!")
elif len(parol_1) <= 8:
    print(parol_1, "Короткий!")
elif len(parol_2) <= 8:
    print(parol_2, "Короткий!")
elif len(parol_2) > 8 and str(parol_1) != str(parol_2):
    print("Различаются.")
else:
    print("OK")