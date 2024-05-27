def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y if y != 0 else "Делить на ноль нельзя!"
    else:
        return "ошибка"


operation = arithmetic_operation('+')
print(operation(1, 4))