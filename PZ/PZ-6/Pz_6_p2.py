# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

import random


def find_l_min(lst):
    if len(lst) == 1:
        loc_min = 0
        return loc_min

    # Проверка первого числа
    if lst[0] < lst[1]:
        loc_min = 0
        return loc_min

    # Проверка эл-тов с 1 до предпоследнего
    for i in range(1, n - 1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            loc_min = i
            return loc_min

    # Проверка последнего эл-та
    if lst[-1] < lst[-2]:
        loc_min = n - 1
        return loc_min


n = input("Введите длину списка: ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите длину списка: ")

spisoc = []
i = 0
while i < n:
    spisoc.append(random.randint(0, 100))
    i += 1

l_min = find_l_min(spisoc)
print("Список:", spisoc)
print("Номер первого локального минимума списка:", l_min)