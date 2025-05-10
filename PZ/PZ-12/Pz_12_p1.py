#Организовать и вывести последовательность из N случайных целых чисел. Из
#исходной последовательности организовать первую последовательность, содержащую
#числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
#полученных последовательностях

import random

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

print('Изначальная последовательность:', spisoc)
krat_tri = list(filter(lambda x: x % 3 == 0, spisoc))
print('Кратны трём', krat_tri, 'количество элементов:', len(krat_tri))
ne_krat = list(filter(lambda x: x % 3 != 0, spisoc))
print('Не кратны трём', ne_krat, 'количество элементов:', len(ne_krat))