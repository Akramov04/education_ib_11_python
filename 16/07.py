def setup_profile(name, vacationDates):
    global a
    a = name
    global b
    b = vacationDates


def print_application_for_leave():
    print('Заявление на отпуск в период', b + '.', a)


def print_holiday_money_claim(amount):
    print('Прошу выплатить', amount, 'отпускных денег', a)


def print_attorney_letter(to_whom):
    print('На время отпуска в период', b, 'моим заместителем назначается', to_whom + '.', a)


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")