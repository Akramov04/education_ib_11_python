translated_text = ''


def translate(text):
    global translated_text
    letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е', '.', ',', '-']
    for i in range(len(text) - 1):
        if letters.count(text[i]) == 0:
            translated_text = translated_text + text[i]
    translated_text = " ".join(translated_text.split())
    return translated_text


translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
print(translated_text)