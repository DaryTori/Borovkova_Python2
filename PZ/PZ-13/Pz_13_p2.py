# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

import random

n = input("Введите количество столбцов матрицы: ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите количество столбцов матрицы: ")

m = input("Введите количество строк матрицы: ")
while type(m) != int:  # обработка исключений
    try:
        m = int(m)
    except ValueError:
        print("Неправильно ввели!")
        m = input("Введите количество строк матрицы: ")

matrix = [[random.randint(1, 50) for ele in range(n)] for strok in range(m)]

print("Матрица:")
for strok in matrix:
    print(strok)

chot = [ele for strok in matrix for ele in strok if ele > 0 and ele % 2 == 0]
summa = sum(chot)
average = summa / len(chot) 

print("Положительные чётные элементы:", *chot)
print("Сумма:", summa)
print("Среднее арифметическое:", average)