def month_name(number, lang):
    ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
        'октябрь', 'ноябрь', 'декабрь']
    en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
          'october', 'november', 'december']
    if lang == "ru":
        return ru[number - 1]
    return en[number - 1]


print(month_name(3, "ru"))