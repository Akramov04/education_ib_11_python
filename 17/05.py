#def mirror(arr):
#    mirrored_part = arr.reverse() В функции mirror(arr) есть ошибка, так как метод reverse() списка изменяет исходный список, а не возвращает новый отражённый список
#    arr = arr + mirrored_part

def mirror(arr):
    mirrored_part = arr[::-1] # Справление ошибки путем копирования всего списка
    arr += mirrored_part # Добавляем в список переменную


arr = [1, 2]
mirror(arr)
print(*arr)